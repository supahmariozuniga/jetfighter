import pygame, math, random
from pygame.locals import *
pygame.init()


height = 500
width = 500
display = pygame.display.set_mode((height, width))
display.blit(pygame.image.load("space.png"),(0, 0))
pygame.display.set_caption("hello")

class Bullet(pygame.sprite.Sprite):
    self.surface = pygame.img.load(img).convert_alpha()
    self.rect = self.surface.get_rect()

    def __init__(self, speed):
        self.speed = speed

    def update(self):
        if self.rect.left < 0:
            self.kill()
        if self.rect.right > width:
            self.kill()
        if self.rect.top < 0:
            self.kill()
        if self.rect.bottom > height:
            self.kill()


class Player(pygame.sprite.Sprite):
    lives = 5
    speed = (5, 5)

    def __init__(self, left, right, img, shoot, up, down):
        super(Player, self).__init__()
        self.surface = pygame.image.load(img).convert_alpha()
        self.rect = self.surface.get_rect()
        self.left = left
        self.right = right
        self.shoot = shoot
        self.up = up
        self.down = down


    def update(self, function):
        # self.rect.move_ip(self.speed)
        if function[self.left]:
            # self.surface = pygame.transform.rotate(self.surface, .174)
            # self.rect = self.surface.get_rect()
            # self.speed = ((self.speed[0] * math.sin(.174)), (self.speed[1] * math.cos(.174)))

            self.rect.move_ip(-5, 0)
        if function[self.right]:
            # self.surface = pygame.transform.rotate(self.surface, -.174)
            # self.rect = self.surface.get_rect()
            # self.speed = ((self.speed[0] * math.sin(-.174)), (self.speed[1] * math.cos(-.174)))
            self.rect.move_ip(5,0)
        if function[self.up]:
            self.rect.move_ip(0, -5)
        if function[self.down]:
            self.rect.move_ip(0, 5)
        if function[self.shoot]:
            self.hold = "L"

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height


lifespawn = [(width/4, height/4), (width/2, height/2), (.75*width, .75*height), (width/4, .75*height), (.75*width, height/4)]
class Powerup(pygame.sprite.Sprite):
    hold = "L"

    def __init__(self, list):
        self.spawn = random.choice(list)
    # surface = pygame.image.load()










player1 = Player(K_LEFT, K_RIGHT, "jet1.png", K_g, K_UP, K_DOWN)
player2 = Player(K_a, K_d, "jet2.png", K_m, K_w, K_s)

display.blit(player1.surface, (width/4, height/4))
display.blit(player2.surface, (.75*width, .75*height))

all_sprites = pygame.sprite.Group([player1, player2])



clock = pygame.time.Clock()
powerspawn = pygame.USEREVENT + 1
pygame.time.set_timer(powerspawn, 30000)

open = True
while open:
    for event in pygame.event.get():
        if pygame.key.get_pressed()[K_ESCAPE]:
            open = False
        elif event.type == QUIT:
            open = False

        elif event.type == powerspawn:
            powerup = Powerup(lifespawn)
            all_sprites.add(powerup)



    pressed = pygame.key.get_pressed()

    all_sprites.update(pressed)

    display.blit(pygame.image.load("space.png"),(0, 0))
    display.blit(player1.surface, player1.rect)
    display.blit(player2.surface, player2.rect)

    pygame.display.flip()

    clock.tick(30)
    #
    if pygame.sprite.spritecollide(player1, Powerup, False):
        player1.lives += 1

    if pygame.sprite.spritecollide(player1, Player, False):
        player1.lives = player1.lives - 1
        player2.lives = player2.lives - 1

    if pygame.sprite.spritecollideany(player1, Bullet):
        player1.lives = player1.lives - 1

    if pressed[K_p]:
        display.fill((0, 5, 50))
        pygame.draw.circle(display, (0, 0, 255), (250, 250), 75)
        print(player2.speed)
