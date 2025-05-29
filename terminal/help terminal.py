list_cards = []
list_ranks = []

suits = ['♠', '♥', '♦', '♣']    #card symbols
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] #13 cards

#strings for adding into lists
suit_str = ""
rank_str = ""
final =""

for q in range(4):  #4 card decks
    suit_num = 0
    for i in range(4): #all suits
        rank_num = 0
        card_rank = 2
        for j in range(13): #all ranks
            suit_str = suits[suit_num]
            rank_str = ranks[rank_num]
            final = suit_str + rank_str
            list_cards.append(final)
            rank_num += 1
            list_ranks.append(card_rank)

            if card_rank < 10:
                card_rank +=1

        suit_num += 1
        
        
    

print(list_cards)
print(list_ranks)