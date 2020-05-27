"""Day la file chua class cua vat the dua xe, tuy theo nguoi dung thiet dat, vat the nay co the là xe hoi, xe keo,may bay ,.."""
import pygame,DEFINE

class emoji:
    # cai nay dung de tuy chinh emoji
    name = "None"  # co the la VEDICH1.png, VEDICH2.png, KHONGVEDICH1.png,..
    picture = None
    posx = 0
    posy = 0
    speed = 0

    def __init__(self,name,posx,posy):
        self.name = name
        self.posx = posx
        self.posy = posy

    def set_emoji_picture(self):
        self.picture = pygame.image.load('picture/emoji/' + self.name).convert_alpha()

    def draw_emoji(self,window):
        window.blit(self.picture, (self.posx, self.posy))

class Racer:
    posx = 0 # hoanh do cua vat
    posy = 0  #tung do cua vat
    speed = DEFINE.firstspeed #toc do cua vat
    type_racer = "NULL" # loai cua nhan vat dua, (co the la xe hoi, may bay,..)
    color = 0 # mau cua cac vat the dua
    picture = None  # cai nay dung de ve cac hinh anh, noi chung khong can de y den cai nay dau ahihi
    bua = [] #cai list nay dung de chua bua ma xe gap phai
    emoji = None # cai nay phuc vu cho viec bieu cam
    change = 0 #cai nay phuc vu cho viec an mung cua xe, khong can quan tam gi nhieu

    FinalRank = 0
    name =""
    width = 0
    height = 0

    def set_picture(self):
        if(self.type_racer == 'PJTeam'):
            picture = pygame.image.load('picture/TurtleObject/'+str(self.type_racer) + "/" + self.fix+str(self.color - 101)+'.png').convert_alpha()
        else:
            picture = pygame.image.load('picture/TurtleObject/'+str(self.type_racer) + "/" + str(self.type_racer)+str(self.color)+'.png').convert_alpha()
        self.picture = picture


    def __init__(self, x_hoanhdo, y_tungdo, type_racer, color  , name, fix):  # cai bien cuoi cung dung de fix loi duong dan neu la PITeam
        self.posx = x_hoanhdo
        self.posy = y_tungdo
        self.type_racer = type_racer
        self.color = color
        self.name = name
        self.fix = fix
        if(type_racer == "TRUCK"):
            self.width = DEFINE.TRUCK_width
            self.height = DEFINE.TRUCK_height
        elif (type_racer == "CAR"):
            self.width = DEFINE.CAR_width
            self.height = DEFINE.CAR_height
        elif (type_racer == "SUPER"):
            self.width = DEFINE.SUPER_width
            self.height = DEFINE.SUPER_height
        elif (type_racer == "TANK"):
            self.width = DEFINE.TANK_width
            self.height = DEFINE.TANK_height
        elif (type_racer == "FUTURE_CAR"):
            self.width = DEFINE.FUTURE_CAR_width
            self.height = DEFINE.FUTURE_CAR_height
        elif (type_racer == "FUTURISTIC_TRUCK"):
            self.width = DEFINE.FUTURISTIC_TRUCK_width
            self.height = DEFINE.FUTURISTIC_TRUCK_height
        elif (type_racer == "PJTeam"):
            self.width = DEFINE.PJTeam_width
            self.height = DEFINE.PJTeam_height

        #cai nay dung de tao lo hong khong gian
        self.x_left = self.width
        self.x_right = 0
        self.davedich = False


    def drawCar(self, window,x_left = 0, x_right = DEFINE.CAR_width): #chieu dai dung de ve mot phan cua racer, cai nay phuc vu cho viec tao lo hong
        window.blit(self.picture, (self.posx, self.posy),(x_left,0,x_right,self.height))


