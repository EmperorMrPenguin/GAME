import pygame, os, time

pygame.init()

#screen adjustment
os.environ["SDL_VIDEO_CENTERED"] = "1" #center the window
info = pygame.display.Info()    #get screen info
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width - 10,screen_height - 50),pygame.RESIZABLE) #creating the game window with current screen

pygame.display.set_caption("BLACXKJACK") #name of window

#fps settings
fps = 20
clock = pygame.time.Clock()


test_img = pygame.image.load("resources/cards/2_of_clubs.svg")

run = True
while run: 
    #shutting the game down 
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            run = False

    screen.blit(test_img,(200,200))



    pygame.display.update()
    clock.tick(fps)

pygame.quit()