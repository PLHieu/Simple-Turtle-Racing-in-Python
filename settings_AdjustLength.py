import pygame

SHORT_LENGTH = 2000
MEDIUM_LENGTH = 2500
LONG_LENGTH = 3000
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
LENGTH =0
length = 2000

pygame.display.set_caption("Turtle Race")
background = pygame.image.load("picture/background/menu_backgroundsettings.png")
button_text_font = pygame.font.SysFont('comicsansms', int(SCREEN_WIDTH/80*3))
white = (255, 255, 255)
black = (0, 0, 0)
grey = (50, 50, 50)
red = (255,0,0)
lightgrey = [(169,169,169),(169,169,169),(169,169,169)]


bright_red = (255, 0, 0)
yellow = (255, 255, 0)
gold = (255, 223, 0)

b_width = SCREEN_WIDTH/4
b_height = SCREEN_WIDTH/6
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.SysFont('comicsansms', int(SCREEN_WIDTH/80*3))
class InputBox:

    def __init__(self, x, y, w, h, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        # self.text will be the text display when user type in
        self.storedValue = text
        # self.storedValue is the variable stored the text( or value) after the user press Enter
        self.txt_surface = FONT.render(text, True, black)
        self.active = False

    def handle_event(self, event):
        global lightgrey

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            lightgrey = [(169, 169, 169), (169, 169, 169), (169, 169, 169)]
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
                    self.text = ""
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
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

def text_object(text, font, text_color):
    text_surface = font.render(text, True, text_color)
    return text_surface, text_surface.get_rect()
def message_display(win,text, text_x, text_y, text_color):
    TextSurf, TextRect = text_object(text, pygame.font.SysFont('comicsansms', 40), text_color)
    TextRect.center = (text_x, text_y)
    win.blit(TextSurf, TextRect)
def message_display1(win,text, text_x, text_y, text_color):
    TextSurf, TextRect = text_object(text, pygame.font.SysFont('comicsansms', 22), text_color)
    TextRect.midleft = (text_x, text_y)
    win.blit(TextSurf, TextRect)
def button(win, text1,text2, choice ,x, y, width, height, color, highlight_color, function = None):
    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(win, highlight_color, (x, y, width, height))
    else:
        pygame.draw.rect(win, color, (x, y, width, height))

    textSurf1, textRect1 = text_object(text1, button_text_font, white)
    textRect1.center = (x + (width / 2), y + (height / 2 - 20 * choice))
    textSurf2, textRect2 = text_object(text2, button_text_font, white)
    textRect2.center = (x + (width / 2), y + (height / 2 + 20 * choice))
    win.blit(textSurf1, textRect1)
    win.blit(textSurf2, textRect2)
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        if clicked[0] == 1 and function != None:
            function()
            return True
LENGTH =2000


def set_long_length():
    global  LENGTH
    global lightgrey
    lightgrey[0]=(169,169,169)
    lightgrey[1]=(169,169,169)
    lightgrey[2]=(50,50,50)
    LENGTH = 2500

def set_short_length():
    global LENGTH
    global lightgrey
    lightgrey[0] = (50,50,50)
    lightgrey[1] = (169, 169, 169)
    lightgrey[2] = (169, 169, 169)
    LENGTH = 1500

def set_medium_length():
    global LENGTH
    global lightgrey
    lightgrey[0] = (169, 169, 169)
    lightgrey[1] = (50, 50, 50)
    lightgrey[2] = (169, 169, 169)
    LENGTH = 2000

def Back():
    return


def set_length():
    return length

def isNumber(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def ROAD_LENGTH(win):
    global length
    global f_length
    f_length = length
    global lightgrey
    run =True
    ok =False
    Ok=False
    win.blit(background, (0,0))
    input_box_x = SCREEN_WIDTH/16*5
    input_box_y = SCREEN_HEIGHT/5*3
    text_box_width = SCREEN_WIDTH/8*3
    text_box_height = SCREEN_HEIGHT/12
    length_input_box = InputBox(input_box_x,input_box_y,text_box_width,text_box_height)
    message_display(win, "SETTING LENGTH OF THE ROAD", SCREEN_WIDTH / 2, SCREEN_WIDTH / 10, white)
    message_display(win,"Length: ",input_box_x-SCREEN_WIDTH/80*7,input_box_y+SCREEN_HEIGHT/300*11,white)
    while run:
        choose =False
        message_display(win,"SETTING LENGTH OF THE ROAD",SCREEN_WIDTH/2,SCREEN_WIDTH/10,white)

        ok = button(win,"SHORT","(2000)",1, SCREEN_WIDTH/16, SCREEN_HEIGHT/4, b_width, b_height, lightgrey[0], grey, set_short_length)
        if ok:
            length =LENGTH
        ok = button(win,"MEDIUM","(2500)",1, SCREEN_WIDTH/8*3, SCREEN_HEIGHT/4, b_width, b_height, lightgrey[1], grey, set_medium_length)
        if ok:
            length =LENGTH
        ok = button(win,"LONG","(3000)",1, SCREEN_WIDTH/16*11, SCREEN_HEIGHT/4, b_width, b_height, lightgrey[2], grey, set_long_length)
        if ok:
            length =LENGTH
        #back without changing anything
        back = button(win,"BACK","",0, SCREEN_WIDTH/2 + 2, SCREEN_HEIGHT/13*11, SCREEN_WIDTH/16*3, SCREEN_HEIGHT/15, black, grey, Back)
        Ok = button(win,"OK","",0,SCREEN_WIDTH/16*5 - 2,SCREEN_HEIGHT/13*11, SCREEN_WIDTH/16*3,SCREEN_HEIGHT/15, black, grey, Back)
        #click to take the value player set
        choose = button(win,"Choose","",0,input_box_x+text_box_width+10,input_box_y +SCREEN_HEIGHT/120 ,SCREEN_WIDTH/16*3,SCREEN_HEIGHT/15, black, grey,Back)

        if back:
            return f_length

        if Ok:
            return length
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            length_input_box.handle_event(event)
        length_input_box.draw(win)
        str = length_input_box.text
        if str != "" and choose:
            if isNumber(str) and int(str)>2000 and int(str)<8000:      
                length = int(str)
            else:
                message_display1(win,"Please input a NUMBER (2000<NUMBER<8000)", input_box_x,input_box_y + SCREEN_HEIGHT/8,red)


        pygame.display.update()

