import pygame
from pygame.locals import *
import sys

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# display surface
DISPLAYSURF = pygame.display.set_mode((300, 300))
DISPLAYSURF.fill((255, 255, 255))  # white
pygame.display.set_caption("Hopscotch")


# Game loop begins
while True:
    # game goes here
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    FramePerSec.tick(FPS)
