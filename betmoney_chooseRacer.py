import pygame       # 20/4/2019: add minigame button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

white = (255, 255, 255)
black = (0, 0, 0)
grey = (50, 50, 50)
teal = (0, 255, 255)
bright_red = (255, 0, 0)
red = (220, 0, 0)
yellow = (255, 255, 0)
gold = (255, 223, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 200)
bright_blue = (0, 0, 255)

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
START_PLAYING_GAME = 482000

PASS_SPELL = 111333

MINIGAME_ASK = 77777333
MINIGAME = 73

# Choose main car definition
LINE_1 = 0
LINE_2 = 1
LINE_3 = 2
LINE_4 = 3
LINE_5 = 4


# font
button_text_font = pygame.font.Font('font/Sheeping Cats.otf', 20)
button_text_font_start_menu = pygame.font.Font('font/vorpalcond.ttf', 20)
car_name_font = pygame.font.Font('font/CALIBRIB.ttf', 20)
wallet_font = pygame.font.SysFont('arial', 36, True)
title_font = pygame.font.SysFont('arial', 50, True)
FONT = pygame.font.Font('font/DIN-Regular.ttf', 30)
# FONT: font of the text which is typing in the text box

background = pygame.image.load("picture/background/menu_backgroundsettings.png")

pygame.display.set_caption('Turtle Race')


# color for the text box
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

class Car:
    posx = 0
    posy = 0
    speed = 0.2
    isMain = False
    color = "NULL"
    road = 0
    list_bua = []
    def __init__(self, x_hoanhdo, y_tungdo, color, road):
        self.setpos((x_hoanhdo, y_tungdo))
        self.set_color(color)
        self.set_road(road)
        pass

    def setpos(self, pos):
        self.posx = pos[0]
        self.posy = pos[1]

    def set_x(self, x):
        self.posx = x
    def set_color(self,color):
        self.color = pygame.image.load(color)

    def set_road(self, road):
        self.road = road

    def drawCar(self, window):
        window.blit(self.color, (self.posx, self.posy))

class InputBox:

    def __init__(self, x, y, w, h, text = ''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        # self.text will be the text display when user type in
        self.storedValue = text
        # self.storedValue is the variable stored the text( or value) after the user press Enter
        self.txt_surface = FONT.render(text, True, black)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            if self.active == True:
                self.color = COLOR_ACTIVE
            else:
                self.color = COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.storedValue = self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.txt_surface.get_width() < self.rect.w - 20:
                    self.text += event.unicode
                else:
                    pass
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, black)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y ))

def text_object(text, font, text_color):
    text_surface = font.render(text, True, text_color)
    return text_surface, text_surface.get_rect()


def isNumber(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def exitgame():
    pygame.quit()
    quit()


def message_display(text, text_x, text_y, font, font_size, text_color):
    TextSurf, TextRect = text_object(text, pygame.font.Font(font, font_size), text_color)
    TextRect.center = (text_x, text_y)
    display_surface.blit(TextSurf, TextRect)

def wallet_box(text, x, y, width, height):
    pygame.draw.rect(display_surface, black, (x, y, width, height))
    pygame.draw.rect(display_surface, white, (x + 5, y + 5, width - 10, height - 10), 3)
    TextSurf, TextRect = text_object(text, wallet_font, white)
    TextRect.midright = (x + width - 50, y + (height / 2))
    display_surface.blit(TextSurf, TextRect)

    message_display('G', x + width - 25, y + (height / 2) + 2, 'font/CALIBRIB.ttf', 36, gold)
    message_display('Wallet', x + 42, y - 15, 'font/CALIBRIB.ttf', 30, teal)

def button_start_menu(text , x, y, width, height, color, highlight_color, function = None, car_img = None, car_name = None):
    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()
    output_number = None

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(display_surface, highlight_color, (x, y, width, height))

        if clicked[0] == 1 and function != None:
            output_number = function

    else:
        pygame.draw.rect(display_surface, color, (x, y, width, height))

    textSurf, textRect = text_object(text, button_text_font_start_menu, white)
    textRect.center = (x + (width / 2), y + (height - 20))
    display_surface.blit(textSurf, textRect)

    if car_img != None:
        imgSurface = car_img.get_rect()
        imgSurface.center = (x + (width / 2), y + (height / 2))
        display_surface.blit(car_img, imgSurface)

    if car_name != None:
        car_name_textSurf, car_name_textRect = text_object(car_name, car_name_font, white)
        car_name_textRect.center = (x + (width / 2), y + (height * 0.2))
        display_surface.blit(car_name_textSurf, car_name_textRect)


    return output_number

def button(text , x, y, width, height, color, highlight_color, function = None, ts1 = None):
    mouse = pygame.mouse.get_pos()
    output_number = 0

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(display_surface, highlight_color, (x, y, width, height))
        if function != None:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # event.button == 1 is left click checked
                    output_number = function

    else:
        pygame.draw.rect(display_surface, color, (x, y, width, height))

    textSurf, textRect = text_object(text, button_text_font, white)
    textRect.center = (x + (width / 2), y + (height / 2))
    display_surface.blit(textSurf, textRect)
    return output_number


def pass_First_Spell_box(wallet_gold):
    passSpell_active = False

    box_x = SCREEN_WIDTH/2 - 150
    box_y = SCREEN_HEIGHT/2 - 70
    box_width = 300
    box_height = 150

    button_width = 70
    button_height = 40
    button_x = SCREEN_WIDTH / 2 - button_width - 15
    button_y = SCREEN_HEIGHT / 2 + 15

    # function when click yes or no
    YES = 11111111111111
    NO = 10101010101010

    while True:

        pygame.draw.rect(display_surface, black, (box_x, box_y, box_width, box_height))
        message_display('Do you want to pass the first spell', box_x + 150, box_y + 20, 'font/CALIBRIB.ttf', 20, white)
        message_display('Cost 1000 gold ', box_x + 150, box_y + 50, 'font/CALIBRIB.ttf', 20, white)

        run = button('YES', button_x, button_y, button_width, button_height, green, bright_green, YES)
        if run == YES:
            wallet_gold -= 1000
            passSpell_active = True
            return wallet_gold, passSpell_active
        run = button('NO', button_x + button_width + 30, button_y, button_width, button_height, red, bright_red, NO)
        if run == NO:
            return  wallet_gold, passSpell_active

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update(box_x, box_y, box_width, box_height)


def Minigame_ask_box():

    box_x = SCREEN_WIDTH/2 - 150
    box_y = SCREEN_HEIGHT/2 - 70
    box_width = 300
    box_height = 150

    button_width = 70
    button_height = 40
    button_x = SCREEN_WIDTH / 2 - button_width - 15
    button_y = SCREEN_HEIGHT / 2 + 15

    # function when click yes or no
    YES = 11111111111111
    NO = 10101010101010

    while True:

        pygame.draw.rect(display_surface, black, (box_x, box_y, box_width, box_height))
        message_display('Do you want to play minigame', box_x + 150, box_y + 20, 'font/CALIBRIB.ttf', 20, white)
        message_display('to gain gold', box_x + 150, box_y + 50, 'font/CALIBRIB.ttf', 20, white)

        run = button('YES', button_x, button_y, button_width, button_height, green, bright_green, YES)
        if run == YES:
            return MINIGAME
        run = button('NO', button_x + button_width + 30, button_y, button_width, button_height, red, bright_red, NO)
        if run == NO:
            return 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update(box_x, box_y, box_width, box_height)



def startgame(l, total_account, first_time_log_in, player_name, passSpell_active):


    #welcome back text attributes
    welcome_back_text_x = SCREEN_WIDTH / 2
    welcome_back_text_y = SCREEN_HEIGHT / 2 + 80
    welcome_back_text_display = False

    # button attributes
    button_x = 600
    button_y = 250
    button_width = 150
    button_height = 40
    button_color = black            # color when inactive
    highlight_button_color = grey   # color when active

    button_start_menu_x = 10
    button_start_menu_y = 50
    button_start_menu_width = 135
    button_start_menu_height = 150

    # coordinate of START
    start_button_x = 600
    start_button_y = 450

    # coordinate of PASS SPELL
    passSpell_button_x = 50
    passSpell_button_y = SCREEN_HEIGHT / 2 + 10
    passSpell_button_width = 200
    passSpell_button_height = 45

    # coordinate of Minigame button
    Minigame_button_x = 550
    Minigame_button_y = SCREEN_HEIGHT / 2 + 10
    Minigame_button_width = 200
    Minigame_button_height = 45

    # Wallet text box
    wallet_text_box_x = 50
    wallet_text_box_y = 490
    wallet_text_box_width = 200
    wallet_text_box_height = 50

    # Text input boxes
    gold_text_box_x = 50
    gold_text_box_y = 250
    name_text_box_x = 550
    name_text_box_y = 250
    text_box_width = 200
    text_box_height = 40

    gold_input_box = InputBox(gold_text_box_x, gold_text_box_y, text_box_width, text_box_height)
    name_input_box = InputBox(name_text_box_x, name_text_box_y, text_box_width, text_box_height, player_name)
    input_boxes = [gold_input_box, name_input_box]

    # List of car type, car color, car name, car face
    #l= ["SUPER", [101,108,106,107,102], ["Long Hieu","Khi dau cho","Hau cuzzz","Hao hao","Hien huynh"]]

    #car Image preparation
    car_1 = l[0] + str(l[1][0])
    car_2 = l[0] + str(l[1][1])
    car_3 = l[0] + str(l[1][2])
    car_4 = l[0] + str(l[1][3])
    car_5 = l[0] + str(l[1][4])

    # The + operator is used to concatenate 2 string into 1 string

    # car Image
    if(l[0] == 'PJTeam'):
        carImg_1 = pygame.image.load("picture/TurtleObject/" + l[0] + "/0" + str(l[1][0] - 101) + ".png")
        carImg_2 = pygame.image.load("picture/TurtleObject/" + l[0] +  "/1" + str(l[1][1] - 101)+ ".png")
        carImg_3 = pygame.image.load("picture/TurtleObject/" + l[0] +  "/2" + str(l[1][2] - 101) + ".png")
        carImg_4 = pygame.image.load("picture/TurtleObject/" + l[0] +  "/3" + str(l[1][3] - 101) + ".png")
        carImg_5 = pygame.image.load("picture/TurtleObject/" + l[0] +  "/4" + str(l[1][4] - 101) + ".png")
    else:
        carImg_1 = pygame.image.load("picture/TurtleObject/" + l[0] + "/" + car_1 + ".png")
        carImg_2 = pygame.image.load("picture/TurtleObject/" + l[0] + "/" + car_2 + ".png")
        carImg_3 = pygame.image.load("picture/TurtleObject/" + l[0] + "/" + car_3 + ".png")
        carImg_4 = pygame.image.load("picture/TurtleObject/" + l[0] + "/" + car_4 + ".png")
        carImg_5 = pygame.image.load("picture/TurtleObject/" + l[0] + "/" + car_5 + ".png")

    car_Img=[carImg_1,carImg_2,carImg_3,carImg_4,carImg_5]


    # this variable is needed to check if gold input is a number or not
    good_to_start = 1

    # variables to set main car
    set = -1
    choosen_car = 2

    # if it's user first time playing
    if first_time_log_in == True:
        # gold when play first time
        total_account = 1000
        first_time_log_in = False
    else:
        welcome_back_text_display = True
        welcome_name = player_name


    while True:

        run = 0
        # run is a variable for funtion return


        # set, choosen_car is variables for choosing the main car
        # set_Maincar function will be update later
        # so please ignore the 2 variables above

        display_surface.blit(background, (0, 0))

        #def button_start_menu(text , x, y, width, height, color, highlight_color, function = None, car_img)
        for i in range(0,5):
            if(choosen_car == i):
                set = button_start_menu('Lane ' + str(i+1), button_start_menu_x + 160 * i, button_start_menu_y,
                                        button_start_menu_width,
                                        button_start_menu_height, (255,137,25), (255,137,25), i, car_Img[i], l[2][i])
            else:
                set = button_start_menu('Lane ' + str(i+1), button_start_menu_x + 160*i, button_start_menu_y, button_start_menu_width,
                                    button_start_menu_height, black, (255,137,25), i, car_Img[i], l[2][i])
            if set != None:
                choosen_car = set

        # Pass first spell function
        if total_account >= 1200 and passSpell_active == False:
            run = button('Pass Spell', passSpell_button_x, passSpell_button_y, passSpell_button_width, passSpell_button_height, bright_blue, blue, PASS_SPELL)
            if run == PASS_SPELL:
                total_account, passSpell_active = pass_First_Spell_box(total_account)

        # Minigame button
        if total_account <= 100:
            run = button('Minigame', Minigame_button_x, Minigame_button_y, Minigame_button_width, Minigame_button_height,(178,34,34),(139,0,0), MINIGAME_ASK)
            if run == MINIGAME_ASK:
                run = Minigame_ask_box()
                if run != 0:
                    break

        #def button(text, x, y, width, height, color, highlight_color, function=None):
        run = button('Back', button_x, button_y + 250, button_width, button_height, button_color, highlight_button_color, 999)
        if run != 0:
            break

        # check if gold input is a number or not
        if good_to_start == 1:
            run = button('Start', start_button_x, start_button_y, button_width, button_height, button_color, highlight_button_color,START_PLAYING_GAME)
            if run != 0:
                break
        else:
            pass



        # def message_display(text, text_x, text_y, font, font_size, text_color):
        message_display('Gold bet', gold_text_box_x + 80, gold_text_box_y - 15, 'font/Sheeping Cats Straight.otf', 30, gold)
        message_display('Name', name_text_box_x + 47, name_text_box_y - 15, 'font/Sheeping Cats Straight.otf', 30, bright_red)

        if welcome_back_text_display == True:
            message_display('Welcome back ' + welcome_name, welcome_back_text_x, welcome_back_text_y, 'font/CALIBRIB.ttf', 30, (255, 0, 255))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    welcome_back_text_display = False


        # wallet box
        # def wallet_box(text, x, y, width, height):
        wallet_box(str(total_account), wallet_text_box_x, wallet_text_box_y, wallet_text_box_width, wallet_text_box_height)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            gold_input_box.handle_event(event)
            name_input_box.handle_event(event)

        for box in input_boxes:
            # draw the text boxes every loop
            box.draw(display_surface)

        # Just make things clearer
        player_gold_bet = gold_input_box.text
        player_name = name_input_box.text

        # check if user have 0 gold or not
        if total_account == 0:
            good_to_start = 0
            message_display('Please play minigame to gain gold', start_button_x - 30, start_button_y + 25, 'font/CALIBRIB.ttf', 25, red)
        else:
            # check if gold input is a number or not
            if isNumber(player_gold_bet) != True or int(player_gold_bet) != int(float(player_gold_bet)):
                good_to_start = 0
                message_display('Gold bet need to be a valid number to start', start_button_x - 30, start_button_y + 25, 'font/CALIBRIB.ttf', 25, red)
            elif int(player_gold_bet) < 0:
                good_to_start = 0
                message_display('Gold bet need to be a positive number', start_button_x - 30, start_button_y + 25, 'font/CALIBRIB.ttf', 25, red)
            elif int(player_gold_bet) > total_account:
                good_to_start = 0
                message_display('Gold bet can not be bigger', start_button_x + 30, start_button_y, 'font/CALIBRIB.ttf', 25, red)
                message_display('than your wallet gold', start_button_x + 30, start_button_y + 25, 'font/CALIBRIB.ttf', 25, red)
            elif int(player_gold_bet) == 0:
                good_to_start = 0
                message_display('Gold bet need to be a bigger than 0', start_button_x - 30, start_button_y + 25, 'font/CALIBRIB.ttf', 25, red)
            else:
                good_to_start = 1


        pygame.display.update()


    return run, choosen_car, player_gold_bet, player_name, total_account, first_time_log_in, passSpell_active


#if __name__ == '__main__':
#   startgame()
 #   pygame.quit()
 #   quit()