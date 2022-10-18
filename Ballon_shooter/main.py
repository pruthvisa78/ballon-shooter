# Importing Package
import pygame

from pygame import mixer

pygame.init()

# Icon and Title
icon = pygame.image.load('balloon1.png')
pygame.display.set_caption("Balloon Shooter")
pygame.display.set_icon(icon)
# img loading
background = pygame.image.load('game.png')
gun = pygame.image.load('gun1.png')
bullet = pygame.image.load('bullet1.png')
balloon = pygame.image.load('balloon2.png')
balloon1 = pygame.image.load('balloon3.png')
ballon2 = pygame.image.load('balloon4.png')
ballon3 = pygame.image.load('balloon5.png')
ballon4 = pygame.image.load('balloon6.png')
# sound loading
mixer.music.load('Balloon Fight.wav')
mixer.music.play(-1)

# functions
gunX = 3
gunY = 220
gunY_c = 0
gunX_c = 0


def gunImg(x, y):
    screen.blit(gun, (x, y))


import random

balloons = [balloon, balloon1, ballon2, ballon3, ballon4]
balloonX = []
balloonY = []
for i in range(len(balloons)):
    balloonX.append(random.randint(135, 736))
    balloonY.append(random.randint(610, 620))

balloonY_c = -0.6


def balloonImg(x, y):
    screen.blit(balloon, (x, y))


bulletX = 100
bulletY = gunY + 38
bulletX_c = 8
bullet_state = "ready"


def bulletImg(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x, y))


import math


def burst(a, b, c, d):
    r = math.sqrt((a - c) ** 2 + (b - d) ** 2)
    if r < 20:
        return True
    else:
        return False


# score
scorev = 0
font = pygame.font.SysFont('comicsansms', 32)
textX = 633
textY = 0


def sscore(x, y):
    score = font.render("Score:" + str(scorev), True, (255, 100, 80))
    screen.blit(score, (x, y))


# Game over
gfont = pygame.font.SysFont('comicsansms', 64)

rfont = pygame.font.SysFont('comicsansms', 32)


def game_over_text():
    Gameover = True
    while Gameover:
        Gameo = gfont.render("Game Over", True, (255, 255, 100))
        rs = rfont.render("Click R to Restart ", True, (0, 0, 0))
        
        screen.blit(rs, (290, 295))

        screen.blit(Gameo, (255, 230))
        sscore(textX, textY)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:

                    for i in range(len(balloons)):
                        balloonY[i] = 640
                    Gameover = False


pfont = pygame.font.SysFont('comicsansms', 64)
mfont = pygame.font.SysFont('Comicsansms', 32)


def Pstext():
    Ps = pfont.render("Paused", True, (0, 0, 0))
    Ms = mfont.render("Click C to continue", True, (255, 255, 255))
    screen.blit(Ps, (300, 230))
    screen.blit(Ms, (270, 295))


def Pause():
    Paused = True
    while Paused:
        Pstext()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    Paused = False
          


# Game Window
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gunY_c = -2.5
            if event.key == pygame.K_DOWN:
                gunY_c = 2.5
            if event.key == pygame.K_p:
                Pause()
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('M416.wav')
                    bullet_sound.play()
                    bulletY = gunY + 38
                    bulletImg(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                gunY_c = 0
            if event.key == pygame.K_DOWN:
                gunY_c = 0

    if bulletX >= 832:
        bulletX = 100
        bullet_state = 'ready'

    if bullet_state == "fire":
        bulletImg(bulletX, bulletY)
        bulletX += bulletX_c
    gunX += gunX_c
    gunY += gunY_c
    if gunY <= -30:
        gunY = -30
    if gunY >= 445:
        gunY = 445
    gunImg(gunX, gunY)
    for i in range(len(balloons)):
        # Game Over
        if balloonY[i] <= -40:
            for j in range(len(balloons)):
                balloonY[i] = 640
            game_over_text()
            scorev = 0

        balloonY[i] += balloonY_c
        screen.blit(balloons[i], (balloonX[i], balloonY[i]))
        bursted = burst(bulletX, bulletY, balloonX[i], balloonY[i])
        if bursted:
            bst = mixer.Sound('Balloon Popping.wav')
            bst.play()
            bulletX = 100
            bullet_state = "ready"
            scorev += 1
            balloonX[i] = random.randint(135, 736)
            balloonY[i] = random.randint(610, 620)
    sscore(textX, textY)
    pygame.display.update()
