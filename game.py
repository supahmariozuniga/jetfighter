import pygame
from pygame.locals import *
pygame.init()


height = 500
width = 500
display = pygame.display.set_mode((height, width))
pygame.display.set_caption("hello")


class Player(pygame.sprite.Sprite):
    lives = 5

    def __init__(self, left, right, img):
        super(Player, self).__init__()
        self.surface = pygame.image.load(img).convert_alpha()
        self.rect = self.surface.get_rect()
        self.left = left
        self.right = right

    def update(self, function):
        if function[self.left]:
            self.rect.move_ip(-5, 0)
        if function[self.right]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height



player1 = Player(K_LEFT, K_RIGHT, "jet1.png")
player2 = Player(K_a, K_d, "jet2.png")

display.blit(player1.surface, (width/4, height/4))
display.blit(player2.surface, (.75*width, .75*height))

all_sprites = pygame.sprite.Group([player1, player2])



clock = pygame.time.Clock()

open = True
while open:
    for event in pygame.event.get():
        if pygame.key.get_pressed()[K_ESCAPE]:
            open = False
        elif event.type == QUIT:
            open = False

    pressed = pygame.key.get_pressed()

    all_sprites.update(pressed)

    display.blit(player1.surface, player1.rect)
    display.blit(player2.surface, player2.rect)

    pygame.display.flip()

    clock.tick(30)

    if pressed[K_p]:
        display.fill((0, 5, 50))
        pygame.draw.circle(display, (0, 0, 255), (250, 250), 75)
