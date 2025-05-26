import pygame, os, time, random
from pygame.locals import *
from data.func import *  #import the function from your other file

pygame.init()

#screen adjustment
os.environ["SDL_VIDEO_CENTERED"] = "1" #center the window
screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
    #info = pygame.display.Info()    #get screen info, saved for future update!
    #screen_width = info.current_w
    #screen_height = info.current_h
    #screen = pygame.display.set_mode((screen_width - 10,screen_height - 50),pygame.RESIZABLE) #creating the game window with current screen

pygame.display.set_caption("BLACXKJACK") #name of window

#fps settings
fps = 20
clock = pygame.time.Clock()
run = True

#background
GREEN = (0, 127, 0)
RED = (235, 0, 0)

#cards
target_pos = (100, 50) # x, y

d_card_pos = [(20, 20), (20, 20), (400, 20)] #positin of dealers cards


speed = 50  # Pixels per frame (how fast is the animation)

card_deck = scaling(200,"resources\cards better/rub.png")  #resize img with function, ()for adding height and path for the file
#resized card is 200 x 290px

card_d_1 = scaling(200,"resources\cards better/2_of_clubs.png")
card_d_2 = scaling(200,"resources\cards better/5_of_clubs.png")

#rect Dealer 1
card_rect = card_d_1.get_rect()
card_rect.topleft = (1100, 20)


#Buttons
button_color = (0, 128, 255)
# Define button 1
font = pygame.font.SysFont(None, 36)
button_rect_1 = pygame.Rect(1100, 350, 140, 50) #button coordinates and width/height
button_text_1 = font.render("HIT", True, (255, 255, 255))

# Define button 2
font = pygame.font.SysFont(None, 36)
button_rect_2 = pygame.Rect(1100, 430, 140, 50) #button coordinates and width/height
button_text_2 = font.render("STAND", True, (255, 255, 255))

# Define button 3
font = pygame.font.SysFont(None, 36)
button_rect_3 = pygame.Rect(1100, 510, 140, 50) #button coordinates and width/height
button_text_3 = font.render("DOUBLE", True, (255, 255, 255))

# Define button 4
font = pygame.font.SysFont(None, 36)
button_rect_4 = pygame.Rect(1100, 590, 140, 50) #button coordinates and width/height
button_text_4 = font.render("RESTART", True, (255, 255, 255))

d_pos = 0
d_cards = 1
clicked_1 = False
clicked_2 = False
clicked_3 = False
clicked_4 = False

while run: 
    #shutting the game down 
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            run = False

        
    #mouse clicks for buttons
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    # button 1 bet
    if button_rect_1.collidepoint(mouse_pos):
        if mouse_pressed[0] and not clicked_1:
            print("Hit!")
            clicked_1 = True
        elif not mouse_pressed[0]:
            clicked_1 = False  # Reset click state when button is released    
    # button 2 stand
    if button_rect_2.collidepoint(mouse_pos):
        if mouse_pressed[0] and not clicked_2:
            print("STAND!")
            clicked_2 = True
        elif not mouse_pressed[0]:
            clicked_2 = False  # Reset click state when button is released
    # button 3 double
    if button_rect_3.collidepoint(mouse_pos):
        if mouse_pressed[0] and not clicked_3:
            print("DOBLE!")
            clicked_3 = True
        elif not mouse_pressed[0]:
            clicked_3 = False  # Reset click state when button is released 
    # button 4 restart
    if button_rect_4.collidepoint(mouse_pos):
        if mouse_pressed[0] and not clicked_4:
            print("RESTART!")
            screen.fill(GREEN)
            clicked_4 = True
            moving = True
        #elif not mouse_pressed[0]:
           # clicked_4 = False  # Reset click state when button is released


    if clicked_4:
        card_rect.topleft = move_towards(card_rect.topleft, d_card_pos[d_pos], speed)
    elif card_rect.topleft == d_card_pos[d_pos]:
        d_pos+=1
        clicked_4 = False
        print(iehutrhgoewriug)





    screen.fill(GREEN)
    screen.blit(card_deck, (1100, 20))       # card deck
    screen.blit(card_d_1, card_rect.topleft) # moving
    screen.blit(card_d_2, card_rect.topleft) # moving card
    
    #button 1 blit
    pygame.draw.rect(screen, button_color, button_rect_1)  # draw button
    screen.blit(button_text_1, (button_rect_1.x + 20, button_rect_1.y + 10))  # draw text

    #button 2 blit
    pygame.draw.rect(screen, button_color, button_rect_2)  # draw button
    screen.blit(button_text_2, (button_rect_2.x + 20, button_rect_2.y + 10))  # draw text

    #button 3 blit
    pygame.draw.rect(screen, button_color, button_rect_3)  # draw button
    screen.blit(button_text_3, (button_rect_3.x + 20, button_rect_3.y + 10))  # draw text

    #button 4 blit
    pygame.draw.rect(screen, button_color, button_rect_4)  # draw button
    screen.blit(button_text_4, (button_rect_4.x + 20, button_rect_4.y + 10))  # draw text

    #updatuje display
    pygame.display.update()
    #aby to běželo na počet fps
    clock.tick(fps)

pygame.quit()