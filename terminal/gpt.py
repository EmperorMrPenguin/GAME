import curses
import random
import time

suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {r: min(10, int(r)) if r.isdigit() else 10 for r in ranks}
values['A'] = 11


def create_deck():
    return [(rank, suit) for suit in suits for rank in ranks]


def calculate_hand_value(hand):
    value = sum(values[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value


def draw_hand(win, y, x, label, hand, hidden=False):
    win.addstr(y, x, f"{label}: ")
    for i, card in enumerate(hand):
        display = "[??]" if hidden and i == 1 else f"[{card[0]}{card[1]}]"
        win.addstr(y, x + len(label) + 2 + i * 5, display)


def draw_button(win, y, x, label):
    win.addstr(y, x, f"[ {label} ]")
    return (y, x, x + len(label) + 3)  # (row, start_col, end_col)


def is_button_clicked(mouse_y, mouse_x, button):
    y, x1, x2 = button
    return mouse_y == y and x1 <= mouse_x <= x2


def blackjack_game(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS)
    stdscr.nodelay(0)

    deck = create_deck()
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    player_turn = True
    game_over = False
    message = ""

    while True:
        stdscr.clear()

        draw_hand(stdscr, 2, 2, "Dealer", dealer_hand, hidden=player_turn)
        draw_hand(stdscr, 4, 2, "Player", player_hand)
        stdscr.addstr(6, 2, f"Player Value: {calculate_hand_value(player_hand)}")

        hit_button = draw_button(stdscr, 8, 2, "HIT")
        stand_button = draw_button(stdscr, 8, 12, "STAND")

        if game_over:
            stdscr.addstr(10, 2, message)
            quit_button = draw_button(stdscr, 12, 2, "QUIT")
            restart_button = draw_button(stdscr, 12, 12, "RESTART")
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()

            if game_over:
                if is_button_clicked(my, mx, quit_button):
                    break
                elif is_button_clicked(my, mx, restart_button):
                    blackjack_game(stdscr)
                    return
            elif player_turn:
                if is_button_clicked(my, mx, hit_button):
                    player_hand.append(deck.pop())
                    if calculate_hand_value(player_hand) > 21:
                        message = "Player busts! Dealer wins."
                        game_over = True
                elif is_button_clicked(my, mx, stand_button):
                    player_turn = False
                    while calculate_hand_value(dealer_hand) < 17:
                        dealer_hand.append(deck.pop())
                        stdscr.clear()
                        draw_hand(stdscr, 2, 2, "Dealer", dealer_hand)
                        draw_hand(stdscr, 4, 2, "Player", player_hand)
                        stdscr.refresh()
                        time.sleep(1)

                    p_val = calculate_hand_value(player_hand)
                    d_val = calculate_hand_value(dealer_hand)
                    if d_val > 21:
                        message = "Dealer busts! Player wins."
                    elif d_val > p_val:
                        message = "Dealer wins."
                    elif d_val < p_val:
                        message = "Player wins!"
                    else:
                        message = "Push (Tie)."
                    game_over = True


if __name__ == "__main__":
    curses.wrapper(blackjack_game)
