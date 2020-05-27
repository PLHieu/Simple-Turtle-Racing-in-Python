import pygame   # 13/4/2019: change buttton function a little bit

pygame.init()

# screen definition
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

white = (255, 255, 255)
black = (0, 0, 0)
grey = (50, 50, 50)
silver = (192, 192, 192)
bright_blue = (0, 0, 255)
bright_red = (255, 0, 0)
yellow = (255, 255, 0)
gold = (255, 223, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)


display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Turtle Race")


# Function definition
MAIN_MENU = 555
START_GAME = 999
SETTING = 768
HISTORY = -999
HELP = 101
ABOUT = 113

RACERS = 420
BACKGROUND = 304
ROAD_LENGTH = 911
SCREEN_RESOLUTION = 4000
BACK = 555
EXIT = 115

# font
button_text_font = pygame.font.Font('font/Sheeping Cats.otf', 20)
title_font = pygame.font.SysFont('arial', 50, True)

# background
background = pygame.image.load('picture/background/menu_backgroundsettings.png')

def text_object(text, font, text_color):
    text_surface = font.render(text, True, text_color)
    return text_surface, text_surface.get_rect()


def exitgame():
    pygame.quit()
    quit()


def button(text , x, y, width, height, color, highlight_color, function = None):
    mouse = pygame.mouse.get_pos()
    output_number = 0

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(display_surface, highlight_color, (x, y, width, height))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                output_number = function
    else:

        pygame.draw.rect(display_surface, color, (x, y, width, height))

    textSurf, textRect = text_object(text, button_text_font, white)
    textRect.center = (x + (width / 2), y + (height / 2))
    display_surface.blit(textSurf, textRect)
    return output_number

def arrow_button(x, y, width, height, color, highlight_color, direction):
    mouse = pygame.mouse.get_pos()
    output_number = False

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(display_surface, highlight_color, (x, y, width, height))
        if direction == 'LEFT':
            pygame.draw.polygon(display_surface, silver, [[x + 5, y + (height / 2)], [x + width, y + height], [x + width, y]])
        else:
            pygame.draw.polygon(display_surface, silver, [[x + width - 5, y + (height / 2)], [x, y + height], [x, y]])

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                output_number = True

    else:
        pygame.draw.rect(display_surface, color, (x, y, width, height))
        if direction == 'LEFT':
            pygame.draw.polygon(display_surface, white, [[x + 5, y + (height / 2)], [x + width, y + height], [x + width, y]])
        else:
            pygame.draw.polygon(display_surface, white, [[x + width - 5, y + (height / 2)], [x, y + height], [x, y]])

    return output_number


def map_menu():

    button_x = 320
    button_y = 500
    button_width = 170
    button_height = 40

    arrow_button_left_x = SCREEN_WIDTH * 0.01
    arrow_button_left_y = SCREEN_HEIGHT * 0.4

    arrow_button_right_x = SCREEN_WIDTH * 0.9
    arrow_button_right_y = SCREEN_HEIGHT * 0.4

    arrow_button_width = 70
    arrow_button_height = 70

    # Button attributes
    inactive_color = black
    active_button_color = grey

    # load the map
    map_1 = pygame.image.load('picture/minimapforselectingmap/map-1.png').convert_alpha()
    map_2 = pygame.image.load('picture/minimapforselectingmap/map-2.png').convert_alpha()
    map_3 = pygame.image.load('picture/minimapforselectingmap/map-3.png').convert_alpha()

    # toa do khi ve map
    map_blit_x = 100
    map_blit_y = 30

    # i la so thu tu cua map trong map_list
    i = 0
    map_list = [map_1, map_2, map_3]
    next_map = 0
    previous_map = 0

    while True:

        run = 0
        display_surface.blit(background, (0, 0))

       #def arrow_button(x, y, width, height, color, highlight_color, direction)
        previous_map = arrow_button(arrow_button_left_x,arrow_button_left_y, arrow_button_width, arrow_button_height, inactive_color, active_button_color, 'LEFT')
        next_map = arrow_button(arrow_button_right_x, arrow_button_right_y, arrow_button_width, arrow_button_height, inactive_color,active_button_color, 'RIGHT')

        if next_map == True:
            i += 1
        if previous_map == True:
            i -= 1

        # reset i
        if i >= 3:
            i = 0
        if i < 0:
            i = 2

        display_surface.blit(map_list[i], (map_blit_x, map_blit_y))

        run = button('OK', button_x, button_y, button_width, button_height, inactive_color, active_button_color, SETTING)
        if run != 0:
            # khi click OK, choosen_map se luu so thu tu cua map
            choosen_map = i
            return  choosen_map

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

#
#
# map_menu()
# pygame.quit()
# quit()