"""File nay chua cac ham ve cac vat the nhu: cay, duong, via he, vach xuat phat, vach dich,..."""

import pygame
# ve cay
def draw_tree(win,x, y):
    x = int(x)
    y = int(y)
    # tree trunk (50 wide and 100 tall)
    pygame.draw.rect(win, (117, 90, 0), (x, y - 100, 50, 100))
    # leaves are a circle
    pygame.draw.circle(win, (27, 117, 0), (x + 25, y - 120), 50)

# v? ???ng
def draw_road(win,road_start_y, road_width):  # Hi?uTr?n
    # road_start_y v? tr� b?t ??u c?a ph?n ???ng ?ua t? tr�n xu?ng
    # width l� ?? r?ng c?a ???ng ?ua
    pygame.draw.rect(win, (109, 107, 107), (0, road_start_y, pygame.display.get_surface().get_width(), road_width))


# v? v?ch xu?t ph�t
def draw_start_line(win,road_start_y, road_width, start_x, x_width):
    # road_start_y v? tr� b?t ??u c?a ph?n ???ng ?ua t? tr�n xu?ng
    # start_x l� v? tr� b?t ??u v? theo tr?c x
    # road_width l� ?? r?ng c?a ???ng ?ua
    # width l� ?? r?ng v?ch ?en, v?ch tr?ng r?ng b?ng 3/5 v?ch ?en
    pygame.draw.rect(win, (0, 0, 0), (start_x, road_start_y, x_width, road_width))
    pygame.draw.rect(win, (255, 255, 255), ((start_x + x_width), road_start_y, x_width * 3 / 5, road_width))


# v? v?ch ph�n chia c�c l�n ???ng
def draw_line(win,road_start_y, road_width, road_length, line_width):  # Hi?uTr?n
    # road_start_y l� v? tr� b?t ??u c?a ???ng ?ua t? tr�n xu?ng
    # road_width l� ?? r�ng c?a ???ng ?ua
    # road_length l� ?? d�i ???ng ?ua
    # width l� ?? r?ng c?a v?ch
    # v? ???ng ranh gi?i gi?a c�c l�n ???ng
    for a in range(1, 5):
        pygame.draw.rect(win, (243, 121, 20), (0, road_start_y + road_width * a / 5, road_length, line_width))


# v? c�c v?ch gi?a ???ng
def draw_midline(win,road_start_y, road_width, road_length, road_start_x, this_height, this_width, distance):  # Hi?uTr?n
    # road_start_y l� v? tr� b?t ??u c?a ???ng t? tr�n xu?ng
    # road_length l� ?? d�i ???ng ?ua
    # road_width l� ?? r�ng ???ng ?ua
    # width l� ?? r?ng c?a v?ch
    # length l� ?? d�i c?a v?ch
    # distance l� kho?ng c�ch t? ??u v?ch n�y ??n ??u v?ch k? ti?p (distance > length)
    # count l� s? l?n l?p l?i c?a v?ch gi?a ???ng trong 1 l�n ???ng
    countend = int(pygame.display.get_surface().get_width() / (this_width + distance) + 4)  # so vach trong man hinh in ra
    # countend = int(road_length/(this_width + distance) + 2)
    if road_start_x < 0:
        countbegin = int(-road_start_x / (this_width + distance))  # so vach ngoai man hinh khong in ra
    else:
        countbegin = int(road_start_x / (this_width + distance))
    startposx = road_start_x + (countbegin - 1) * (this_width + distance)
    # v? v?ch gi?a ???ng cho 5 l�n ???ng
    for a in range(0, 5):
        # v? v?ch gi?a ???ng cho m?i l�n ???ng
        for b in range(0, countend):
            pygame.draw.rect(win, (255, 255, 255), (
            startposx + b * (this_width + distance), road_start_y + (2 * a + 1) / 10 * road_width - this_height / 2,
            this_width, this_height))


def VeViaHe(window, ToaDoBatDauX, ToaDoY, ChieuDai, DoDay):
    # window la man hinh dung de in vach nay ra
    # ToaDoBatDauX muc dich de khi cho toa do nay am giam dan thi cac vach se tu dong chay lui lai
    # ToaDoY la toa do Y phia tren cua vach
    # ChieuDai tinh theo phuong X
    # DoDay tinh theo phuong Y
    PixelPerTurn = 40  # do dai cua moi vach tinh bang pixel
    slope = 10  # do nghieng cua cac vach
    color = [(255, 51, 51), (255, 255, 0)]  # hai mau luan phien [cam, trang]
    turn = 0  # luot chon mau
    for posx in range(int(ToaDoBatDauX), int(ChieuDai), PixelPerTurn):
        pygame.draw.polygon(window, color[turn], [(posx, ToaDoY), (posx + PixelPerTurn, ToaDoY),
                                                  (posx + PixelPerTurn - slope, ToaDoY + DoDay),
                                                  (posx - slope, ToaDoY + DoDay)])
        turn = 1 - turn


def draw_goal(win,x, y, height):  # Hieuphanlong
    # x: ho�nh ?? ?�ch
    # y: tung ?? ?�ch
    # height : chi?u cao ?�ch
    a = (height % 20) / 2
    # b = (height - 2 * a) / 20
    b = int(height / 20)
    ngang = int(height * 0.3)
    c = ngang * 7 / 60

    pygame.draw.rect(win, (109, 107, 107), (x, y, c + ngang * 13 / 15, height))
    # thanhdoc ban dau
    pygame.draw.rect(win, (255, 255, 255), (x, y, c, height))
    # thanh doc 1
    pygame.draw.rect(win, (0, 0, 0), (x + c, y, ngang / 12, height))

    for i in range(10):
        pygame.draw.rect(win, (255, 255, 255), (x + ngang * 0.2, y + a + b * 2 * i, ngang * 0.4, b))
        pygame.draw.rect(win, (0, 0, 0), (x + ngang * 0.5, y + a + b + b * 2 * i, ngang * 0.4, b))
    # for i in range(10):
    #     pygame.draw.rect(win, (0, 0, 0), (x + ngang*0.5, y + a + b + b * 2 * i, ngang * 0.4, b))

    pygame.draw.rect(win, (255, 255, 255), (x + ngang * 0.9, y, ngang / 12, height))

    # ve 2 thanh ben duoi
    pygame.draw.rect(win, (0, 0, 0), (x + c, y, ngang * 13 / 15, a))
    pygame.draw.rect(win, (255, 255, 255), (x + c, y + height - a, ngang * 13 / 15, a))