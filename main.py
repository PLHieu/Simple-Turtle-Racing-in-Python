# -*- coding: utf-8 -*-
import pygame, settings_racers, mainmenu, help_exit_about, history, settings_AdjustLength,betmoney_chooseRacer
import startingRacing,map_menu, set_screen, DEFINE, MiniGame

pygame.init()
pygame.mixer.init()
display_surface = pygame.display.set_mode((800, 600))

#cac bien cho game
settings_game =  ["SUPER", [101,108,106,104,102], ["LittleZeros","Gorilla","HappyMan","Chocopie","FunGirl"]]

first_time_log_in  = True
taikhoan = 0
tiencuoc = 0
passSpell_active = False
name_player = ""  #ten nguoi choi
maincar = 2  #so thu tu cua xe chinh
HistoryList = history.History_List()  #lich su thi dau
settings_length = 2500  # do dai quang duong
map = 1  # so thu tu cua map
run  = True
mn = 0
menu_music = "sounds/this_is_it.mp3"
sound = False
screensize = 0 # 0 la nho



HistoryList.add(0, 0, 0, 0, 0, new_account = taikhoan)

while(run):
    if not sound:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(menu_music)
        pygame.mixer.music.play(-1)
        sound = True
    if (mn == 0):
        mn = mainmenu.game_menu()

    if mn == 999:  # start game
        a, maincar, tiencuoc, name_player, taikhoan,first_time_log_in, passSpell_active = betmoney_chooseRacer.startgame(settings_game, taikhoan, first_time_log_in, name_player,passSpell_active)
        if (a == 482000):
            # goi ham bat dau dua xe
            b, taikhoan = startingRacing.racing_running(display_surface, settings_game, maincar, int(tiencuoc), name_player,
                                                HistoryList,settings_length,map, taikhoan,passSpell_active)
            if (b == 1):  # nguoi dung chon  vao lich su
                mn = -999
            elif (b == 2): # nguoi dung chon choi tiep
                mn = 999
            elif (b == DEFINE.MINIGAME):  # nguoi dung chon choi minigame
                choiminigame =  MiniGame.game_loop()
                taikhoan += choiminigame
                HistoryList.add(0, 0,choiminigame , 0, 0, new_account =  taikhoan)
                mn = 999
            elif (b == 115 or b == 3): # nguoi dung chon exit, vay thi quay lai menu chinh
                mn = 0
            # To restart menu music
            sound = False
        elif (a == 73):
            choiminigame = MiniGame.game_loop()
            taikhoan += choiminigame
            HistoryList.add(0, 0, choiminigame, 0, 0, new_account=taikhoan)
        elif (a == 999):  # neu nhu nguoi  dung nhan back trong man hinh ca cuoc xe
            mn = 0

    elif mn == 768:  # settings
        mn_setting = True
        while (mn_setting):
            a = mainmenu.settings_menu()

            if a == 420:  # racer
                settings_game = settings_racers.Racer_settings(display_surface,settings_game)

            elif a == 911:
                settings_length = settings_AdjustLength.ROAD_LENGTH(display_surface)

            elif a == 4000:
                screensize = set_screen.main_set_screen_size(display_surface)
                if(screensize == 200):
                    display_surface = pygame.display.set_mode((800, 600))
                else:
                    display_surface = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)

            elif a == 304:
                map = map_menu.map_menu()

            elif a == 555:  # back
                mn_setting = False
        mn = 0

    elif mn == -999:  # history
        a = history.History_board(HistoryList)
        if (a == 0):
            mn = 0

    elif mn == 101:  # help
        a = help_exit_about.Help_board(display_surface, pygame.display.get_surface().get_width(),
                                 pygame.display.get_surface().get_height())
        if (a == 99):
            mn = 0

    elif mn == 113:  # about
        a = help_exit_about.Info_board(display_surface, pygame.display.get_surface().get_width(),
                                 pygame.display.get_surface().get_height())
        if (a == 99):
            mn = 0

    elif mn == 115:  # exit
        a = help_exit_about.exitfunc(display_surface, pygame.display.get_surface().get_width(),
                               pygame.display.get_surface().get_height())
        if (a == 115):  # neu nhu exit
            run = False
        elif (a == 116):
            mn = 0



