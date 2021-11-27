import pygame
from pygame.locals import *

# New Screen
pygame.init()
screen = pygame.display.set_mode((1920//2, 1080//2))

# FPS Control
CLOCK = pygame.time.Clock()

# Game Logic
running = True
while running:
    
    # fill the screen with white background - R = 255, G = 255, B = 255
    screen.fill((255,255,255))

    # for every event loop
    for event in pygame.event.get():
        if event.typee == QUIT:
            running = False

    # control FPS - ingame
    CLOCK.tick(60)

    # control Screen updating
    pygame.display.update()

# Quitting
pygame.quit()
