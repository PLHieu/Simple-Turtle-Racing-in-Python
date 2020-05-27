import pygame

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

def Help_board(display_surface,SCREEN_WIDTH,SCREEN_HEIGHT):
    font = pygame.font.SysFont("Goudy Stout, Arial", 56)

    border = 30
    ystartboard = 3 * border

    boardheight = SCREEN_HEIGHT - 6 * border


    back_button_width = 100
    back_button_height = 50
    back_button_startx = SCREEN_WIDTH*0.45
    back_button_starty = ystartboard + boardheight + 10

    running = 1

    a = pygame.image.load("picture/background/menu_backgroundsettings.png")
    display_surface.blit(a,(0,0))

    b = pygame.image.load("picture/help.png")
    display_surface.blit(b, (0, -40))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 1 - exitfunc()

        back_button = button(display_surface,"Back", back_button_startx, back_button_starty, back_button_width, back_button_height, white, (220,220,220),black, BACK)
        if back_button == BACK:
            return back_button
        pygame.display.update()

    return back_button

def exitfunc(display_surface,SCREEN_WIDTH,SCREEN_HEIGHT):
    stroke = 3
    strokecolor = blue
    backgroundcolor = green
    exit_ask_box = button(display_surface,"Are you sure you want to exit?", SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2-70, 300, 150, backgroundcolor, backgroundcolor,black)

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
        res = button(display_surface,"Yes", startx, starty, button_width, button_height, darkgreen, lightgreen,black, EXIT)
        if res == EXIT:
            return res
        res = button(display_surface,"No", startx + button_width + distance, starty, button_width, button_height, darkgreen, lightgreen,black, NOTEXIT)
        if res == NOTEXIT:
            return res
        pygame.display.update((SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2-70, 300, 150))

def Info_board(display_surface,SCREEN_WIDTH,SCREEN_HEIGHT):
    # Background
    info_background = pygame.image.load("picture/background/about.png")
    font = pygame.font.SysFont("Goudy Stout, Arial", 56)
    title_surface, title_Rect = text_object("About", font, black)

    font = pygame.font.SysFont("Comic Sans, Arial", 21, True)
    helptext = [
                ["Project Turtle Race", "Group 20"],
                ["Project manager:",  "              Hieu Phan Long",
                 "Business Analyst:", "              Tran Van Hieu",
                 "Developer:", "              Hieu Phan Long",
                               "              Tran Trung Hau",
                               "              Le Nguyen Hao",
                               "              Tran Van Hieu",
                               "              Huynh Van Hien",
                 "Designer:",  "              Le Nguyen Hao",
                 "Tester:",    "              Tran Trung Hau", "              Huynh Van Hien"],
                ["Truck, minivan, car images designed by macrovector on www.freepik.com",
                 "Music provided by freecommercialmusic.com",
                 "emoji images provided on www.freepik.com"]
                ]
    numparagraph = 3
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
    # pygame.draw.rect(display_surface, green, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    display_surface.blit(info_background, (0, 0))
    pygame.draw.rect(display_surface, (21, 255, 225), (border, border, SCREEN_WIDTH-2*border, SCREEN_HEIGHT-2*border))
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
            pygame.draw.rect(display_surface, white, (xstartboard, ystartboard, boardwidth, boardheight))
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
        mouse_press = button(display_surface,"", xstartboard + boardwidth - scroll_width, ystartboard + hold_mouse_down,
                             scroll_width, scroll_height, gray, lightgray,white, 1)
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

        back_button = button(display_surface,"Back", back_button_startx, back_button_starty, back_button_width, back_button_height, black, grey,white, BACK)
        if back_button == BACK:
            return back_button
        pygame.display.update((back_button_startx, back_button_starty, back_button_width, back_button_height))

    return back_button