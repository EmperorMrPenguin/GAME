import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load card image
card_img = pygame.image.load("resources\cards better/2_of_clubs.png").convert_alpha()
card_rect = card_img.get_rect()
card_rect.topleft = (100, 100)  # Start position

# Target position
target_pos = (400, 300)
speed = 10  # Pixels per frame

def move_towards(current, target, speed):
    x, y = current
    tx, ty = target
    dx, dy = tx - x, ty - y
    distance = (dx ** 2 + dy ** 2) ** 0.5
    if distance <= speed:
        return target
    else:
        ratio = speed / distance
        return (x + dx * ratio, y + dy * ratio)

# Game loop
moving = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 120, 0))  # Green background

    if moving:
        card_rect.topleft = move_towards(card_rect.topleft, target_pos, speed)
        if card_rect.topleft == target_pos:
            moving = False

    screen.blit(card_img, card_rect)
    pygame.display.flip()
    clock.tick(60)
