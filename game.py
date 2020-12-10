import pygame, math, random
from pygame.locals import *
pygame.init()
vec = pygame.math.Vector2


height = 500
width = 500
display = pygame.display.set_mode((height, width))
display.blit(pygame.image.load("space.png"),(0, 0))
pygame.display.set_caption("UFO Fighters")


class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, x, y, image):
        super(Bullet, self).__init__()
        self.image = image
        self.surface = pygame.image.load(image).convert_alpha()
        self.rect = self.surface.get_rect()
        self.speed = vec(speed[0]*1.5, speed[1]*1.5)
        self.rect.x = x + 10*self.speed[0]
        self.rect.y = y + 10*self.speed[1]

    def update(self):
        self.rect.move_ip(self.speed)
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.left < 0:
            self.kill()
            if self.image == "bullet1.png":
                del player1.bullets[-1]
            else:
                del player2.bullets[-1]
        if self.rect.right > width:
            self.kill()
            if self.image == "bullet1.png":
                del player1.bullets[-1]
            else:
                del player2.bullets[-1]
        if self.rect.bottom > height:
            self.kill()
            if self.image == "bullet1.png":
                del player1.bullets[-1]
            else:
                del player2.bullets[-1]
        if self.rect.top < 0:
            self.kill()
            if self.image == "bullet1.png":
                del player1.bullets[-1]
            else:
                del player2.bullets[-1]
        if pygame.sprite.spritecollide(self, players, False):
            self.kill()
            if self.image == "bullet1.png":
                del player1.bullets[-1]
            else:
                del player2.bullets[-1]



class Player(pygame.sprite.Sprite):
    lives = 5
    cooldown = 1000

    def __init__(self, left, right, img, shoot, x, y, speed, bullet):
        super(Player, self).__init__()
        self.image = img
        self.surface = pygame.image.load(self.image).convert_alpha()
        self.rect = self.surface.get_rect()
        self.left = left
        self.right = right
        self.shoot = shoot
        self.speed = vec(0, speed)
        self.rect.x = x
        self.rect.y = y
        self.bullet_image = bullet


    def update(self, function):
        self.rect.move_ip(self.speed)
        if function[self.left]:
            self.speed = self.speed.rotate(-15)
        if function[self.right]:
            self.speed = self.speed.rotate(15)

        if function[self.shoot]:
            if self.bullets != "<Group(0 sprites)>":
                bullet = Bullet(self.speed, self.rect.x, self.rect.y, self.bullet_image)
                self.bullets.append(bullet)
                bullets.add(bullet)
                # self.cooldown = pygame.time.get_ticks()


        if pygame.sprite.spritecollide(self, bullets, False):
            self.lives -= 1

        if pygame.sprite.spritecollide(self, powerups, False):
            if self.lives < 10:
                self.lives += 1

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]


class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        super(Powerup, self).__init__()
        self.surface = pygame.image.load("heart.png").convert_alpha()
        self.rect = self.surface.get_rect()
        # self.position = random.choice(spawns)
        # self.rect.x = self.position[0]
        # self.rect.y = self.position[1]
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self):
        if pygame.sprite.spritecollide(self, players, False):
            self.kill()


display.blit(pygame.image.load("space.png"),(0, 0))

player1 = Player(K_LEFT, K_RIGHT, "ufo1.png", K_UP, 0, height, -3, "bullet1.png")
player2 = Player(K_a, K_d, "ufo2.png", K_w, width, 0, 3, "bullet2.png")

players = pygame.sprite.Group(player1, player2)
bullets = pygame.sprite.Group([])
powerups = pygame.sprite.Group([])
player1.bullets = []
player2.bullets = []



clock = pygame.time.Clock()
powerspawn = pygame.USEREVENT + 1
pygame.time.set_timer(powerspawn, 2000)


# def gameover_screen():


open = True
game_over = False
while open:
    clock.tick(30)

    for event in pygame.event.get():
        if pygame.key.get_pressed()[K_ESCAPE]:
            open = False
        elif event.type == QUIT:
            open = False

        elif event.type == powerspawn:
            powerup = Powerup()
            powerups.add(powerup)


    print(player2.lives)

    pressed = pygame.key.get_pressed()


    display.blit(pygame.image.load("space.png"),(0, 0))

    for sprite in players:
        sprite.update(pressed)
        display.blit(sprite.surface, [sprite.rect.x, sprite.rect.y])
        if sprite.lives < 1:
            sprite.kill()
            victory_lap = pygame.time.get_ticks()
            if victory_lap > 10000:
                open = False

    for sprite in powerups:
        sprite.update()
        display.blit(sprite.surface, [sprite.rect.x, sprite.rect.y])

    for sprite in player1.bullets:
        sprite.update()
        display.blit(sprite.surface, [sprite.rect.x, sprite.rect.y])

    for sprite in player2.bullets:
        sprite.update()
        display.blit(sprite.surface, [sprite.rect.x, sprite.rect.y])



    pygame.display.flip()
