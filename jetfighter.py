import pygame
from pygame.locals import *
pygame.init()


height = 500
width = 500
display = pygame.display.set_mode((height, width))
pygame.display.set_caption("hello")


class player(pygame.sprite.Sprite):
    lives = 5

    def __init__(self, left, right, img):
        super(player, self).__init__()
        self.surface = pygame.image.load(img).convert_alpha()
        self.rect = self.surface.get_rect()
        self.left = left
        self.right = right

    def update(self):
        if pressed[self.left]:
            self.surface.move_ip(-5, 0)


player1 = player(K_LEFT, K_RIGHT, "jet1.png")
player2 = player(K_a, K_d, "jet2.png")


open = True
while open:
    for event in pygame.event.get():
        if pygame.key.get_pressed()[K_ESCAPE]:
            open = False
        elif event.type == QUIT:
            open = False

    pressed = pygame.key.get_pressed()

    player.update(pressed)

    display.blit(player1.surface, (width/4, height/4))
    display.blit(player2.surface, (.75 * width, .75 * height))

    pygame.display.flip()

    if pressed[K_UP]:
        display.fill((0, 5, 50))
        pygame.draw.circle(display, (0, 0, 255), (250, 250), 75)
        print(player2.left)
