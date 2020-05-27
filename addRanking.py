
import pygame
import DEFINE
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

button_text_font = pygame.font.SysFont('arial', 20)
MINIGAME = 273
EXIT = 115
NOTEXIT = 116
textcolor = (0, 0, 0)
BACK = 99


def text_object(text, font, text_color):
    text_surface = font.render(text, True, text_color)
    return text_surface, text_surface.get_rect()

def button(display_surface,text ,x, y, width, height, color, highlight_color,colortext, function = None):
    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()
    output_number = 0

    if (x < mouse[0] < x + width) and (y < mouse[1] < y + height):
        pygame.draw.rect(display_surface, highlight_color, (x, y, width, height))

        if clicked[0] == 1 and function != None:
            output_number = function

    else:
        pygame.draw.rect(display_surface, color, (x, y, width, height))
    textSurf, textRect = text_object(text, button_text_font, colortext)
    textRect.center = (x + (width / 2), y + (height / 2))
    display_surface.blit(textSurf, textRect)
    return output_number

class Button:
    posx = 0
    posy = 0
    width = 10
    height = 10
    color = (20, 200, 200)

    def Setup(self, posx, posy, width, height, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.posx, self.posy, self.width, self.height))
    def drawTempSet(self, window, color, posx, posy, width, height):
        pygame.draw.rect(window, color, (posx, posy, width, height))
    def check(self, coord):
        if coord[0] >= self.posx and coord[0] <= self.posx + self.width:
            if coord[1] >= self.posy and coord[1] <= self.posy + self.height:
                return 1
        return 0

def drawTimeRankBoard(window, boardposx, boardposy, carlist, numcar, maincarID, betmoney):
    #yeu cau de ham hoat dong dung:
    # Class xe phai co thuoc tinh FinalRank la thu tu xep hang cuoi cung cua xe
    # Neu co xe da ve dich thi phai dam bao da lam xong cong viec gan cho FinalRank ben ngoai ham nay
    monn = [1, -0.25, -0.5, -0.75, -1]
    rl = []
    stroke = 2
    patterncolor = (235, 235, 10)
    textcolor = (10, 10, 10)
    textunderbutton = 2
    boardWidth = 200
    boardHeight = 100
    pieceHeight = boardHeight/numcar
    for i in range(0, numcar, 1):
        rl.append(i)
    for i in range(0, numcar-1, 1):
        for j in range(i + 1, numcar, 1):
            if (carlist[rl[i]].FinalRank > carlist[rl[j]].FinalRank) and (carlist[rl[j]].FinalRank > 0) or (
                    carlist[rl[i]].posx < carlist[rl[j]].posx) and (carlist[rl[i]].FinalRank <= 0):
                temp = rl[i]
                rl[i] = rl[j]
                rl[j] = temp
    rankMainCar = 0
    for i in range(0, numcar, 1):
        if rl[i] == maincarID:
            rankMainCar = i
            break

    #setup font
    font = pygame.font.SysFont("Stencil, Time New Romans", int(pieceHeight*0.75))
    text = font.render("Now Ranking", True, textcolor)
    window.blit(text, (boardposx, boardposy))
    #draw part
    fence = 15
    for i in range(0, numcar, 1):
        pygame.draw.rect(window, patterncolor, (boardposx, boardposy + (i + 1)*(pieceHeight + stroke), fence, pieceHeight))
        pygame.draw.rect(window, patterncolor, (boardposx + fence + 2, boardposy + (i + 1)*(pieceHeight + stroke), boardWidth - (fence + 2), pieceHeight))
        text = font.render(str(i+1) + "  " + carlist[rl[i]].name, True, textcolor)
        window.blit(text, (boardposx + stroke, boardposy + (i + 1)*(pieceHeight + stroke) + textunderbutton))

    betmoneycolor = (150, 50, 200)
    fence = 130
    pygame.draw.rect(window, betmoneycolor, (boardposx, boardposy + (numcar + 1)*(pieceHeight + stroke), fence, pieceHeight))
    text = font.render("Account change", True, textcolor)
    window.blit(text, (boardposx, boardposy + (numcar + 1)*(pieceHeight + stroke) + textunderbutton))
    pygame.draw.rect(window, betmoneycolor, (boardposx + (fence + 2), boardposy + (numcar + 1)*(pieceHeight + stroke), boardWidth - (fence + 2), pieceHeight))
    if betmoney*monn[rankMainCar] < 0:
        text = font.render("-$" + str(-(int(betmoney * monn[rankMainCar]))), True, textcolor)
    else:
        text = font.render('+$' + str(int(betmoney * monn[rankMainCar])), True, textcolor)
    window.blit(text, (boardposx + fence + 5, boardposy + (numcar + 1)*(pieceHeight + stroke) + textunderbutton))

def ask_to_minigame(display_surface,SCREEN_WIDTH = 800, SCREEN_HEIGHT = 600):
    stroke = 3
    strokecolor = blue
    backgroundcolor = green
    startfrmid = -100
    btempwidth = 40
    exit_ask_box = button(display_surface,"Your money had run out!", SCREEN_WIDTH/2+50, SCREEN_HEIGHT/2+startfrmid, 300, btempwidth, backgroundcolor, backgroundcolor,black)
    exit_ask_box = button(display_surface,"Do you want to play mini-game", SCREEN_WIDTH/2+50, SCREEN_HEIGHT/2+startfrmid+1*btempwidth, 300, btempwidth, backgroundcolor, backgroundcolor,black)
    exit_ask_box = button(display_surface,"to raise your money again,", SCREEN_WIDTH/2+50, SCREEN_HEIGHT/2+startfrmid+2*btempwidth, 300, btempwidth, backgroundcolor, backgroundcolor,black)
    exit_ask_box = button(display_surface,"or you want to exit?", SCREEN_WIDTH/2+50, SCREEN_HEIGHT/2+startfrmid+3*btempwidth, 300, btempwidth, backgroundcolor, backgroundcolor,black)


    button_width = 140- stroke
    button_height = 40
    distance = 20
    startx = SCREEN_WIDTH/2 + 50 + stroke# - button_width - distance/2
    starty = SCREEN_HEIGHT/2 + startfrmid+4*btempwidth + stroke+ 20
    key = "minigame"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key = "minigame"
                elif event.key == pygame.K_RIGHT:
                    key = "exit"
                elif event.key == pygame.K_KP_ENTER or event.key == 13:
                    if key == "exit":
                        pygame.quit()
                        quit()
                    else:
                        return DEFINE.MINIGAME

        mousepress = pygame.mouse.get_pressed()
        if key == "minigame":
            pygame.draw.rect(display_surface, strokecolor, (startx - stroke, starty - stroke, button_width + 2*stroke, button_height + 2*stroke))
            pygame.draw.rect(display_surface, backgroundcolor,
                             (startx + button_width + distance - stroke, starty - stroke, button_width + 2 * stroke, button_height + 2 * stroke))

        if key == "exit":
            pygame.draw.rect(display_surface, backgroundcolor, (startx - stroke, starty - stroke, button_width + 2*stroke, button_height + 2*stroke))
            pygame.draw.rect(display_surface, strokecolor,
                             (startx + button_width + distance - stroke, starty - stroke, button_width + 2 * stroke, button_height + 2 * stroke))
        res = button(display_surface,"Play mini-game", startx, starty, button_width, button_height, darkgreen, lightgreen,black, DEFINE.MINIGAME)
        if res == DEFINE.MINIGAME:
            return res
        res = button(display_surface,"Exit", startx + button_width + distance, starty, button_width, button_height, darkgreen, lightgreen,black, EXIT)
        if res == EXIT:
            pygame.quit()
            quit()
        pygame.display.update()

def FinalRankingScreen(window, carlist, numcar, maincarID, betmoney, totalAccount):
    monn = [1, -0.25, -0.5, -0.75, -1]
    runout_money = 0
    isRunout = 0
    rl = []
    for i in range(0, numcar, 1):
        rl.append(i)
    for i in range(0, numcar-1, 1):
        for j in range(i + 1, numcar, 1):
            if (carlist[rl[i]].FinalRank > carlist[rl[j]].FinalRank) and (carlist[rl[j]].FinalRank > 0) or (
                    carlist[rl[i]].posx < carlist[rl[j]].posx) and (carlist[rl[i]].FinalRank <= 0):
                temp = rl[i]
                rl[i] = rl[j]
                rl[j] = temp
    rankMainCar = 0
    for i in range(0, numcar, 1):
        if rl[i] == maincarID:
            rankMainCar = i
            break
    totalAccount += monn[rankMainCar]*betmoney
    isRunout = 0
    if totalAccount < runout_money:
        isRunout = 1

    #draw part
    textcolor = (10, 10, 10)
    textunderbutton = 10
    boardposx = 50
    boardposy = 50
    boardWidth = 800 - 2*boardposx
    boardHeight = 600 - 2*boardposy
    pygame.draw.rect(window, (140, 50, 140), (boardposx, boardposy, boardWidth, boardHeight))

    namepopup = Button()
    namepopup.Setup(boardposx, boardposy, boardWidth, 70, (30, 200, 250))
    namepopup.draw(window)
    bigfont = pygame.font.SysFont("Goudy Stout, Time New Romans", 50)
    text = bigfont.render("Ranking", True, textcolor)
    window.blit(text, (namepopup.posx + 10, namepopup.posy + textunderbutton))

    boardposx = 60
    boardposy = 150
    boardWidth = 350
    boardHeight = 200
    patterncolor = (90, 235, 100)
    stroke = 10

    pieceHeight = boardHeight/numcar
    #setup font
    font = pygame.font.SysFont("Stencil, Magneto, Time New Romans", int(pieceHeight * 0.75))
    text = font.render("Result", True, textcolor)
    window.blit(text, (boardposx, boardposy))

    font = pygame.font.SysFont("Stencil, Time New Romans", int(pieceHeight * 0.75))

    fence = 40
    for i in range(0, numcar, 1):
        pygame.draw.rect(window, patterncolor,
                         (boardposx, boardposy + (i + 1) * (pieceHeight + stroke), fence, pieceHeight))
        pygame.draw.rect(window, patterncolor,
                         (boardposx + fence + 2, boardposy + (i + 1) * (pieceHeight + stroke), boardWidth - (fence + 2), pieceHeight))
        text = font.render(str(i + 1) + "  " + carlist[rl[i]].name, True, textcolor)
        window.blit(text, (boardposx + stroke, boardposy + (i + 1) * (pieceHeight + stroke) + 5))

    moneyChangeBtn = Button()
    moneyChangeBtn.Setup(60, 450, 388, 60, (10, 250, 20))
    moneyChangeBtn.draw(window)
    if betmoney*monn[rankMainCar] < 0:
        text = font.render("Account change: -$" + str(-int(betmoney * monn[rankMainCar])), True, textcolor)
    else:
        text = font.render('Account change: +$' + str(betmoney * monn[rankMainCar]), True, textcolor)
    window.blit(text, (moneyChangeBtn.posx + 2, moneyChangeBtn.posy + textunderbutton))

    font = pygame.font.SysFont("Forte, Time New Romans", int(pieceHeight * 0.75))
    btnHistory = Button()
    historyText = font.render("History", True, textcolor)
    btnHistory.Setup(450, 200, 280, 60, (5, 230, 20))
    #btnHistory.draw(window)
    #window.blit(historyText, (btnHistory.posx + 5, btnHistory.posy + textunderbutton))

    btnContinuePlay = Button()
    continueText = font.render("Continue Play", True, textcolor)
    btnContinuePlay.Setup(450, 300, 280, 60, (5, 230, 20))
    #btnContinuePlay.draw(window)
    #window.blit(continueText, (btnContinuePlay.posx + 5, btnContinuePlay.posy + textunderbutton))

    btnToMainScreen = Button()
    toMainText = font.render("Go to main screen", True, textcolor)
    btnToMainScreen.Setup(450, 400, 280, 60, (5, 230, 20))
    #btnToMainScreen.draw(window)
    #window.blit(toMainText, (btnToMainScreen.posx + 5, btnToMainScreen.posy + textunderbutton))
    #pygame.display.update()

    running = 1
    click = 0
    if isRunout==0:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = 1
            mousex, mousey = pygame.mouse.get_pos()

            if btnHistory.check((mousex, mousey)):
                btnHistory.drawTempSet(window, (20, 50, 200), btnHistory.posx, btnHistory.posy, btnHistory.width, btnHistory.height)
                if click:
                    return 1
            else:
                btnHistory.draw(window)
            window.blit(historyText, (btnHistory.posx + 5, btnHistory.posy + textunderbutton))
            if btnContinuePlay.check((mousex, mousey)):
                btnContinuePlay.drawTempSet(window, (20, 50, 200), btnContinuePlay.posx, btnContinuePlay.posy, btnContinuePlay.width, btnContinuePlay.height)
                if click:
                    return 2
            else:
                btnContinuePlay.draw(window)
            window.blit(continueText, (btnContinuePlay.posx + 5, btnContinuePlay.posy + textunderbutton))
            if btnToMainScreen.check((mousex, mousey)):
                btnToMainScreen.drawTempSet(window, (20, 50, 200), btnToMainScreen.posx, btnToMainScreen.posy, btnToMainScreen.width, btnToMainScreen.height)
                if click:
                    return 3
            else:
                btnToMainScreen.draw(window)
            window.blit(toMainText, (btnToMainScreen.posx + 5, btnToMainScreen.posy + textunderbutton))

            pygame.display.update()
    else:
        temp = ask_to_minigame(window)
        return temp