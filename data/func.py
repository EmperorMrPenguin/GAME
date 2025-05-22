import pygame
from pygame.locals import *

def scaling(new_height, link): #will convert img in ratio, import height
    card = pygame.image.load(link).convert()
    original_width, original_height = card.get_size()   
    new_width = int(original_width * (new_height / original_height))    #calculate width by ratio
    resized_image = pygame.transform.scale(card, (new_width, new_height))   #make new proportions for the newly created smaller img
    return (resized_image)