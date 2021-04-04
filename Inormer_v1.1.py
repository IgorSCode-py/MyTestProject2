import pygame
import random
import os
icon = pygame.image.load("ggg.png")
pygame.display.set_icon(icon)
WIDTH = 800
HEIGHT = 600
FPS = 3000000000000000000
# ----------------------
# game_f = os.path.dirname(__file__)
# img_f = os.path.join(game_f, 'img')
# player_img = pygame.image.load(os.path.join(img_f, 'Kek2.png'))
player_img = pygame.image.load("Kek2.png")
#IMGHIGHT = pygame.image.
player_back = pygame.image.load("Kek2 left.png")
background = pygame.image.load("228.jpg")
platform_img = pygame.image.load("lol.png")
boards = []
# ----------------------
# Задаём цвета
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
# ----------------------
class Platforms(pygame.sprite.Sprite):
    speedx = 0.3

    def __init__(self, top, speedx):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((32,32))
        # self.image.fill(GREEN)
        self.image = platform_img
        # self.back = player_back
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.y = HEIGHT - top
        self.speedx = speedx
        self.y = HEIGHT - top

    def update(self):
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speedx = 0 - self.speedx
        #print(1)
        self.rect.x += self.speedx
        #print('plat')
        #print(self.rect.y)
        #print(self.rect.x)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((32,32))
        #self.image.fill(GREEN)
        self.image = player_img
        # self.back = player_back
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.rect.y = HEIGHT - 50
        self.speedx = 0
        self.speedy = 1
        self.is_jumping = False
        self.is_falling = False
        self.is_onBoard = False
        self.the_board = ''
        self.t = 0
        self.y = self.rect.y
        #self.hight = self.image.get_height()

    def update(self):
        self.speedx = 0
        key_s = pygame.key.get_pressed()

        if key_s[pygame.K_LEFT]:
            self.speedx = -1
            self.image = player_back

        if key_s[pygame.K_RIGHT]:
            self.image = player_img
            self.speedx = 1

        if key_s[pygame.K_UP] and (self.rect.bottom == HEIGHT or self.is_onBoard):
            self.is_jumping = True
            self.t = 0
 #           if self.is_jumping:
 #               self.is_jumping = False

        if self.is_onBoard:
            #print("Не упал ли?")
            #print(self.rect.right)
            #print(self.the_board.rect.right)
            if (self.rect.right < self.the_board.rect.left) or (self.rect.left > self.the_board.rect.right):
                self.is_falling = True
                self.is_onBoard = False
                self.t = 0
                self.speedx = 0

        if self.is_jumping:
            #print("jump")
            self.t = self.t + 1
            delta = (1.4 - 0.0001 * self.t * self.t / 2)
            if delta <= 0:
                self.is_falling = True
                self.is_jumping = False
                self.t = 0
            else:
                self.y = self.y - delta
                self.rect.y = self.y

        if self.is_falling:
            print("fall")
            self.t = self.t + 1
            self.y = self.y + (0 + 0.0001 * self.t * self.t / 2)
            self.rect.y = self.y
            print(self.y)
            if self.rect.bottom >= HEIGHT:
                self.is_jumping = False
                self.is_falling = False
                self.y = HEIGHT - self.image.get_height()
                self.rect.y = self.y
            for board in boards:
                #print(board.rect.y)
                #print(self.rect.y)
                if (board.rect.y - self.rect.height + 1 >= self.rect.y >= board.rect.y - self.rect.height):
                    #print(board)
                    #print(board.rect.right)
                    if (self.rect.right >= board.rect.left) and (self.rect.left <= board.rect.right):
                        print(board)
                        self.is_jumping = False
                        self.is_falling = False
                        self.y = board.rect.y - self.rect.height
                        self.rect.y = self.y
                        self.is_onBoard = True
                        self.the_board = board
                        self.speedx = board.speedx


                #a=1
                #self.rect.y = board.rect. - 50:
                #self.is_jumping = False
                #self.rect.y = HEIGHT - self.rect.height
        #if self.rect.y <= 0 or self.rect.y >= HEIGHT - self.hight:
        #        self.speedy = 0 - self.speedy


        # if self.rect.bottom >= HEIGHT:
        #     self.rect.y = 0
        # self.rect.y += self.speedy

        #if self.is_falling:
        #    self.t = self.t + 1
        #    self.rect.y = self.rect.y + (0 + (0.0001 * self.t ** 2) / 2)
        #    if self.rect.y == HEIGHT - self.rect.height:
        #        self.is_falling = False
                #picy = h

        # self.rect.x += 3
        if self.rect.right > WIDTH:

            self.rect.right = WIDTH -1
        if self.rect.left < 0:
            self.rect.left = 1


        if self.is_onBoard:
            self.rect.x = self.rect.x + self.speedx + self.the_board.speedx
        else:
            self.rect.x += self.speedx
        # self.rect.y += self.speedy
        #print('man')
        #print(self.rect.x)

# ----------------------
pygame.init()
pygame.mixer.init()
# ----------------------
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Inormer")
clock = pygame.time.Clock()
sprites = pygame.sprite.Group()

player = Player()
sprites.add(player)

#plats = pygame.sprite.Group()
for i in range(5):
    platform = Platforms(100*i, i/2)
    boards.append(platform)
    sprites.add(platform)
    #plats.add(platform)

# ----------------------
# Цикл игры
running = True
while running:
    # clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
    sprites.update()
    #plats.update()
    screen.blit(background, [0,0])
    sprites.draw(screen)
    #plats.draw(screen)
    pygame.display.flip()
# ----------------------

pygame.quit()