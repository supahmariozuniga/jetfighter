import pygame
from pygame.locals import *
pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

red = (25, 100, 0)

display = pygame.display.set_mode((500, 500))
display.fill(red)
pygame.display.set_caption("hello")


class player:
    lives = 5
    pressed = pygame.key.get_pressed()
    
    def __init__(self, up, down, left, right):
        self.up = pressed(up)
        self.down = pressed(down)
        self.left = pressed(left)
        self.right = pressed(right)
    
    def update(self):
        if self.up:
            

player1 = player(K_W, K_S, K_A, K_D)

        

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
