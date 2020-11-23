import pygame
from pygame.locals import *
pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

red = (25, 100, 0)

display = pygame.display.set_mode((500, 500))
display.fill(red)
pygame.display.set_caption("hello")


class Player:
    lives = 5
    pressed = pygame.key.get_pressed()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
