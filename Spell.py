# day la file chua class bua
import random, pygame, DEFINE


class Spell:
    posx = 0  # hoanh do cua cac bua
    road = 0  # vi tri duong cua cac bua
    type = 0  # loai bua

    list_hinhanh_congkhonggian = [] # cai nay chi danh cho bua ve dich va ve vach xuat phat
    picture = None

    def __init__(self, type, x, road):
        self.road = road
        self.type = type
        self.posx = x

        #cai nay chi dung cho viec debug
        if(type == DEFINE.VE_VACHXUATPHAT or type == DEFINE.VE_DICH):
            self.set_listkhonggian()
        else:
            self.set_picture()

    def set_listkhonggian(self):
        l = []
        for i in range(0, 15):
            l.append(pygame.image.load("picture/hole/h" + str(i + 1) + ".png").convert_alpha())

        if (self.type == DEFINE.VE_VACHXUATPHAT or self.type == DEFINE.VE_DICH):
            self.list_hinhanh_congkhonggian = l

    def set_picture(self):
        if (self.type == DEFINE.TANG_TOC):
            self.picture = pygame.image.load("picture/spellicon/speed.png").convert_alpha()
        elif (self.type == DEFINE.DUNG_LAI):
            self.picture = pygame.image.load("picture/spellicon/stop.png").convert_alpha()
        elif (self.type == DEFINE.QUAY_DAU):
            self.picture = pygame.image.load("picture/spellicon/turnback.png").convert_alpha()





    # Set random from the start to avoid redundancy
    def set_type(self):
        rand = random.randint(1, 100)
        if 0 < rand < 6:  # 5 chances out of 100  (1 <= rand <= 5)
            self.type = DEFINE.VE_DICH
        if 5 < rand < 11:  # 5 chances out of 100  (6 <= rand <= 10)
            self.type = DEFINE.VE_VACHXUATPHAT
        if 10 < rand < 46:  # 35 chances out of 100 (11 <= rand <= 45)
            self.type = DEFINE.TANG_TOC
        if 45 < rand < 81:  # 35 chances out of 100 (46 <= rand <= 80)
            self.type = DEFINE.DUNG_LAI
        if 80 < rand < 101:  # 20 chances out of 100 (81 <= rand <= 100)
            self.type = DEFINE.QUAY_DAU

    def draw_spell(self, window, road_width, road_start_y,i):
        # road_start_y+(self.road+0.5)*road_width
        if(  self.type == DEFINE.VE_DICH or self.type == DEFINE.VE_VACHXUATPHAT ):
            window.blit(self.list_hinhanh_congkhonggian[i],(self.posx - 123/2 ,road_start_y + road_width / 5 * self.road - 126/3.5))
        else:
            window.blit(self.picture,(self.posx, road_start_y + road_width / 5 * (self.road + 0.5)-15))



# Update 01/04/2019 9:01 PM


#   Tao list bua cua CAC LAN DUONG
#   Tao list bua cua CAC LAN DUONG
def createListSpell(lanes, start_line_x, finish_line_x):
    # Giai thich ten bien:
    #   lanes:          so luong lan duong
    #   start_line_x:   Vi tri vach xuat phat
    #   finish_line_x:  Vi tri vach dich

    # Cac gia tri co the chinh sua ma khong anh huong logic:

    limit = [0, 25000, 50000, 100000]  # Cac muc ma neu do dai quang duong vuot qua thi se co so luong bua tuong ung
    spell_for_limit = [5, 6, 7, 8]  # So luong bua tuong ung voi muc do dai
    buffer = 120
    # Nhung dong sau comment nay khong nen chinh sua
    road_length = finish_line_x - start_line_x
    newList = []
    current_limit = len(limit) - 1  # Muc dang xet
    # Xet tu muc cao nhat xuong, neu do dai quang duong vuot qua muc do thi se co so luong bua tuong ung o moi lan duong

    while current_limit >= 0:
        if road_length > limit[current_limit]:
            spells = spell_for_limit[current_limit]
            break
        current_limit -= 1
    start_x = start_line_x
    spell_range = int((road_length - start_x) / spells - buffer)

    for i in range(lanes):
        start_x = start_line_x + buffer
        spell_in_lane = []
        for j in range(spells):
            new_spell = Spell(0, 0, 0)
            new_spell.set_type()
            # Dieu kien
            if (j < spells - 1):
                while new_spell.type == DEFINE.VE_DICH:
                    new_spell.set_type()
            if (j > 0):
                while new_spell.type == DEFINE.VE_VACHXUATPHAT:
                    new_spell.set_type()

            new_spell.posx = (start_x + random.randint(0, spell_range))
            new_spell.road = i
            new_spell.set_listkhonggian()
            spell_in_lane.append(new_spell)
            # Nhay vi tri bat dau khoang tiep
            start_x += spell_range + buffer
            new_spell.set_picture()
        newList.append(spell_in_lane)

    return newList