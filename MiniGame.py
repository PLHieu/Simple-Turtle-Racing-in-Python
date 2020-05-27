import pygame
import random
import time
import cmath

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RED = (255, 0, 0)
GRAY = (155, 155, 155)
WHITE = (255, 255, 255)

pygame.init()
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Turtle Race")
background = pygame.image.load("picture/minigame/minigame-background.png")


class player:
    posx = 0
    posy = 0
    width = 50
    height = 50
    interf = pygame.image.load("picture/minigame/player2.png")

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def DisplayPlayer(self, window, posx, posy):
        window.blit(self.interf, (posx, posy))


def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()


def message(text, rect_x, rect_y, size, choice):
    largeText = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = text_objects(text, largeText)
    if choice == 1:
        TextRect.center = (rect_x, rect_y)
    else:
        TextRect.midleft = (rect_x, rect_y)
    win.blit(TextSurf, TextRect)


def gameOver():
    message("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 115, 1)
    pygame.display.update()
    time.sleep(2)


def gameWin():
    message("You Win", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 115, 1)
    pygame.display.update()
    time.sleep(2)


def Point(point):
    message("Point: " + str(point), 0, 20, 30, 2)


class Falling_things:
    posx = 0
    posy = 0
    width = 0
    speed = 1
    height = 0
    interf = pygame.image.load("picture/minigame/rotationY1_1.png")

    def __init__(self, posx, posy, speed_extra, width, height):
        self.posx = posx
        self.posy = posy
        # speed_extra la toc do tang them
        self.speed = 1 + speed_extra
        self.width = width
        self.height = height

    def DisplayThing(self, window, posx, posy):
        window.blit(self.interf, (posx, posy))


crash = False
minigame_music = "sounds/hit_it.mp3"

def game_loop():
    # Sound
    pygame.mixer.music.stop()
    pygame.mixer.music.load(minigame_music)
    pygame.mixer.music.play(-1)
    # Logic
    NUMBER = 151
    x = SCREEN_WIDTH / 2 - player.width
    y = SCREEN_HEIGHT - player.height - 10
    things = []
    thing_startx = []
    thing_starty = []
    thing_speed_ex = []
    vector = 0
    # for i in range(0,NUMBER):
    #        thing_startx.append(random.randrange(0,SCREEN_WIDTH))
    #        thing_starty.append(random.randrange(-1000,0))
    thing_width = 15
    thing_height = 8
    point = 0
    Player = player(x, y)
    x_change = 0
    for i in range(0, NUMBER):
        thing_startx.append(random.randrange(0, SCREEN_WIDTH))
        thing_starty.append(random.randrange(-2000, 0))
        thing_speed_ex.append(random.randrange(1, 5))
        things.append(
            Falling_things(thing_startx[i], thing_starty[i], thing_speed_ex[i] * 0.2, thing_width, thing_height))
    for i in range(0, int(NUMBER / 2)):
        thing_startx.remove(thing_startx[i])
        thing_starty.remove(thing_starty[i])
        thing_speed_ex.remove(thing_speed_ex[i])
    while not crash:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -2
                if event.key == pygame.K_RIGHT:
                    x_change = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        # win.fill(GRAY)
        win.blit(background, (0, 0))
        Player.DisplayPlayer(win, x, y)

        for i in range(0, NUMBER):
            things[i].DisplayThing(win, things[i].posx, things[i].posy)

            if things[i].posx + things[i].width >= x and things[i].posx <= x + Player.width:
                if (things[i].posy >= y - things[i].height and things[i].posy <= y + Player.height - 10):
                    gameOver()
                    return point

            if things[i].posy > SCREEN_HEIGHT:
                point += 1
                things[i] = things[NUMBER - 1]
                things[i].speed = 0
            things[i].posy += things[i].speed

        Point(point)

        if (x > SCREEN_WIDTH - 68 or x < 12):
            gameOver()
            return point
        if (point == 150):
            gameWin()
            return point
        pygame.display.update()


