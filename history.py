# Update 12/04/2019 9:37AM: restructure main menu and button behaviour

import pygame       # pygame 1.9.5, pygame.QUIT() no more

pygame.init()

# Definitions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

white = (255, 255, 255)
bluewhite = (180, 210, 255)
black = (0, 0, 0)
grey = (50, 50, 50)
gray = (100, 100, 100)
darkgray = (30, 30, 30)
lightgray = (170, 170, 170)
bright_blue = (0, 0, 255)
bright_red = (255, 0, 0)
yellow = (255, 255, 0)
gold = (255, 223, 0)
blue = (30, 50, 200)
darkblue = (50, 60, 175)
lightblue = (20, 30, 255)
skytblue = (100, 200, 255)
orange = (240, 180, 20)
darkgreen = (50, 170, 40)
green = (20, 210, 30)
lightgreen = (10, 255, 20)

# Definition for function names (need to not be 0)
MAIN_MENU = 555
START_GAME = 999
SETTING = 768
HISTORY = 79
HELP = 101
ABOUT = 113
EXIT = 115
NOTEXIT = 116
BACK = 99

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

background = pygame.image.load("picture/background/Historybackground.png")

pygame.display.set_caption('Race menu')
#
# carImg_1 = pygame.image.load("bluecar.gif")

# font input typing
FONT = pygame.font.Font(None, 36)
textsize = 36
textcolor = (0, 0, 0)
# color for the text box
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, bright_red)
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
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, bright_red)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
class History_data:
    #index 0: Rank
    #index 1: Road_lenght
    #index 2: Time
    #index 3: Bet money
    #index 4: Account change
    #index 5: Total account
    #index 6: Is a new account
    data = [0, 0, 0, 0, 0, 0, 0]
    def __init__(self, rank, bet_amount, account_change, account, road_length = 0, time = 0, new_account = 0):
        if new_account != 0:
            self.data = [0, 0, 0, 0, 0, new_account, 1]
        else:
            self.data = [rank, road_length, time, bet_amount, account_change, account, 0]
class History_List:
    List = []
    number = 0
    def add(self, rank, bet_amount, account_change, road_length = 0, time = 0, new_account = 0):
        if new_account != 0:
            htemp = History_data(0, 0, 0, 0, 0, 0, new_account)
        else:
            if self.number > 0:
                htemp = History_data(rank, bet_amount, account_change, self.List[self.number - 1].data[5] + account_change, road_length, time, new_account)
            else:
                htemp = History_data(rank, bet_amount, account_change, account_change, road_length, time, new_account)
                i = 1
        self.List.append(htemp)
        self.number += 1


HistoryList = History_List()

def text_object(text, font, text_color):
    text_surface = font.render(text, True, text_color)
    return text_surface, text_surface.get_rect()


def exitgame():
    pygame.quit()
    quit()

def message_display(text, text_x, text_y, text_color):
    text_box_font = pygame.font.SysFont('arial', 30, True)

    TextSurf, TextRect = text_object(text, text_box_font, text_color)
    TextRect.center = (text_x, text_y)
    display_surface.blit(TextSurf, TextRect)


def button_start_menu(text , x, y, width, height, color, highlight_color, function = None, car_img = None):
    button_text_font = pygame.font.SysFont('arial', 20)

    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(display_surface, highlight_color, (x, y, width, height))
        if clicked[0] == 1 and function != None:
            function()
    else:
        pygame.draw.rect(display_surface, color, (x, y, width, height))

    textSurf, textRect = text_object(text, button_text_font, white)
    textRect.center = (x + (width / 2), y + (height - 20))
    display_surface.blit(textSurf, textRect)

    if car_img != None:
        display_surface.blit(car_img, (x + (width * 0.35), y + (height * 0.45)))

def button(text ,x, y, width, height, color, highlight_color, function = None):
    button_text_font = pygame.font.SysFont('arial', 20)

    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()
    output_number = 0

    if (x < mouse[0] < x + width) and (y < mouse[1] < y + height):
        pygame.draw.rect(display_surface, highlight_color, (x, y, width, height))

        if clicked[0] == 1 and function != None:
            output_number = function

    else:
        pygame.draw.rect(display_surface, color, (x, y, width, height))
    textSurf, textRect = text_object(text, button_text_font, white)
    textRect.center = (x + (width / 2), y + (height / 2))
    display_surface.blit(textSurf, textRect)
    return output_number

def exitfunc():
    stroke = 3
    strokecolor = blue
    backgroundcolor = green
    exit_ask_box = button("Are you sure you want to exit?", SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2-70, 300, 150, backgroundcolor, backgroundcolor)

    button_width = 70
    button_height = 40
    distance = 20
    startx = SCREEN_WIDTH/2 - button_width - distance/2
    starty = SCREEN_HEIGHT/2 + 30
    key = "Yes"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key = "Yes"
                elif event.key == pygame.K_RIGHT:
                    key = "No"
                elif event.key == pygame.K_KP_ENTER or event.key == 13:
                    if key == "Yes":
                        exitgame()
                    else:
                        return 0

        mousepress = pygame.mouse.get_pressed()
        if key == "Yes":
            pygame.draw.rect(display_surface, strokecolor, (startx - stroke, starty - stroke, button_width + 2*stroke, button_height + 2*stroke))
            pygame.draw.rect(display_surface, backgroundcolor,
                             (startx + button_width + distance - stroke, starty - stroke, button_width + 2 * stroke, button_height + 2 * stroke))

        if key == "No":
            pygame.draw.rect(display_surface, backgroundcolor, (startx - stroke, starty - stroke, button_width + 2*stroke, button_height + 2*stroke))
            pygame.draw.rect(display_surface, strokecolor,
                             (startx + button_width + distance - stroke, starty - stroke, button_width + 2 * stroke, button_height + 2 * stroke))
        res = button("Yes", startx, starty, button_width, button_height, darkgreen, lightgreen, EXIT)
        if res == EXIT:
            if mousepress[0]==1:
                exitgame()
        res = button("No", startx + button_width + distance, starty, button_width, button_height, darkgreen, lightgreen, NOTEXIT)
        if res == NOTEXIT:
            if mousepress[0]==1:
                return 0
        pygame.display.update((SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2-70, 300, 150))


resolutions = [(800, 600), (960, 640), (1280, 680)]
road_lengths = [3000, 5000, 7000]
background_number = 0
resolution_number = 0
road_length_number = 0

def Settings_menu(background_number, resolution_number, road_length_number):
    setting_text_font = pygame.font.SysFont("Arial", 100, True, True)
    setting_font = pygame.font.SysFont("Arial", 35, True)
    setting_text_color = darkgray
    text_color = white
    background_settings = pygame.image.load('menu_accent.png')
    # Button attributes
    b_width = 150
    b_height = 40
    b_back_button_x = SCREEN_WIDTH - 200
    b_back_button_y = SCREEN_HEIGHT - 100
    b_color = black
    b_highlight_color = grey
    b_select_color = gray


    def button_select(text, x, y, width, height, color, highlight_color, select_color, current, do = None):
        button_text_font = pygame.font.SysFont('arial', 20)

        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        output_number = current

        if (x < mouse[0] < x + width) and (y < mouse[1] < y + height):
            pygame.draw.rect(display_surface, highlight_color, (x, y, width, height))
            if clicked[0] == 1 and do != None:
                output_number = do
        elif current == do:
            pygame.draw.rect(display_surface, select_color, (x, y, width, height))
        else:
            pygame.draw.rect(display_surface, color, (x, y, width, height))
        textSurf, textRect = text_object(text, button_text_font, white)
        textRect.center = (x + (width / 2), y + (height / 2))
        display_surface.blit(textSurf, textRect)
        return output_number

    setting_text, setting_text_rect = text_object('Settings', setting_text_font, setting_text_color)
    bg_num = 3  # Max number of backgrounds
    bg_pos = [(80, 100), (280, 100), (480, 100)]
    bg_name = ['Forest', 'Desert', 'City']
    bg_text, bg_text_rect = text_object('Backgrounds', setting_font, text_color)
    bg_text_rect.bottomleft = (80, 90)

    res_num = 3 # Max number of resolution
    res_pos = [(80, 250), (280, 250), (480, 250)]
    res_name = ['800 x 600', '960 x 640', '1080 x 680']
    res_text, res_text_rect = text_object('Resolutions', setting_font, text_color)
    res_text_rect.bottomleft = (80, 240)

    road_num = 3    # Max number of road lengths
    road_pos = [(80, 400), (280, 400), (480, 400)]
    road_name = ['Short', 'Medium', 'Long']
    road_text, road_text_rect = text_object('Road lengths', setting_font, text_color)
    road_text_rect.bottomleft = (80, 390)

    while True:
        display_surface.blit(background_settings, (0, 0))
        display_surface.blit(setting_text, setting_text_rect)
        # Backgrounds
        display_surface.blit(bg_text, bg_text_rect)
        for i in range(bg_num):
            background_number = button_select(bg_name[i], bg_pos[i][0], bg_pos[i][1], b_width, b_height,
                                              b_color, b_highlight_color, b_select_color, background_number, i)
        # Resolutions
        display_surface.blit(res_text, res_text_rect)
        for i in range(res_num):
            resolution_number = button_select(res_name[i], res_pos[i][0], res_pos[i][1], b_width, b_height,
                                              b_color, b_highlight_color, b_select_color, resolution_number, i)
        # Road_lengths
        display_surface.blit(road_text, road_text_rect)
        for i in range(road_num):
            road_length_number = button_select(road_name[i], road_pos[i][0], road_pos[i][1], b_width, b_height,
                                               b_color, b_highlight_color, b_select_color, road_length_number, i)
        # back button
        back_button = button("Back", b_back_button_x, b_back_button_y, b_width, b_height, b_color, b_highlight_color, BACK)
        if back_button == BACK:
            return MAIN_MENU
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = MAIN_MENU
        pygame.display.update()
    return 0

def History_board(HistoryList):
    font = pygame.font.SysFont("Goudy Stout, Arial", 56)
    border = 30
    title_surface, title_Rect = text_object("History", font, white)
    xstartboard = 2*border
    ystartboard = 3*border
    boardwidth = SCREEN_WIDTH - 4*border
    boardheight = SCREEN_HEIGHT - 6*border

    num_line_per_board = 11
    linestartx = xstartboard
    linestarty = ystartboard
    linewidth = boardwidth
    lineheight = boardheight/num_line_per_board
    scroll_width = 15
    if HistoryList.number < num_line_per_board:
        scroll_height = (num_line_per_board - 1)*lineheight
        maxline = HistoryList.number
    else:
        scroll_height = int(((num_line_per_board-1)/HistoryList.number)*(num_line_per_board - 1)*lineheight)
        maxline = num_line_per_board - 1
    num_portion = 6
    portion_border = 3 #pixel
    width_portion = boardwidth/num_portion

    back_button_width = 100
    back_button_height = 50
    back_button_startx = xstartboard + int(boardwidth/2) - back_button_width/2
    back_button_starty = ystartboard + boardheight

    #pygame.draw.rect(display_surface, green, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    timg = pygame.image.load("picture/background/Historybackground.png")
    display_surface.blit(timg, (0, 0))
    #pygame.draw.rect(display_surface, darkblue, (border, border, SCREEN_WIDTH-2*border, SCREEN_HEIGHT-2*border))
    title_Rect.center = (border + int(boardwidth/2), border + int((ystartboard - border)/2))
    display_surface.blit(title_surface, title_Rect)
    pygame.draw.rect(display_surface, blue, (xstartboard, ystartboard, boardwidth, boardheight))

    pygame.draw.rect(display_surface, orange, (linestartx, linestarty, linewidth, lineheight))
    textsize = int(0.4*lineheight)
    font = pygame.font.SysFont("Forte, Arial", textsize)
    nametxt = [["Rank"], ["Road", "length"], ["time"], ["Bet"], ["Account", "change"], ["Total", "account"]]
    #nametxt = "Rank"
    for i in range(1, 7):
        if i > 1:
            pygame.draw.rect(display_surface, gray, (linestartx + (i-1) * width_portion, linestarty, portion_border, lineheight))
        try:
            trash = nametxt[i-1][1]
            for j in range(0, 2):
                texthold, text_Rect = text_object(nametxt[i-1][j], font, black)
                text_Rect.center = (int(linestartx + (i - 0.5) * width_portion), int(linestarty + lineheight*(j+1)/3))
                display_surface.blit(texthold, text_Rect)
        except:
            texthold, text_Rect = text_object(nametxt[i - 1][0], font, black)
            text_Rect.center = (int(linestartx + (i - 0.5) * width_portion), int(linestarty + lineheight/2))
            display_surface.blit(texthold, text_Rect)

    pygame.display.update()

    hold_mouse = 0
    hold_mouse_down = 0
    if HistoryList.number != 0 :
        max_hold_mouse_down = int((1 - (num_line_per_board-1)/HistoryList.number)*(num_line_per_board - 1)*lineheight)
    else:
        max_hold_mouse_down = 0
    start_hold_mousey = 0

    draw = 1
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 1 - exitfunc()
                draw = 1
        if draw == 1:

            for i in range(0 + int(hold_mouse_down*HistoryList.number/(num_line_per_board - 1)/lineheight), maxline + int(hold_mouse_down*HistoryList.number/(num_line_per_board - 1)/lineheight) + 1):
                #those line
                try:
                    HistoryList.List[i]
                except:
                    break
                pygame.draw.rect(display_surface, skytblue*(i%2 == 0)+bluewhite*(i%2 == 1), (linestartx, linestarty + (i+1)*lineheight - (HistoryList.number/(num_line_per_board-1))*hold_mouse_down, linewidth, lineheight))
                for j in range(0, 6):
                    if j != 4:
                        text = str(HistoryList.List[i].data[j])
                    else:
                        if HistoryList.List[i].data[j] >= 0:
                            text = '+' + str(HistoryList.List[i].data[j])
                        else:
                            text = str(HistoryList.List[i].data[j])
                    texthold, text_Rect = text_object(text, font, black)
                    text_Rect.center = (
                    int(linestartx + (j + 0.5) * width_portion), int(linestarty + (i + 1.5) * lineheight - (HistoryList.number/(num_line_per_board-1))*hold_mouse_down))
                    display_surface.blit(texthold, text_Rect)

            # fence
            for i in range(1, num_portion):
                pygame.draw.rect(display_surface, gray, (
                    linestartx + i * width_portion, linestarty + lineheight, portion_border, maxline * lineheight))

            # scroll
            pygame.draw.rect(display_surface, darkgray, (
            xstartboard + boardwidth - scroll_width, ystartboard + lineheight, scroll_width, boardheight - lineheight))
            pygame.draw.rect(display_surface, gray, (
            xstartboard + boardwidth - scroll_width, ystartboard + lineheight + hold_mouse_down, scroll_width,
            scroll_height))
            # update
            pygame.display.update((xstartboard, ystartboard + lineheight, boardwidth, boardheight - lineheight))
            # pause to save manipulation time, waiting for response
            draw = 0

        mouse_press = button("", xstartboard + boardwidth - scroll_width, ystartboard + lineheight + hold_mouse_down, scroll_width, scroll_height, gray, lightgray, 1)
        pygame.display.update((xstartboard + boardwidth - scroll_width, ystartboard + lineheight + hold_mouse_down,
                             scroll_width, scroll_height))
        #mouse_press = pygame.mouse.get_pressed()
        mousex, mousey =pygame.mouse.get_pos()
        #if (xstartboard + boardwidth - scroll_width<mousex<xstartboard + boardwidth - scroll_width+scroll_width)and(ystartboard + lineheight + hold_mouse_down<mousey<ystartboard + lineheight + hold_mouse_down + scroll_height):
        if mouse_press == 1 and hold_mouse == 1:
            hold_mouse = 1
            if int((mousey - start_hold_mousey)) != 0:
                draw = 1
                hold_mouse_down += int((mousey - start_hold_mousey))
                start_hold_mousey = mousey
            else:
                draw = 0
            if hold_mouse_down > max_hold_mouse_down:
                hold_mouse_down = max_hold_mouse_down
            if hold_mouse_down < 0:
                hold_mouse_down = 0
        elif mouse_press == 1 and hold_mouse == 0:
            hold_mouse = 1
            start_hold_mousey = mousey
        elif mouse_press == 0 and hold_mouse == 1:
            hold_mouse = 0
        else:
            pass

        #back button
        back_button = button("Back", back_button_startx, back_button_starty, back_button_width, back_button_height, black, grey, BACK)
        if back_button==BACK:
            return 0
        pygame.display.update((back_button_startx, back_button_starty, back_button_width, back_button_height))
        #pygame.display.update()
    return 0

def Help_board():
    font = pygame.font.SysFont("Goudy Stout, Arial", 56)
    title_surface, title_Rect = text_object("Help", font, white)

    font = pygame.font.SysFont("Comic Sans, Arial", 36)
    helptext = [
                ["Go to setting to choose the perfomance"],
                ["Click Play game in the main menu", "Enter the money your bet in the 'Gold'", "Enter the name", "Click Start and... GO"],
                ["If your money run out,", "You must play minigame to raise money"],
                []
                ]
    numparagraph = 4
    numline = 0
    for i in range(0, numparagraph):
        crash = 0
        j = 0
        while not crash:
            try:
                trash = helptext[i][j]
                numline += 1
                j += 1
            except:
                crash = 1
    numline += numparagraph
    border = 30
    xstartboard = 2 * border
    ystartboard = 3 * border
    boardwidth = SCREEN_WIDTH - 4 * border
    boardheight = SCREEN_HEIGHT - 6 * border

    num_line_per_board = 11
    linestartx = xstartboard + 5
    linestarty = ystartboard + 5
    linewidth = boardwidth - 10
    lineheight = boardheight/num_line_per_board
    scroll_width = 15
    if numline < num_line_per_board:
        scroll_height = (num_line_per_board)*lineheight
        maxline = numline
    else:
        scroll_height = int(((num_line_per_board-1)/numline)*(num_line_per_board)*lineheight)
        maxline = num_line_per_board - 1

    back_button_width = 100
    back_button_height = 50
    back_button_startx = xstartboard + int(boardwidth/2) - back_button_width/2
    back_button_starty = ystartboard + boardheight

    #outside board
    #pygame.draw.rect(display_surface, green, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    timg = pygame.image.load("Historybackground.jpg")
    display_surface.blit(timg, (0, 0))
    #pygame.draw.rect(display_surface, darkblue, (border, border, SCREEN_WIDTH-2*border, SCREEN_HEIGHT-2*border))

    #title
    title_Rect.center = (border + int(boardwidth/2), border + int((ystartboard - border)/2))
    display_surface.blit(title_surface, title_Rect)

    pygame.display.update()

    hold_mouse = 0
    hold_mouse_down = 0
    max_hold_mouse_down = int((1 - (num_line_per_board-1)/numline)*(num_line_per_board)*lineheight)
    start_hold_mousey = 0

    draw = 1
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 1 - exitfunc()
                draw = 1

        if draw == 1:
            pygame.draw.rect(display_surface, skytblue, (xstartboard, ystartboard, boardwidth, boardheight))

            paragraph = 0
            line = -1
            reachtext = int(hold_mouse_down * numline / (num_line_per_board - 1) / lineheight)
            while reachtext > 0:
                reachtext -= 1
                try:
                    line += 1
                    trash = helptext[paragraph][line]
                except:
                    line = -1
                    paragraph += 1
                    if paragraph >= numparagraph:
                        break
                    continue

            for i in range(0 + int(hold_mouse_down * numline / (num_line_per_board - 1) / lineheight),
                           maxline + int(hold_mouse_down * numline / (num_line_per_board - 1) / lineheight) + 1):

                try:
                    line += 1
                    trash = helptext[paragraph][line]
                except:
                    line = -1
                    paragraph += 1
                    if paragraph >= numparagraph:
                        break
                    continue

                texthold, text_Rect = text_object(helptext[paragraph][line], font, textcolor)
                display_surface.blit(texthold, (linestartx, linestarty + i*lineheight - (numline/(num_line_per_board-1))*hold_mouse_down))
            pygame.display.update((xstartboard, ystartboard, boardwidth, boardheight))
            draw = 0
        mouse_press = button("", xstartboard + boardwidth - scroll_width, ystartboard + hold_mouse_down,
                             scroll_width, scroll_height, gray, lightgray, 1)
        pygame.display.update((xstartboard + boardwidth - scroll_width, ystartboard + hold_mouse_down,
                             scroll_width, scroll_height))
        # mouse_press = pygame.mouse.get_pressed()
        mousex, mousey = pygame.mouse.get_pos()
        # if (xstartboard + boardwidth - scroll_width<mousex<xstartboard + boardwidth - scroll_width+scroll_width)and(ystartboard + lineheight + hold_mouse_down<mousey<ystartboard + lineheight + hold_mouse_down + scroll_height):
        if mouse_press == 1 and hold_mouse == 1:
            hold_mouse = 1
            if int((mousey - start_hold_mousey)) != 0:
                draw = 1
                hold_mouse_down += int((mousey - start_hold_mousey))
                start_hold_mousey = mousey
            else:
                draw = 0
            if hold_mouse_down > max_hold_mouse_down:
                hold_mouse_down = max_hold_mouse_down
            if hold_mouse_down < 0:
                hold_mouse_down = 0
        elif mouse_press == 1 and hold_mouse == 0:
            hold_mouse = 1
            start_hold_mousey = mousey
        elif mouse_press == 0 and hold_mouse == 1:
            hold_mouse = 0
        else:
            pass

        back_button = button("Back", back_button_startx, back_button_starty, back_button_width, back_button_height, black, grey, BACK)
        if back_button == BACK:
            return 0
        pygame.display.update((back_button_startx, back_button_starty, back_button_width, back_button_height))

    return 0

def game_menu():
    # Font
    title_font = pygame.font.SysFont('arial', 50, True)

    # Title
    title_accent = pygame.image.load('main_accent.png')
    title_accent_pos = (SCREEN_WIDTH - 260, SCREEN_HEIGHT - 460)
    game_title, game_title_rect = text_object('Turtle race', title_font, black)
    game_title_rect.bottomright = (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 400)


    button_x = SCREEN_WIDTH - 200
    button_y = SCREEN_HEIGHT - 350
    # Button attributes
    button_width = 150
    button_height = 40
    b_color = black
    b_highlight_color = grey
    # Because break is used, there's no need to use a bool variable
    while True:
        run = 0
        display_surface.blit(background, (0, 0))
        display_surface.blit(title_accent, title_accent_pos)
        display_surface.blit(game_title, game_title_rect)

        # Need constant checking to avoid relapses and run keep on being 0
        run = button('Play game', button_x, button_y, button_width, button_height, b_color, b_highlight_color, START_GAME)
        if run != 0:
            break
        run = button('Settings', button_x, button_y + 50, button_width, button_height, b_color, b_highlight_color, SETTING)
        if run != 0:
            break
        run = button('History', button_x, button_y + 100, button_width, button_height, b_color, b_highlight_color, HISTORY)
        if run == HISTORY:
            run = History_board(HistoryList)
        run = button('Help', button_x, button_y + 150, button_width, button_height, b_color, b_highlight_color, HELP)
        if run == HELP:
            run = Help_board()
        run = button('About', button_x, button_y + 200, button_width, button_height, b_color, b_highlight_color, ABOUT)
        if run != 0:
            break
        run = button('Exit', button_x, button_y + 250, button_width, button_height, b_color, b_highlight_color, EXIT)
        if run == EXIT:
            run = exitfunc()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = exitfunc()
        pygame.display.update()
    return run

def isMain():
    pass


def StartMenu():

    button_start_menu_x = 10
    button_start_menu_y = 10
    button_start_menu_width = 135
    button_start_menu_height = 150

    button_x = 600
    button_y = 250
    button_width = 150
    button_height = 40

    text_box_x = 50
    text_box_y = 400
    text_box_width = 200
    text_box_height = 32

    gold_input_box = InputBox(text_box_x, text_box_y, text_box_width, text_box_height)
    name_input_box = InputBox(text_box_x, text_box_y + 70, text_box_width, text_box_height)
    input_boxes = [gold_input_box, name_input_box]

    done = False

    while not done:

        display_surface.blit(background, (0, 0))

        # def button_start_menu(text, x, y, width, height, color, highlight_color, function=None, car_img=None)
        button_start_menu('Lane 1', button_start_menu_x , button_start_menu_y, button_start_menu_width, button_start_menu_height , black, grey, isMain, carImg_1)
        button_start_menu('Lane 2', button_start_menu_x + 160, button_start_menu_y, button_start_menu_width, button_start_menu_height, black, grey, isMain, carImg_1)
        button_start_menu('Lane 3', button_start_menu_x + 320, button_start_menu_y, button_start_menu_width, button_start_menu_height, black, grey, isMain, carImg_1)
        button_start_menu('Lane 4', button_start_menu_x + 480, button_start_menu_y, button_start_menu_width, button_start_menu_height, black, grey, isMain, carImg_1)
        button_start_menu('Lane 5', button_start_menu_x + 640, button_start_menu_y, button_start_menu_width, button_start_menu_height, black, grey, isMain, carImg_1)
        run = button('Back', button_x, button_y + 250, button_width, button_height, black, grey, MAIN_MENU)

        if run != 0:
            break
        #def message_display(text, text_x, text_y):Z
        message_display('Gold', text_box_x + 30, text_box_y - 15, gold)
        message_display('Name', text_box_x + 35, text_box_y + 55, bright_red)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.draw(display_surface)

        pygame.display.update()
    return run

#
# call_menu = MAIN_MENU
# #call_menu = START_GAME
# for i in range(0, 20, 1):
#     HistoryList.add(i, i*100, (1%5-2)*300, 100*i)
# HistoryList.add(1, 300, 300, 1000)
# HistoryList.add(3, 300, -75, 1300)
# HistoryList.add(2, 400, 0, 1225)
# while True:
#     if call_menu == MAIN_MENU:
#         call_menu = game_menu()
#     if call_menu == START_GAME:
#         call_menu = StartMenu()
#     if call_menu == SETTING:
#         call_menu = Settings_menu(background_number, resolution_number, road_length_number)
#     if call_menu == EXIT:
#         exitgame()
#
# pygame.quit()
# quit()
