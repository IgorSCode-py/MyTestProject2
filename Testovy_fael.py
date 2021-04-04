import pygame

class FlyingObjects():
    x = 0
    y = 0
    speed = 0
    pic = ""

    def __init__(self, x, y, speed, pic):
        self.x = x
        self.y = y
        self.speed = speed
        self.pic = pic


    def moveHorizontal(self):
        return self.x + self.speed

class RunningMen(FlyingObjects):
    direction = ''

    isJumping = False
    isFalling = False
    isOnBoard = False

    def __init__(self, picForward, picBack):
        self.pic = picForward
        self.picForward = picForward
        self.picBack = picBack


    def Jump(self):
        a = 1


def nextStep():

    return

pygame.init()
screen = pygame.display.set_mode([700,700])
# Задать цвет фону
# bg = (113,188,120)



pic = pygame.image.load("Kek2 left.png")
picback = pygame.image.load("Kek2.png")
picplat = pygame.image.load("plat.png")
piclol = pygame.image.load("lol.png")


#picshow = pic


forward = True


picy = 550
picx = 700 - pic.get_height()
lolx = 500
loly = 515
platx = 400
platy = 410

colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picback.set_colorkey(colorkey)

keep_going = True

BLACK = (0,0,0)
timer = pygame.time.Clock()
speedx = 0.5
speedy = 0.5

speedbordy = 0.2
speedbordx = 0.2

startjump = False
fallDown = False
onBoard = False

h = picy
t = 0

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[pygame.K_UP] and not startjump:
        print("jump!")
        startjump = True
        h = picy
        t = 0

    if pressedKeys[pygame.K_RIGHT]:
        speedx = -0.5
        forward = False

    if pressedKeys[pygame.K_LEFT]:
        speedx = 0.5
        forward = True

    if pressedKeys[pygame.K_SPACE]:
        speedx = 0

    if onBoard:
        speedx = speedx + speedbordx


    pygame.display.update()
    #picy = picy - speedy
    if startjump:
        t = t + 1
        picy = picy - (1 - (0.0001 * t * t) / 2)
        print(picy)
        if picy >= h:
            startjump = False
            picy = h
        if picy >= loly and lolx <= picx <= (lolx + piclol.get_width()):
            onBoard = True
            startjump = False
            picy = loly - pic.get_height()
            speedx = speedbordx

    if onBoard:
        #Проверим, не свалились ли
        if not (lolx <= picx <= (lolx + piclol.get_width())):
            fallDown = True
            onBoard = False
            t = 0

    if fallDown:
        t = t + 1
        picy = picy + (0 + (0.0001 * t * t) / 2)
        if picy >= h:
            fallDown = False
            picy = h

    picx = picx - speedx
    screen.fill(BLACK)

    if forward:
        screen.blit(pic,(picx,picy))
    else:
        screen.blit(picback, (picx, picy))

    screen.blit(picplat, (platx, platy))

    screen.blit(piclol, (lolx, loly))



    lolx = lolx - speedbordx


# Добавить передвижение перидвижной платформе и чтобы она могла перевозить персонажа по колёсику мыши.
    pygame.display.update()
    if picx <= 0 or picx >= 700 - pic.get_width():
        speedx = 0 - speedx
        forward = not forward
    if picy <= 0 or picy >= 700 - pic.get_height():
        speedy = 0 - speedy



    if lolx <= 0 or lolx >= 700 - piclol.get_width():
        speedbordx = 0 - speedbordx
    if loly <= 0 or loly >= 700 - piclol.get_height():
        speedbordy = 0 - speedbordy
pygame.quit()