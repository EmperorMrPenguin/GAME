import pygame, os, time
from pygame.locals import *

pygame.init()

#screen adjustment
os.environ["SDL_VIDEO_CENTERED"] = "1" #center the window
screen = pygame.display.set_mode((1280,720),pygame.RESIZABLE)
    #info = pygame.display.Info()    #get screen info
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


img = pygame.image.load("resources\cards better/3_of_clubs.png")
img.convert()
rect = img.get_rect()
moving = False

while run: 
    #shutting the game down 
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            run = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)



    #background
    screen.fill(GREEN)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    #updatuje display
    pygame.display.update()
    #aby to běželo na počet fps
    clock.tick(fps)

pygame.quit()