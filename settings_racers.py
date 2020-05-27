import pygame,history  # pygame 1.9.5, pygame.QUIT() no more

pygame.init()
display_surface = pygame.display.set_mode((800, 600))


# color for the text box
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        FONT = pygame.font.SysFont("comicsansms", 22)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.storedValue = text
        self.txt_surface = FONT.render(text, True, (0,0,0))
        self.active = False

    def handle_event(self, event):
        FONT = pygame.font.SysFont("comicsansms", 22)
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
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif self.txt_surface.get_width() < self.rect.w - 20:
                    self.text += event.unicode
                else:
                    pass
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, (0,0,0))

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        screen.blit(self.txt_surface, (self.rect.x , self.rect.y ))


# sau nay se import cai nay tu file cua thang Hao
def text_object(text, font, text_color):
    text_surface = font.render(text, True, text_color)
    return text_surface, text_surface.get_rect()
def button(display_surface,text ,x, y, width, height, color, highlight_color, function = None, ts1 = None):
    font = pygame.font.SysFont("comicsansms", 22)
    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()
    output_number = None

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(display_surface, highlight_color, (x, y, width, height))

        if clicked[0] == 1 and function != None:
            output_number = function(ts1)
    else:
        pygame.draw.rect(display_surface, color, (x, y, width, height))

    textSurf, textRect = text_object(text, font, (0,0,0))
    textRect.center = (x + (width / 2), y + (height / 2))
    display_surface.blit(textSurf, textRect)
    return output_number


def draw_racertype_settings(screen, posx, posy, l, w, color, text):
    r = pygame.Rect(posx, posy, l, w)
    pygame.draw.rect(screen, color, r)
    text_rect = text.get_rect()
    text_rect.center = r.center
    screen.blit(text, text_rect)


# cac function dung de truyen vao button
def type_choosing_resulf(type_racer):
    return type_racer


def color_oneRacer_resulf(color):
    return color


def draw_color_chosing_board(screen, posx, posy, leng_board, width_board):
    color_racer_choosecolor_settings = (
        (237, 125, 49), (68, 114, 196), (220, 0, 0), (0, 176, 80), (229, 24, 94),(255, 255, 255) , (253, 242, 28),
        (104, 33, 122))
    color_racer_choosecolor_settings_hightlight = (
        (255, 145, 60), (80, 130, 220), (255, 10, 10), (0, 200, 100), (240, 40, 120), (220, 220, 220), (255, 255, 60),
        (104, 33, 122))
    j = 0


    #cac bien phuc vu cho viec chon mau sac
    lon = None
    result = None


    for i in range(0, 4):
        lon = button(screen,"",posx + leng_board / 25 + (leng_board / 25 + leng_board / 5) * i, posy + width_board / 9, leng_board / 5,width_board / 3,color_racer_choosecolor_settings[j],color_racer_choosecolor_settings_hightlight[j],color_oneRacer_resulf,j+100 +1)
        if(lon!=None):
            result = lon
        lon = button(screen, "",posx + leng_board / 25 + (leng_board / 25 + leng_board / 5) * i, posy + width_board / 9 * 2 + width_board / 3,leng_board / 5, width_board / 3,color_racer_choosecolor_settings[j+4],color_racer_choosecolor_settings_hightlight[j+4],color_oneRacer_resulf,j+4+100 + 1)
        if(lon!=None):
            result = lon

        j += 1

    return result


def draw_name(screen, posx, posy, leng_board, width_board):
    pygame.draw.rect(screen, (189, 189, 189,),
                     (posx + leng_board / 7, posy + width_board / 10, leng_board / 7 * 5, width_board / 4))


def result_face(face):
    return face


def click_ok(ts  = None):
    return True

def kiemtra_cochularong(list):

    for chu in list:
        if chu == "" :
            return True

    return False

# ham chinh
# tham so in_settings
def Racer_settings(screen,st = None):

    #dung cho viec thong bao phai nhap day du thi moi duoc nhan OK
    font_thongbao = pygame.font.SysFont("comicsansms", 24)
    textSurf, textRect = text_object("Please entering racer's name !", font_thongbao, (255, 0, 0))


    in_setting = st[:]
    # ve cac doi tuong
    running = True
    a = pygame.display.get_surface().get_width()
    b = pygame.display.get_surface().get_height()

    # chua cac seting ve xe
    setting = []
    racers = [None,None,None,None,None]
    racers_face = [None,None,None,None,None]

    # phuc vu cho viec chon type
    type_resulf = None # chua car type
    lon = None # khong  nen quan tam bien nay dung de lam gi


    # phuc vu cho viec chon color cho tung racer
    l_color = [None,None,None,None,None]
    l_onecar = None
    background = pygame.image.load("picture/background/menu_backgroundsettings.png")


    #phuc vu cho viec chon name cho tung racer
    l_inputbox = [None,None,None,None,None]
    for i in range(0,5):
        l_inputbox[i] = InputBox(a / 36 + (a / 6 + a / 36) * i + a/42, b*0.37, a*5/42, b / 20)
    l_name = [None,None,None,None,None]


    # khoi tao cac chu
    color_type_racer_settings = ((200, 0, 0), (200, 200, 0), (0, 176, 80), (46, 117, 182),(237, 125, 49),(229, 24, 94),(255, 255, 255))
    color_type_racer_settings_hightlight = ((255, 30, 30), (255, 255, 30), (30, 206, 110), (76, 147, 212),(255, 156, 80),(250, 60, 130),(220, 220, 220))
    chudemohang1 = ["TRUCK","TANK","CAR","SUPER","PJTeam","FUTURISTIC_TRUCK","FUTURE_CAR"]


    #phuc vu cho viec chon cac option
    ok = False
    back = False

    type_resulf  = in_setting[0]
    l_color = in_setting[1].copy()
    l_name = in_setting[2].copy()


    while (running):
        screen.blit(background, (0, 0))

        # draw type car choose
        for i in range(0, 7):
            if i <= 4:
                lon = button(screen, chudemohang1[i],   a /36 + (a/6 + a/36)*i,   3 / 32 * b,   a / 6,   2 / 25 * b,
                                    color_type_racer_settings[i],color_type_racer_settings_hightlight[i],type_choosing_resulf,chudemohang1[i])
                if(lon != None):
                    type_resulf = lon
            else:
                lon = button(screen, chudemohang1[i], a / 9 + (a / 3 + a / 9) * (i-5), 0.2 * b, a / 3, 2 / 25 * b,
                             color_type_racer_settings[i], color_type_racer_settings_hightlight[i],
                             type_choosing_resulf, chudemohang1[i])
                if (lon != None):
                    type_resulf = lon

        # draw information car,draw choose car face, choose car color
        for i in range(0, 5):
            pygame.draw.rect(screen, (255, 230, 153), (a / 36 + (a / 6 + a / 36) * i, b / 3, a / 6, b / 5))
            pygame.draw.rect(screen, (248, 203, 173), (a / 36 + (a / 6 + a / 36) * i, b * 0.55, a / 6, b * 0.2))

            #color
            l_onecar = draw_color_chosing_board(screen, a / 36 + (a / 6 + a / 36) * i, 0.55 * b, a / 6, 0.2 * b)
            if(l_onecar!=None):
                l_color[i] = l_onecar


        # draw button OK
        if(kiemtra_cochularong(l_name)):
            display_surface.blit(textSurf,(a * 0.16, b * 0.85) )
        else:
            ok = button(screen, "OK",a * 0.25, b * 0.85, a *0.15, b * 0.08, (255,255,255),(220,220,220),click_ok)
        back = button(screen, "BACK",a * 0.6, b * 0.85, a*0.15, b * 0.08, (255,255,255),(220,220,220),click_ok)

        for event in pygame.event.get():
            if event.type == pygame.quit:
                running = False

            for i in range(0, 5):
                l_inputbox[i].handle_event(event)

        for i in range(0,5):
            l_inputbox[i].draw(screen)
            l_name[i] = l_inputbox[i].text

        setting = [type_resulf,l_color,l_name]

        for i in range (0,5):
            if(type_resulf !=None and l_color[i] != None  ):
                if(type_resulf == "PJTeam"):
                    racers[i] = pygame.image.load(
                        "picture/TurtleObject/" + str(type_resulf) + "/" + str(i) + str(l_color[i]-101) + ".png")
                    screen.blit(racers[i], (0.08 * a + (a / 6 + a / 36) * i, 0.45 * b))
                else:
                    racers[i] = pygame.image.load("picture/TurtleObject/" + str(type_resulf) + "/" + str(type_resulf)+ str(l_color[i]) + ".png")
                    screen.blit(racers[i],(0.08*a + (a / 6 + a / 36) * i,0.45*b))

        if(ok == True):
            return setting
        if (back == True):
            return st


        pygame.display.update()


#
#
# settings_game =  ["SUPER", [101,108,106,104,102], ["Long Hieu","Khi dau cho","Hau cuzzz","Hao hao","Hien huynh"]]
#
# l = []
# Racer_settings(display_surface, settings_game)
