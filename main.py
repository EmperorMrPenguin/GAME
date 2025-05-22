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
resized_image = scaling(200,"resources\cards better/rub.png")  #resize img with function, ()for adding height and path for the file
#resized card is 200 x 290px

x=20
while run: 
    #shutting the game down 
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            run = False

    x+=1


    screen.fill(GREEN)
    screen.blit(resized_image,(1100,20))    #card deck
    

    #updatuje display
    pygame.display.update()
    #aby to běželo na počet fps
    clock.tick(fps)

pygame.quit()