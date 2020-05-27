import pygame   # 13/4/2019: change buttton function a little bit

pygame.init()

# screen definition
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

white = (255, 255, 255)
black = (0, 0, 0)
grey = (50, 50, 50)
bright_blue = (0, 0, 255)
bright_red = (255, 0, 0)
yellow = (255, 255, 0)
gold = (255, 223, 0)


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
background = pygame.image.load('picture/background/menu_background.png')

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


def game_menu():
    # Title
    game_title, game_title_rect = text_object('Turtle race', title_font, black)
    game_title_rect.bottomright = (750, 200)
    game_title_back_rect = pygame.Rect((0, 0), (207, 55))
    game_title_back_rect.bottomright = (750, 200)

    button_x = 600
    button_y = 250
    button_width = 150
    button_height = 40
    # Button attributes
    button_color = black
    highlight_button_color = grey
    # Because break is used, there's no need to use a bool variable
    while True:
        run = 0
        display_surface.blit(background, (0, 0))

        display_surface.blit(game_title, game_title_rect)

        # Need constant checking to avoid relapses and run keep on being 0
        run = button('Play game', button_x, button_y, button_width, button_height, black, grey, START_GAME)
        if run != 0:
            break
        run = button('Settings', button_x, button_y + 50, button_width, button_height, black, grey, SETTING)
        if run != 0:
            break
        run = button('History', button_x, button_y + 100, button_width, button_height, black, grey, HISTORY)
        if run != 0:
            break
        run = button('Help', button_x, button_y + 150, button_width, button_height, black, grey, HELP)
        if run != 0:
            break
        run = button('About', button_x, button_y + 200, button_width, button_height, black, grey, ABOUT)
        if run != 0:
            break
        run = button('Exit', button_x, button_y + 250, button_width, button_height, black, grey, EXIT)
        if run != 0:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

    return run


def settings_menu():

    button_x = 600
    button_y = 250
    button_width = 170
    button_height = 40
    # Button attributes
    inactive_color = black
    active_button_color = grey
    # Because break is used, there's no need to use a bool variable
    while True:

        run = 0
        display_surface.blit(background, (0, 0))


        # Need constant checking to avoid relapses and run keep on being 0
        run = button('Racers', button_x, button_y, button_width, button_height, inactive_color, active_button_color, RACERS)
        if run != 0:
            break
        run = button('Road Length', button_x, button_y + 50, button_width, button_height, inactive_color, active_button_color, ROAD_LENGTH)
        if run != 0:
            break
        run = button('Background', button_x, button_y + 100, button_width, button_height, inactive_color, active_button_color, BACKGROUND)
        if run != 0:
            break
        run = button('Resolution', button_x, button_y + 150, button_width, button_height, inactive_color, active_button_color, SCREEN_RESOLUTION)
        if run != 0:
            break
        run = button('Back', button_x, button_y + 200, button_width, button_height, inactive_color, active_button_color, BACK)
        if run != 0:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

    return run

# #### main:
#
# def main():
#
#     call_function = MAIN_MENU
#     while True:
#         if call_function == MAIN_MENU:
#             call_function = game_menu()
#         if call_function == SETTING:
#             call_function = settings_menu()
#         if call_function == EXIT:
#             exitgame()
#
#
# if __name__ == "__main__":
#     main()
#     pygame.QUIT()
#     quit()
