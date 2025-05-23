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

#


target_pos = (400, 300)
speed = 50  # Pixels per frame
#

#cards
card_deck = scaling(200,"resources\cards better/rub.png")  #resize img with function, ()for adding height and path for the file
#resized card is 200 x 290px

card_d_1 = scaling(200,"resources\cards better/2_of_clubs.png")
card_d_2 = scaling(200,"resources\cards better/5_of_clubs.png")


card_rect = card_d_1.get_rect()
card_rect.topleft = (1100, 20)

# Define button
font = pygame.font.SysFont(None, 36)
button_rect = pygame.Rect(250, 200, 140, 50)
button_color = (0, 128, 255)
button_text = font.render("Click me", True, (255, 255, 255))

x=0
moving = True
while run: 
    #shutting the game down 
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            run = False

    

    if moving:
        card_rect.topleft = move_towards(card_rect.topleft, target_pos, speed)
    elif card_rect.topleft == target_pos:
        moving = False
        
    # Check for mouse click
    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):
            print("Button clicked!",x)
            x+=1
#DOBBLE CLICK!!!!!
    
    screen.fill(GREEN)
    screen.blit(card_deck, (1100, 20))       # card deck
    screen.blit(card_d_1, card_rect.topleft) # moving card
    
    pygame.draw.rect(screen, button_color, button_rect)  # draw button
    screen.blit(button_text, (button_rect.x + 20, button_rect.y + 10))  # draw text

    #updatuje display
    pygame.display.update()
    #aby to běželo na počet fps
    clock.tick(fps)

pygame.quit()