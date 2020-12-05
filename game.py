import pygame, math, random
from pygame.locals import *
pygame.init()

vec = pygame.math.Vector2

height = 500
width = 500
display = pygame.display.set_mode((height, width))
display.blit(pygame.image.load("space.png"),(0, 0))
pygame.display.set_caption("hello")

class Bullet(pygame.sprite.Sprite):
    # self.surface = pygame.img.load(img).convert_alpha()
    # self.rect = self.surface.get_rect()

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
    speed = 150
    rot_speed = 360

    def __init__(self, left, right, img, shoot, speed):
        super(Player, self).__init__()
        self.image = img
        self.surface = pygame.image.load(img).convert_alpha()
        self.rect = self.surface.get_rect()
        self.left = left
        self.right = right
        self.shoot = shoot
        self.speed = vec(0, speed)


    def update(self, function):
        self.rect.move_ip(self.speed)
        if function[self.left]:
            self.speed = self.speed.rotate(-15)
        if function[self.right]:
            self.speed = self.speed.rotate(15)
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


spawns = [[width/4, height/4], [width/2, height/2], [.75*width, .75*height], [width/4, .75*height], [.75*width, height/4]]
class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        super(Powerup, self).__init__()
        self.surface = pygame.image.load("heart.png").convert_alpha()
        self.rect = self.surface.get_rect()

    def update(self):
        if pygame.sprite.spritecollide(self, Player, False):
            self.kill()



display.blit(pygame.image.load("space.png"),(0, 0))


player1 = Player(K_LEFT, K_RIGHT, "jet1.png", K_g, 5)
player2 = Player(K_a, K_d, "jet2.png", K_m, 5)

player_sprites = pygame.sprite.Group(player1, player2)
all_sprites = pygame.sprite.Group(player1, player2)



clock = pygame.time.Clock()
powerspawn = pygame.USEREVENT + 1
pygame.time.set_timer(powerspawn, 2000)

open = True
while open:
    for event in pygame.event.get():
        if pygame.key.get_pressed()[K_ESCAPE]:
            open = False
        elif event.type == QUIT:
            open = False

        elif event.type == powerspawn:
            powerup = Powerup()
            display.blit(powerup.surface, random.choice(spawns))
            all_sprites.add(powerup)




    pressed = pygame.key.get_pressed()

    player_sprites.update(pressed)

    display.blit(pygame.image.load("space.png"),(0, 0))

    for sprite in all_sprites:
        display.blit(sprite.surface, sprite.rect)


    pygame.display.flip()

    clock.tick(30)
    #
    # if pygame.sprite.spritecollide(player1, Powerup, False):
    #     player1.lives += 1
    #
    # if pygame.sprite.spritecollide(player1, Player, False):
    #     player1.lives = player1.lives - 1
    #     player2.lives = player2.lives - 1
    #
    # if pygame.sprite.spritecollideany(player1, Bullet):
    #     player1.lives = player1.lives - 1
