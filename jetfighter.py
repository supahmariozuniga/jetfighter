import pygame
from pygame.locals import *
pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

red = (100, 100, 100)

display = pygame.display.set_mode((500, 500))
display.fill(red)
pygame.display.set_caption("hello")


class player(pygame.sprite.Sprite):
    lives = 5

    def __init__(self, left, right, img):
        super(player, self).__init__()
        self.image = pygame.image.load(img)
        self.surface = pygame.Surface((26, 26))
        self.rect = self.surface.get_rect()
        self.left = left
        self.right = right

    # def update(self):
    #     if pressed[self.left]:
    #         self.rect.move_ip(-5, 0)
    #     if pressed[self.right]:
    #         self.rect.move_ip(5, 0)



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

    display.blit(player1.surface, player1.rect)
    display.blit(player2.surface, player2.rect)

    pygame.display.flip()


    if pygame.key.get_pressed()[K_UP]:
        display.fill((50, 0, 0))
        pygame.draw.circle(display, (0, 0, 255), (250, 250), 75)
    # for event in pygame.event.get():
    #     if event.type == QUIT:
    #         pygame.quit()
    #         sys.exit()
