# return 200 for small-windowed, return 400 for big-fullscreen
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.init()

SIZE = 200 #small-windowed
chosen_size = 0
pygame.display.set_caption("Turtle Race")
background = pygame.image.load("picture/background/menu_backgroundsettings.png")
button_text_font = pygame.font.SysFont('comicsansms', int(SCREEN_WIDTH/80*3))
white = (255, 255, 255)
black = (0, 0, 0)
grey = (50, 50, 50)
lightgrey = [(169,169,169),(169,169,169)]

def text_object(text, font, text_color):
    text_surface = font.render(text, True, text_color)
    return text_surface, text_surface.get_rect()
def message_display(win,text, text_x, text_y, text_color):
    TextSurf, TextRect = text_object(text, pygame.font.SysFont('comicsansms', 40), text_color)
    TextRect.center = (text_x, text_y)
    win.blit(TextSurf, TextRect)

def button(win, text,x, y, width, height, color, highlight_color, function = None):
    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(win, highlight_color, (x, y, width, height))
    else:
        pygame.draw.rect(win, color, (x, y, width, height))

    textSurf, textRect = text_object(text, button_text_font, white)
    textRect.center = (x + (width / 2), y + (height / 2))

    win.blit(textSurf, textRect)

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        if clicked[0] == 1 and function != None:
            function()
            return True
def set_small_size():
    global chosen_size
    global lightgrey
    lightgrey[0]=grey
    lightgrey[1]=(169,169,169)
    chosen_size = 200 #small-windowed
def set_big_size():
    global  chosen_size
    global lightgrey
    lightgrey[0] = (169, 169, 169)
    lightgrey[1] = grey
    chosen_size = 400 #big-fullsreen
def Back():
    return
def main_set_screen_size(win):

    global f_size
    global SIZE
    f_size= SIZE

    global lightgrey
    b_size = False
    b_ok = False
    b_back = False
    run =True
    while run:
        win.blit(background, (0, 0))
        message_display(win,"SETTING DISPLAY",SCREEN_WIDTH/2,SCREEN_HEIGHT/6,white)
        b_size = button(win,"SMALL-WINDOWED",SCREEN_WIDTH/32,SCREEN_HEIGHT/12*5,SCREEN_WIDTH/16*7,SCREEN_HEIGHT/6,lightgrey[0],grey,set_small_size)
        if b_size:
            SIZE = chosen_size
        b_size = button(win,"BIG-FULLSCREEN",SCREEN_WIDTH/32*17,SCREEN_HEIGHT/12*5,SCREEN_WIDTH/16*7,SCREEN_HEIGHT/6,lightgrey[1],grey,set_big_size)
        if b_size:
            SIZE = chosen_size
        b_back = button(win,"BACK", SCREEN_WIDTH/2 + 2, SCREEN_HEIGHT/13*11, SCREEN_WIDTH/16*3, SCREEN_HEIGHT/13, black, grey, Back)
        b_ok = button(win,"OK",SCREEN_WIDTH/16*5 - 2,SCREEN_HEIGHT/13*11, SCREEN_WIDTH/16*3,SCREEN_HEIGHT/13, black, grey, Back)
        if b_back:
            return f_size #return the previous value if user hit "BACK" button

        if b_ok:
            return SIZE   #return the new value if user hit "OK" button
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
        pygame.display.update()


