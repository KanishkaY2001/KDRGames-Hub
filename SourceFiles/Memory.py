# Importing Modules
import pygame
import time
import random
import threading
import sys
from random import shuffle

pygame.init()

# Creates a Window
width = 1100
height = 605
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mind Shaper')

# Background Images
sunset = pygame.image.load("DataFile/IMAGES/SUNSET_.png")                     # Selection Screen
Space = pygame.image.load("DataFile/IMAGES/OuterSpace.png")                   # Easy mode Screen
table = pygame.image.load("DataFile/IMAGES/medium_mode_bg.png")               # Medium mode Screen
maths_background = pygame.image.load("DataFile/IMAGES/maths background.png")  # Hard mode Screen

# Easy, Meduim, Hard Buttons for Selection Screen
# Contains 2 same sized button but different colour to create an allusion of a button.
EASY_button = pygame.image.load("DataFile/IMAGES/EASY1.png")
EASY_button2 = pygame.image.load("DataFile/IMAGES/EASY2.png")
medium_button = pygame.image.load("DataFile/IMAGES/meduim button.png")
medium_button2 = pygame.image.load("DataFile/IMAGES/meduim button2.png")
hard_button = pygame.image.load("DataFile/IMAGES/hard_button.png")
hard_button2 = pygame.image.load("DataFile/IMAGES/hard_button2.png")

# Highlights Boxes/Tiles
highlight = pygame.image.load("DataFile/IMAGES/hover.png")                    # Used in Easy mode
highlight = pygame.transform.scale(highlight, (175, 150))
highlight_med = pygame.image.load("DataFile/IMAGES/highlight_med.png")        # Used in Medium mode
highlight_hard = pygame.image.load("DataFile/IMAGES/hardmode highlight.png")  # Used in Hard mode

congratsEasy = pygame.image.load("DataFile/IMAGES/Congrats Easy Mode.png")
table2 = pygame.image.load("DataFile/IMAGES/transparent bg.png")              # Background gets Dull
congratsEasyretry = pygame.image.load("DataFile/IMAGES/Congrats Easy Mode retry.png")
congratsEasyhome = pygame.image.load("DataFile/IMAGES/Congrats Easy Mode home.png")

bridgegate = pygame.image.load("DataFile/IMAGES/Bridge Door.png")
bridgegate2 = pygame.image.load("DataFile/IMAGES/Bridge Door2.png")


#Home and Retry Button that allows a user to quit or retry their current mode anytime.
homebutton = pygame.image.load("DataFile/IMAGES/menu.png")
homebutton2 = pygame.image.load("DataFile/IMAGES/menu2.png")
retrybutton = pygame.image.load("DataFile/IMAGES/retry.png")
retrybutton2 = pygame.image.load("DataFile/IMAGES/retry2.png")

# Loads all the Emojis and stores it in a list, which will be used in "Easy mode Screen".
multi_images = []
for i in range(4):
    emoji = pygame.image.load("DataFile/IMAGES/Emoji_" + str(i) + ".png")
    emoji = pygame.transform.scale(emoji, (100, 100))
    multi_images.append(emoji)
# Makes a copy of the loaded Emojis above and adds it into a new list.
multi_images_L1 = []
for i in multi_images:
    multi_images_L1.extend([i, i])

# Loads all the Fast Food images and stores it in a list, which will be used in "Medium mode Screen".
multi_junks = []
for i in range(15):
    junks = pygame.image.load("DataFile/IMAGES/junk_" + str(i) + '.png')
    multi_junks.append(junks)
# Makes a copy of the loaded Fast Food images above and adds it into a new list.
multi_junks_L2 = []
for i in multi_junks:
    multi_junks_L2.extend([i, i])

# Loads all the Shapes and stores it in a list, which will be used in "Hard mode Screen".
multi_shapes = []
for i in range(21):
    shapes = pygame.image.load("DataFile/IMAGES/Shape_" + str(i) + ".png")
    multi_shapes.append(shapes)
# Makes a copy of the loaded Shapes above and adds it into a new list example: [1,2,3,4] to [1,1,2,2,3,3,4,4].
multi_shapes_L2 = []
for i in multi_shapes:
    multi_shapes_L2.extend([i, i])

# Loads the Boxes/Tile for each mode
Box = pygame.image.load("DataFile/IMAGES/Box.png")                   # Easy mode
Box = pygame.transform.scale(Box, (175, 150))
boxh_1 = pygame.image.load("DataFile/IMAGES/box4.png")               # Medium mode
medium_box = pygame.image.load("DataFile/IMAGES/tile_medium.png")    # Hard mode

# Sets each and every Emoji as False.
angel_1,angel_2,angel_match,whatever_1,whatever_2,whatever_match,worried_1,worried_2,worried_match,cool_1,cool_2, cool_match  = (False,)*12

# Sets each and every Shapes as False.
rect_1, rect_2,rect_1A,rect_2A, hex_1, hex_2, hex_1A, hex_2A, star_1, star_2, star_1A, star_2A,circle_1, circle_2, circle_1A, circle_2A, triangle_1, triangle_2, triangle_1A, triangle_2A, opphex_1, opphex_2, opphex_1A, opphex_2A, oval_1, oval_2, oval_1A, oval_2A, heart_1, heart_2, heart_1A, heart_2A,commstar_1,commstar_2, commstar_1A, commstar_2A,splatpaint_1, splatpaint_2,splatpaint_1A,splatpaint_2A, square_1, square_2, rect_match, hex_match, star_match, circle_match, triangle_match, opphex_match, rect_Amatch, hex_Amatch,star_Amatch, circle_Amatch,triangle_Amatch, opphex_Amatch, oval_match, oval_Amatch, heart_match, heart_Amatch, commstar_match, commstar_Amatch, splatpaint_match,splatpaint_Amatch, square_match = (False,) * 63

# Sets each and every Fast Food images as False.
tacos_1, tacos_2, tacos_match, pizza_1, pizza_2 ,pizza_match, popcorn_1, popcorn_2, popcorn_match, burger_1, burger_2,burger_match, sandwich_1, sandwich_2,sandwich_match, cookies_1,cookies_2,cookies_match, icecream_1, icecream_2, icecream_match,  whitechoc_1, whitechoc_2,whitechoc_match, pancakecream_1,pancakecream_2, pancakecream_match, chips_1,chips_2, chips_match,fries_1,fries_2,fries_match,donut_1, donut_2, donut_match, drink_1,drink_2,drink_match, cupcake_1,cupcake_2,cupcake_match, hotdog_1, hotdog_2,hotdog_match = (False,) * 45

# Makes a list of coordinates/position where all the Emoji will be placed, in short rows and columns.
pos = []
for i in range(252, 872, 155):
    posx = ((i), 145)
    pos.append(posx)
    posy = ((i), 310)
    pos.append(posy)

# Makes a list of coordinates/position where all the Shapes will be placed, in short rows and columns.
pos2 = []
for i in range(242, 827, 95):
    pos_1line = ((i), 53)
    pos2.append(pos_1line)
    pos_2Line = ((i), 138)
    pos2.append(pos_2Line)
    pos_3Line = ((i), 223)
    pos2.append(pos_3Line)
    pos_4Line = ((i), 308)
    pos2.append(pos_4Line)
    pos_5Line = ((i), 393)
    pos2.append(pos_5Line)
    pos_6line = ((i), 478)
    pos2.append(pos_6line)

# Makes a list of coordinates/position where all the Fast Food images  will be placed, in short rows and columns.
pos3 = []
for i in range(250,850,100):
    pos_m = ((i), 40)
    pos3.append(pos_m)
    pos_m2 = ((i), 145)
    pos3.append(pos_m2)
    pos_m3 = ((i), 250)
    pos3.append(pos_m3)
    pos_m4 = ((i), 355)
    pos3.append(pos_m4)
    pos_m5 = ((i), 460)
    pos3.append(pos_m5)

initiate = 0    # Off (nothing is clicked # Easy_mode)
initiate_2 = 0  # Off (nothing is clicked # Hard_mode)
initiate_3 = 0  # Off (nothing is clicked # Medium_mode)
centery = (115)

canClick,canClick2,canClick3 = (True,) * 3
clock = pygame.time.Clock()
xs = 0
ys = 0
xe = ((width - 300) / 2)
ye = 100

def easybutton():
    # Easy Button function which is placed in the Selection Screen
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 400 <= mouse_x <= 700 and 100 <= mouse_y <= 200:
        display.blit(EASY_button2, (xe -5 , ye))
        if click[0] == 1:  # Checks if the left button of the mouse is clicked.
            easy_mode()    # Runs the Easy Mode function
    else:
        display.blit(EASY_button, (xe -5 , ye))

def MediumButton():
    # Medium Button function which is placed in the Selection Screen
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 400 <= mouse_x <= 700 and 250 <= mouse_y <= 400:
        display.blit(medium_button, (xe - 5, 250))
        if click[0] == 1:   # Checks if the left button of the mouse is clicked.
            medium_mode()   # Runs the Medium Mode function
    else:
        display.blit(medium_button2, (xe - 5, 250))

def HardButton():
    # Hard Button function which is placed in the Selection Screen
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 400 <= mouse_x <= 700 and 400 <= mouse_y <= 500:
        display.blit(hard_button2, (xe -5 , 400))
        if click[0] == 1:  # Checks if the left button of the mouse is clicked.
            Hard_mode()    # Runs the Medium Mode function
    else:
        display.blit(hard_button, (xe - 5, 400))


def selection_screen():
    intro = True
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Mind Shaper')
    display.blit(sunset, (xs, ys))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Closes the window when the "X" button is clicked.
                pygame.quit()
                quit()
        bridgebutton()  # Bridge Gate
        easybutton()      # Places Easy Button Function
        MediumButton()    # Places Medium Button Function
        HardButton()      # Places Hard Button Function
        pygame.display.update()
        clock.tick(15)

def easy_mode():
    global pos,highLight, initiate, angel_1, angel_2, whatever_1, whatever_2, worried_1, worried_2, cool_1, cool_2, angel_match,whatever_match, worried_match, cool_match
    run = True
    random.shuffle(pos)
    while run:
        display = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Mind Shaper')
        display.blit(Space, (xs, ys))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        for i in range(8):  # Gets the Emoji's position from the "pos" list and places it into the Screen.
            display.blit(multi_images_L1[i], (pos[i]))

        """ These bunch of "if" statement checks whether the user has clicked on the "box" where each Emojis 
            are placed. It then changes the variable from False to True and adds "1" to the initiate variable. Adding 
            "1" notifies the system that the user has made his/her first selection and then waits for them to make their 
            Second choice. """
        if (pos[0][0]) - 10 <= mouse_x <= (pos[0][0]) + 115 and(pos[0][1]) -5 <= mouse_y <= int(pos[0][1]) + 129 and canClick:
            if mouse_click[0] == 1 and not angel_1:
                angel_1 = True
                initiate += 1
        elif (pos[1][0]) - 10 <= mouse_x <= (pos[1][0]) + 115 and(pos[1][1])-5 <= mouse_y <= (pos[1][1]) + 129 and canClick:
            if mouse_click[0] == 1 and not angel_2:
                angel_2 = True
                initiate += 1
        elif (pos[2][0]) - 10 <= mouse_x <= (pos[2][0]) + 115 and(pos[2][1])-5 <= mouse_y <= (pos[2][1]) + 129 and canClick:
            if mouse_click[0] == 1 and not whatever_1:
                whatever_1 = True
                initiate += 1
        elif (pos[3][0]) - 10 <= mouse_x <= (pos[3][0]) + 115 and(pos[3][1])-5 <= mouse_y <= (pos[3][1]) + 129 and canClick:
            if mouse_click[0] == 1 and not whatever_2:
                whatever_2 = True
                initiate += 1
        elif (pos[4][0]) - 10 <= mouse_x <= (pos[4][0]) + 115 and(pos[4][1])-5 <= mouse_y <= (pos[4][1]) + 129 and canClick:
            if mouse_click[0] == 1 and not worried_1:
                worried_1 = True
                initiate += 1
        elif (pos[5][0])- 10 <= mouse_x <= (pos[5][0]) + 115 and(pos[5][1])-5 <= mouse_y <= (pos[5][1]) + 129 and canClick:
            if mouse_click[0] == 1 and not worried_2:
                worried_2 = True
                initiate += 1
        elif (pos[6][0]) - 10 <= mouse_x <= (pos[6][0]) + 115 and(pos[6][1])-5 <= mouse_y <= (pos[6][1]) + 129 and canClick:
            if mouse_click[0] == 1 and not cool_1:
                cool_1 = True
                initiate += 1
        elif (pos[7][0]) - 10 <= mouse_x <= (pos[7][0]) + 115 and(pos[7][1])-5 <= mouse_y <= int(pos[7][1]) + 129 and canClick:
            if mouse_click[0] == 1 and not cool_2:
                cool_2 = True
                initiate += 1

        """ The "if" statements below adds the Boxes/Tiles in the screen. It also adds the function which highlights the 
        boxes when the mouse is hovering on top of it."""
        if not angel_1:
            hover()
            display.blit(Box, (pos[0][0] - 30, pos[0][1] - 20))
        if not angel_2:
            hover()
            display.blit(Box, (pos[1][0] - 30, pos[1][1] - 20))
        if not whatever_1:
            hover()
            display.blit(Box, (pos[2][0] - 30, pos[2][1] - 20))
        if not whatever_2:
            hover()
            display.blit(Box, (pos[3][0] - 30, pos[3][1] - 20))
        if not worried_1:
            hover()
            display.blit(Box, (pos[4][0] - 30, pos[4][1] - 20))
        if not worried_2:
            hover()
            display.blit(Box, (pos[5][0] - 30, pos[5][1] - 20))
        if not cool_1:
            hover()
            display.blit(Box, (pos[6][0] - 30, pos[6][1] - 20))
        if not cool_2:
            hover()
            display.blit(Box, (pos[7][0] - 30, pos[7][1] - 20))
        """Once the user has made their 2 choices, the system checks whether the emojis match or not. 
            If it matches the Boxes disappear and initiate is back to "0". Whereas, if they are not matched the Boxes 
            appear again and the game resumes. """
        if initiate == 2:
            if angel_1 == True and angel_2 == True and not angel_match:
                initiate = 0
                angel_match = True
            elif whatever_1 == True and whatever_2 == True and not whatever_match:
                initiate = 0
                whatever_match = True
            elif worried_1 == True and worried_2 == True and not worried_match:
                initiate = 0
                worried_match = True
            elif cool_1 == True and cool_2 == True and not cool_match:
                initiate = 0
                cool_match = True
            else:
                initiate = 0
                """ When the user has clicked on two boxes, Threading is used to pause the program for 1 second. This
                allows the program to set everything back to False if the emojis does not match and also prevents the 
                user to click on images no more than twice."""
                t = threading.Thread(target=display_pause, name="something", args=(800, "something"))
                t.start()
        retrybuttonfunc()  # Retry Button
        menubutton()       # Home Button
        congratulation_easy()  # Well Done Popup
        pygame.display.update()
        clock.tick(15)

def bridgebutton():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 19.2 <= mouse_x <= 100.9 and 19.2 <= mouse_y <= 100.9:
        display.blit(bridgegate2, (19.2, 20))
        if click[0] == 1:
            print("Bridge is Working")
    else:
        display.blit(bridgegate, (20, 20))

def congratulation_easy():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Checks whether all the images are matched or not. If they are matched Display the "dull screen" and the "Popup"
    if (angel_match and whatever_match and worried_match and cool_match) == True:
        display.blit(table2, (0, 0))
        display.blit(congratsEasy, (240, 100))
        # If retry is clicked it loops back and starts the game again.
        if 390 <= mouse_x <= 530 and 300 <= mouse_y <= 367:
            display.blit(congratsEasyretry, (390, 300))
            if click[0] == 1:
                normalise()
                easy_mode()
        # If Home is clicked it goes back to the Selection screen as well as resets the Easy mode.
        elif 560 <= mouse_x <= 700 and 300 <= mouse_y <= 367:
            display.blit(congratsEasyhome, (560, 300))
            if click[0] == 1:
                normalise()
                selection_screen()
                exit(easy_mode())

def menubutton():
    """ This function is a home button which will always be around the top left corner of the Screen, while the user is playing the game.
        This will allow the user to leave their current mode and go back to the selection screen in order to either quit the game or choose a new mode."""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 15 <= mouse_x <= 95 and 15 <= mouse_y <= 95:
        display.blit(homebutton2, (10, 10))
        if click[0] == 1:
            normalise()
            selection_screen()
            exit(easy_mode())
    else:
        display.blit(homebutton, (10, 10))
def retrybuttonfunc():
    """ This function is a "retry" button which will always be around the top right corner of the Screen, while the user
    is playing the game.This will allow the user to restart their current mode"""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 1005 <= mouse_x <= 1085 and 15 <= mouse_y <= 95:
        display.blit(retrybutton2, (1005, 10))
        if click[0] == 1:
            normalise()
            easy_mode()
    else:
        display.blit(retrybutton, (1005, 10))

def hover():
    global pos, click, highlight, highLight
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #This function will highligth the box if the mouse pointer is above it
    # Works for Easy mode only.
    for i in range(8):
        if (pos[i][0]) - 8 <= mouse_x <= (pos[i][0]) + 108 and (pos[i][1]) -5  <= mouse_y <= (pos[i][1]) + 115:
            display.blit(highlight, (int(pos[i][0]) - int(30), int(pos[i][1]) - int(20)))

def display_pause(time,name):
    # This function is used for threading in the Easy mode function
    global canClick, angel_1, angel_2, whatever_1, whatever_2, worried_1, worried_2, cool_1, cool_2
    canClick = False  # Stops the user from clicking any other boxes/tiles.
    pygame.time.wait(time)
    # Converts the emojis back to False if the are not matched.
    if not angel_match:
        angel_1,angel_2 = (False,) * 2
    if not whatever_match:
        whatever_1,whatever_2 = (False,) * 2
    if not worried_match:
        worried_1,worried_2 = (False,) * 2
    if not cool_match:
        cool_1,cool_2 = (False,) * 2
    canClick = True  # Allows the user to click the boxes/tiles after 1 sec.



def Hard_mode():
    global pos2, initiate_2,hard_box, rect_1, rect_2,rect_1A,rect_2A, hex_1, hex_2, hex_1A, hex_2A, star_1, star_2, star_1A,star_2A,circle_1, circle_2, circle_1A, circle_2A, triangle_1, triangle_2, triangle_1A, triangle_2A, opphex_1,opphex_2, opphex_1A, opphex_2A, oval_1, oval_2, oval_1A, oval_2A, heart_1, heart_2, heart_1A, heart_2A,commstar_1,commstar_2, commstar_1A, commstar_2A,splatpaint_1, splatpaint_2,splatpaint_1A,splatpaint_2A, square_1, square_2, rect_match, hex_match, star_match, circle_match, triangle_match, opphex_match, rect_Amatch, hex_Amatch,star_Amatch, circle_Amatch,triangle_Amatch, opphex_Amatch, oval_match, oval_Amatch, heart_match, heart_Amatch,commstar_match, commstar_Amatch, splatpaint_match,splatpaint_Amatch, square_match
    run2 = True
    random.shuffle(pos2)
    while run2:
        display = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Mind Shaper')
        display.blit(maths_background, (xs, ys))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()
                quit()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        for i in range(42):  # Gets the Shape's position from the "pos2" list and places it into the Screen.
            display.blit(multi_shapes_L2[i], (pos2[i]))

        # These "if" statements follows the same concept as described in Easy mode function, however, the emoji is replaced with shapes.
        if (pos2[0][0]) <= mouse_x <= (pos2[0][0]) + 75 and (pos2[0][1]) <= mouse_y <= int(pos2[0][1]) + 80 and canClick2:
            if mouse_click[0] == 1 and not rect_1:
                rect_1 = True
                initiate_2 += 1
        elif (pos2[1][0]) <= mouse_x <= (pos2[1][0])+ 75 and (pos2[1][1]) <= mouse_y <= (pos2[1][1])+ 80and canClick2:
            if mouse_click[0] == 1 and not rect_2:
                rect_2 = True
                initiate_2 += 1
        elif (pos2[2][0]) <= mouse_x <= (pos2[2][0])+ 75 and (pos2[2][1]) <= mouse_y <= (pos2[2][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not rect_1A:
                rect_1A = True
                initiate_2 += 1
        elif (pos2[3][0]) <= mouse_x <= (pos2[3][0]) + 75and (pos2[3][1]) <= mouse_y <= (pos2[3][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not rect_2A:
                rect_2A = True
                initiate_2 += 1
        elif (pos2[4][0]) <= mouse_x <= (pos2[4][0]) + 75and (pos2[4][1]) <= mouse_y <= (pos2[4][1]) + 80 and canClick2:
            if mouse_click[0] == 1 and not hex_1:
                hex_1 = True
                initiate_2 += 1
        elif (pos2[5][0]) <= mouse_x <= (pos2[5][0])+ 75 and (pos2[5][1]) <= mouse_y <= (pos2[5][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not hex_2:
                hex_2 = True
                initiate_2 += 1
        elif (pos2[6][0]) <= mouse_x <= (pos2[6][0]) + 75and (pos2[6][1]) <= mouse_y <= (pos2[6][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not hex_1A:
                hex_1A = True
                initiate_2 += 1
        elif (pos2[7][0]) <= mouse_x <= (pos2[7][0]) + 75and (pos2[7][1]) <= mouse_y <= int(pos2[7][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not hex_2A:
                hex_2A = True
                initiate_2 += 1
        if (pos2[8][0]) <= mouse_x <= (pos2[8][0]) + 75and (pos2[8][1]) <= mouse_y <= int(pos2[8][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not star_1:
                star_1 = True
                initiate_2 += 1
        elif (pos2[9][0]) <= mouse_x <= (pos2[9][0]) + 75and (pos2[9][1]) <= mouse_y <= (pos2[9][1])+ 80and canClick2:
            if mouse_click[0] == 1 and not star_2:
                star_2 = True
                initiate_2 += 1
        elif (pos2[10][0]) <= mouse_x <= (pos2[10][0]) + 75and (pos2[10][1]) <= mouse_y <= (pos2[10][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not star_1A:
                star_1A = True
                initiate_2 += 1
        elif (pos2[11][0]) <= mouse_x <= (pos2[11][0]) + 75and (pos2[11][1]) <= mouse_y <= (pos2[11][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not star_2A:
                star_2A = True
                initiate_2 += 1
        elif (pos2[12][0]) <= mouse_x <= (pos2[12][0]) + 75and (pos2[12][1]) <= mouse_y <= (pos2[12][1]) + 80 and canClick2:
            if mouse_click[0] == 1 and not circle_1:
                circle_1 = True
                initiate_2 += 1
        elif (pos2[13][0]) <= mouse_x <= (pos2[13][0]) + 75and (pos2[13][1]) <= mouse_y <= (pos2[13][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not circle_2:
                circle_2 = True
                initiate_2 += 1
        elif (pos2[14][0]) <= mouse_x <= (pos2[14][0]) + 75and (pos2[14][1]) <= mouse_y <= (pos2[14][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not circle_1A:
                circle_1A = True
                initiate_2 += 1
        elif (pos2[15][0]) <= mouse_x <= (pos2[15][0])+ 75 and (pos2[15][1]) <= mouse_y <= int(pos2[15][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not circle_2A:
                circle_2A = True
                initiate_2 += 1
        elif (pos2[16][0]) <= mouse_x <= (pos2[16][0]) + 75and (pos2[16][1]) <= mouse_y <= int(pos2[16][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not triangle_1:
                triangle_1 = True
                initiate_2 += 1
        elif (pos2[17][0]) <= mouse_x <= (pos2[17][0]) + 75and (pos2[17][1]) <= mouse_y <= (pos2[17][1])+ 80and canClick2:
            if mouse_click[0] == 1 and not triangle_2:
                triangle_2 = True
                initiate_2 += 1
        elif (pos2[18][0]) <= mouse_x <= (pos2[18][0]) + 75and (pos2[18][1]) <= mouse_y <= (pos2[18][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not triangle_1A:
                triangle_1A = True
                initiate_2 += 1
        elif (pos2[19][0]) <= mouse_x <= (pos2[19][0])+ 75 and (pos2[19][1]) <= mouse_y <= (pos2[19][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not triangle_2A:
                triangle_2A = True
                initiate_2 += 1
        elif (pos2[20][0]) <= mouse_x <= (pos2[20][0]) + 75and (pos2[20][1]) <= mouse_y <= (pos2[20][1]) + 80 and canClick2:
            if mouse_click[0] == 1 and not opphex_1:
                opphex_1 = True
                initiate_2 += 1
        elif (pos2[21][0]) <= mouse_x <= (pos2[21][0])+ 75 and (pos2[21][1]) <= mouse_y <= (pos2[21][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not opphex_2:
                opphex_2 = True
                initiate_2 += 1
        elif (pos2[22][0]) <= mouse_x <= (pos2[22][0]) + 75and (pos2[22][1]) <= mouse_y <= (pos2[22][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not opphex_1A:
                opphex_1A = True
                initiate_2 += 1
        elif (pos2[23][0]) <= mouse_x <= (pos2[23][0])+ 75 and (pos2[23][1]) <= mouse_y <= int(pos2[23][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not opphex_2A:
                opphex_2A = True
                initiate_2 += 1
        elif (pos2[24][0]) <= mouse_x <= (pos2[24][0])+ 75 and (pos2[24][1]) <= mouse_y <= int(pos2[24][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not oval_1:
                oval_1 = True
                initiate_2 += 1
        elif (pos2[25][0]) <= mouse_x <= (pos2[25][0])+ 75 and (pos2[25][1]) <= mouse_y <= (pos2[25][1])+ 80and canClick2:
            if mouse_click[0] == 1 and not oval_2:
                oval_2 = True
                initiate_2 += 1
        elif (pos2[26][0]) <= mouse_x <= (pos2[26][0]) + 75and (pos2[26][1]) <= mouse_y <= (pos2[26][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not oval_1A:
                oval_1A = True
                initiate_2 += 1
        elif (pos2[27][0]) <= mouse_x <= (pos2[27][0]) + 75and (pos2[27][1]) <= mouse_y <= (pos2[27][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not oval_2A:
                oval_2A = True
                initiate_2 += 1
        elif (pos2[28][0]) <= mouse_x <= (pos2[28][0]) + 75and (pos2[28][1]) <= mouse_y <= (pos2[28][1]) + 80 and canClick2:
            if mouse_click[0] == 1 and not heart_1:
                heart_1 = True
                initiate_2 += 1
        elif (pos2[29][0]) <= mouse_x <= (pos2[29][0]) + 75and (pos2[29][1]) <= mouse_y <= (pos2[29][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not heart_2:
                heart_2 = True
                initiate_2 += 1
        elif (pos2[30][0]) <= mouse_x <= (pos2[30][0]) + 75and (pos2[30][1]) <= mouse_y <= (pos2[30][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not heart_1A:
                heart_1A = True
                initiate_2 += 1
        elif (pos2[31][0]) <= mouse_x <= (pos2[31][0])+ 75 and (pos2[31][1]) <= mouse_y <= int(pos2[31][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not heart_2A:
                heart_2A = True
                initiate_2 += 1
        elif (pos2[32][0]) <= mouse_x <= (pos2[32][0]) + 75and (pos2[32][1]) <= mouse_y <= (pos2[32][1]) + 80 and canClick2:
            if mouse_click[0] == 1 and not commstar_1:
                commstar_1 = True
                initiate_2 += 1
        elif (pos2[33][0]) <= mouse_x <= (pos2[33][0]) + 75and (pos2[33][1]) <= mouse_y <= (pos2[33][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not commstar_2:
                commstar_2 = True
                initiate_2 += 1
        elif (pos2[34][0]) <= mouse_x <= (pos2[34][0]) + 75and (pos2[34][1]) <= mouse_y <= (pos2[34][1]) + 80 and canClick2:
            if mouse_click[0] == 1 and not commstar_1A:
                commstar_1A = True
                initiate_2 += 1
        elif (pos2[35][0]) <= mouse_x <= (pos2[35][0]) + 75and (pos2[35][1]) <= mouse_y <= int(pos2[35][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not commstar_2A:
                commstar_2A = True
                initiate_2 += 1
        elif (pos2[36][0]) <= mouse_x <= (pos2[36][0]) + 75and (pos2[36][1]) <= mouse_y <= int(pos2[36][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not splatpaint_1:
                splatpaint_1 = True
                initiate_2 += 1
        elif (pos2[37][0]) <= mouse_x <= (pos2[37][0]) + 75and (pos2[37][1]) <= mouse_y <= (pos2[37][1])+ 80and canClick2:
            if mouse_click[0] == 1 and not splatpaint_2:
                splatpaint_2 = True
                initiate_2 += 1
        elif (pos2[38][0]) <= mouse_x <= (pos2[38][0]) + 75and (pos2[38][1]) <= mouse_y <= (pos2[38][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not splatpaint_1A:
                splatpaint_1A = True
                initiate_2 += 1
        elif (pos2[39][0]) <= mouse_x <= (pos2[39][0]) + 75and (pos2[39][1]) <= mouse_y <= (pos2[39][1])+ 80 and canClick2:
            if mouse_click[0] == 1 and not splatpaint_2A:
                splatpaint_2A = True
                initiate_2 += 1
        elif (pos2[40][0]) <= mouse_x <= (pos2[40][0])+ 75 and (pos2[40][1]) <= mouse_y <= (pos2[40][1]) + 80 and canClick2:
            if mouse_click[0] == 1 and not square_1:
                square_1 = True
                initiate_2 += 1
        elif (pos2[41][0]) <= mouse_x <= (pos2[41][0]) + 75and (pos2[41][1]) <= mouse_y <= (pos2[41][1]) + 80and canClick2:
            if mouse_click[0] == 1 and not square_2:
                square_2 = True
                initiate_2 += 1

        """ The "if" statements below adds the Boxes/Tiles in the screen. It also adds the function which highlights the 
        boxes when the mouse is hovering on top of it."""
        if not rect_1:
            display.blit(boxh_1, (pos2[0][0], pos2[0][1]))
            hover3()
        if not rect_2:
            display.blit(boxh_1, (pos2[1][0], pos2[1][1]))
            hover3()
        if not rect_1A:
            display.blit(boxh_1, (pos2[2][0], pos2[2][1]))
            hover3()
        if not rect_2A:
            display.blit(boxh_1, (pos2[3][0], pos2[3][1]))
            hover3()
        if not hex_1:
            display.blit(boxh_1, (pos2[4][0], pos2[4][1]))
            hover3()
        if not hex_2:
            display.blit(boxh_1, (pos2[5][0], pos2[5][1]))
            hover3()
        if not hex_1A:
            display.blit(boxh_1, (pos2[6][0], pos2[6][1]))
            hover3()
        if not hex_2A:
            display.blit(boxh_1, (pos2[7][0], pos2[7][1]))
            hover3()
        if not star_1:
            display.blit(boxh_1, (pos2[8][0], pos2[8][1]))
            hover3()
        if not star_2:
            display.blit(boxh_1, (pos2[9][0], pos2[9][1]))
            hover3()
        if not star_1A:
            display.blit(boxh_1, (pos2[10][0], pos2[10][1]))
            hover3()
        if not star_2A:
            display.blit(boxh_1, (pos2[11][0], pos2[11][1]))
            hover3()
        if not circle_1:
            display.blit(boxh_1, (pos2[12][0], pos2[12][1]))
            hover3()
        if not circle_2:
            display.blit(boxh_1, (pos2[13][0], pos2[13][1]))
            hover3()
        if not circle_1A:
            display.blit(boxh_1, (pos2[14][0], pos2[14][1]))
            hover3()
        if not circle_2A:
            display.blit(boxh_1, (pos2[15][0], pos2[15][1]))
            hover3()
        if not triangle_1:
            display.blit(boxh_1, (pos2[16][0], pos2[16][1]))
            hover3()
        if not triangle_2:
            display.blit(boxh_1, (pos2[17][0], pos2[17][1]))
            hover3()
        if not triangle_1A:
            display.blit(boxh_1, (pos2[18][0], pos2[18][1]))
            hover3()
        if not triangle_2A:
            display.blit(boxh_1, (pos2[19][0], pos2[19][1]))
            hover3()
        if not opphex_1:
            display.blit(boxh_1, (pos2[20][0], pos2[20][1]))
            hover3()
        if not opphex_2:
            display.blit(boxh_1, (pos2[21][0], pos2[21][1]))
            hover3()
        if not opphex_1A:
            display.blit(boxh_1, (pos2[22][0], pos2[22][1]))
            hover3()
        if not opphex_2A:
            display.blit(boxh_1, (pos2[23][0], pos2[23][1]))
            hover3()
        if not oval_1:
            display.blit(boxh_1, (pos2[24][0], pos2[24][1]))
            hover3()
        if not oval_2:
            display.blit(boxh_1, (pos2[25][0], pos2[25][1]))
            hover3()
        if not oval_1A:
            display.blit(boxh_1, (pos2[26][0], pos2[26][1]))
            hover3()
        if not oval_2A:
            display.blit(boxh_1, (pos2[27][0], pos2[27][1]))
            hover3()
        if not heart_1:
            display.blit(boxh_1, (pos2[28][0], pos2[28][1]))
            hover3()
        if not heart_2:
            display.blit(boxh_1, (pos2[29][0], pos2[29][1]))
            hover3()
        if not heart_1A:
            display.blit(boxh_1, (pos2[30][0], pos2[30][1]))
            hover3()
        if not heart_2A:
            display.blit(boxh_1, (pos2[31][0], pos2[31][1]))
            hover3()
        if not commstar_1:
            display.blit(boxh_1, (pos2[32][0], pos2[32][1]))
            hover3()
        if not commstar_2:
            display.blit(boxh_1, (pos2[33][0], pos2[33][1]))
            hover3()
        if not commstar_1A:
            display.blit(boxh_1, (pos2[34][0], pos2[34][1]))
            hover3()
        if not commstar_2A:
            display.blit(boxh_1, (pos2[35][0], pos2[35][1]))
            hover3()
        if not splatpaint_1:
            display.blit(boxh_1, (pos2[36][0], pos2[36][1]))
            hover3()
        if not splatpaint_2:
            display.blit(boxh_1, (pos2[37][0], pos2[37][1]))
            hover3()
        if not splatpaint_1A:
            display.blit(boxh_1, (pos2[38][0], pos2[38][1]))
            hover3()
        if not splatpaint_2A:
            display.blit(boxh_1, (pos2[39][0], pos2[39][1]))
            hover3()
        if not square_1:
            display.blit(boxh_1, (pos2[40][0], pos2[40][1]))
            hover3()
        if not square_2:
            display.blit(boxh_1, (pos2[41][0], pos2[41][1]))
            hover3()

        """Once the user has made their 2 choices, the system checks whether the Shapes match or not. 
            If it matches the Boxes disappear and initiate is back to "0". Whereas, if they are not matched the Boxes 
            appear again and the game resumes. """
        if initiate_2 == 2:
            if rect_1 == True and rect_2 == True and not rect_match:
                initiate_2 = 0
                rect_match = True
            elif rect_1A == True and rect_2A == True and not rect_Amatch:
                initiate_2 = 0
                rect_Amatch = True
            elif hex_1 == True and hex_2 == True and not hex_match:
                initiate_2 = 0
                hex_match = True
            elif hex_1A == True and hex_2A == True and not hex_Amatch:
                initiate_2 = 0
                hex_Amatch = True
            elif star_1 == True and star_2 == True and not star_match:
                initiate_2 = 0
                star_match = True
            elif star_1A == True and star_2A == True and not star_Amatch:
                initiate_2 = 0
                star_Amatch = True
            elif circle_1 == True and circle_2 == True and not circle_match:
                initiate_2 = 0
                circle_match = True
            elif circle_1A == True and  circle_2A == True and not circle_Amatch:
                initiate_2 = 0
                circle_Amatch = True
            elif triangle_1 == True and triangle_2 == True and not triangle_match:
                initiate_2 = 0
                triangle_match = True
            elif triangle_1A == True and triangle_2A == True and not triangle_Amatch:
                initiate_2 = 0
                triangle_Amatch = True
            elif opphex_1 == True and opphex_2 == True and not opphex_match:
                initiate_2 = 0
                opphex_match = True
            elif opphex_1A == True and opphex_2A == True and not opphex_Amatch:
                initiate_2 = 0
                opphex_Amatch = True
            elif oval_1 == True and oval_2 == True and not oval_match:
                initiate_2 = 0
                oval_match = True
            elif oval_1A == True and oval_2A == True and not oval_Amatch:
                initiate_2 = 0
                oval_Amatch = True
            elif heart_1 == True and heart_2 == True and not heart_match:
                initiate_2 = 0
                heart_match = True
            elif heart_1A == True and heart_2A == True and not heart_Amatch:
                initiate_2 = 0
                heart_Amatch = True
            elif commstar_1 == True and commstar_2 == True and not commstar_match:
                initiate_2 = 0
                commstar_match = True
            elif commstar_1A == True and commstar_2A == True and not commstar_Amatch:
                initiate_2 = 0
                commstar_Amatch = True
            elif splatpaint_1 == True and splatpaint_2 == True and not splatpaint_match:
                initiate_2 = 0
                splatpaint_match = True
            elif splatpaint_1A == True and splatpaint_2A == True and not splatpaint_Amatch:
                initiate_2 = 0
                splatpaint_Amatch = True
            elif square_1 == True and square_2 == True and not square_match:
                initiate_2 = 0
                square_match = True
            else:
                initiate_2 = 0
                t_2 = threading.Thread(target=display_pause2, name="something", args=(1000, "something"))
                t_2.start()
        retrybuttonfunc3()  # Retry Button
        menubutton3()  # Home Button
        congratulation_easy3()  # Well Done Popup
        pygame.display.update()

def display_pause2(time, name2):
    # This function is used for threading in the Hard mode function
    global canClick2, rect_1, rect_2,rect_1A,rect_2A, hex_1, hex_2, hex_1A, hex_2A, star_1, star_2, star_1A, star_2A,circle_1, circle_2, circle_1A, circle_2A, triangle_1, triangle_2, triangle_1A, triangle_2A, opphex_1,opphex_2, opphex_1A, opphex_2A, oval_1, oval_2, oval_1A, oval_2A, heart_1, heart_2, heart_1A, heart_2A,commstar_1,commstar_2, commstar_1A, commstar_2A,splatpaint_1, splatpaint_2,splatpaint_1A,splatpaint_2A, square_1,square_2
    canClick2 = False # Stops the user from clicking any other boxes/tiles.
    pygame.time.wait(time)
    # Converts the emojis back to False if the are not matched.
    if not rect_match:
        rect_1,rect_2 = (False,) * 2
    if not rect_Amatch:
        rect_1A,rect_2A = (False,) * 2
    if not hex_match:
        hex_1,hex_2 = (False,) * 2
    if not hex_Amatch:
        hex_1A,hex_2A = (False,) * 2
    if not star_match:
        star_1,star_2 = (False,) * 2
    if not star_Amatch:
        star_1A,star_2A = (False,) * 2
    if not circle_match:
        circle_1, circle_2= (False,) * 2
    if not circle_Amatch:
        circle_1A,circle_2A = (False,) * 2
    if not triangle_match:
        triangle_1,triangle_2 = (False,) * 2
    if not triangle_Amatch:
        triangle_1A,triangle_2A = (False,) * 2
    if not opphex_match:
        opphex_1,opphex_2 = (False,) * 2
    if not opphex_Amatch:
        opphex_1A,opphex_2A = (False,) * 2
    if not oval_match:
        oval_1,oval_2 = (False,) * 2
    if not oval_Amatch:
        oval_1A,oval_2A = (False,) * 2
    if not heart_match:
        heart_1,heart_2 = (False,) * 2
    if not heart_Amatch:
        heart_1A,heart_2A = (False,) * 2
    if not commstar_match:
        commstar_1,commstar_2 = (False,) * 2
    if not commstar_Amatch:
        commstar_1A,commstar_2A = (False,) * 2
    if not splatpaint_match:
        splatpaint_1,splatpaint_2 = (False,) * 2
    if not splatpaint_Amatch:
        splatpaint_1A,splatpaint_2A = (False,) * 2
    if not square_match:
        square_1,square_2 = (False,) * 2
    canClick2 = True # Allows the user to click the boxes/tiles after 1 sec.

def menubutton3():
    """ This function is a home button which will always be around the top left corner of the Screen, while the user is playing the game.
        This will allow the user to leave their current mode and go back to the selection screen in order to either quit the game or choose a new mode."""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 15 <= mouse_x <= 95 and 15 <= mouse_y <= 95:
        display.blit(homebutton2, (10, 10))
        if click[0] == 1:
            normalise_3()
            selection_screen()
            exit(Hard_mode())
    else:
        display.blit(homebutton, (10, 10))
def retrybuttonfunc3():
    """ This function is a "retry" button which will always be around the top right corner of the Screen, while the user
    is playing the game.This will allow the user to restart their current mode"""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 1005 <= mouse_x <= 1085 and 15 <= mouse_y <= 95:
        display.blit(retrybutton2, (1005, 10))
        if click[0] == 1:
            normalise_3()
            Hard_mode()
    else:
        display.blit(retrybutton, (1005, 10))

def hover3():
    global pos2, click, highlight_hard
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # This function will highligth the box if the mouse pointer is above it
    # Works for Hard mode only.
    for i in range(42):
        if (pos2[i][0]) <= mouse_x <= (pos2[i][0]) + 75 and (pos2[i][1]) <= mouse_y <= (pos2[i][1]) + 80:
            display.blit(highlight_hard, (pos2[i][0] - 2 , pos2[i][1]-2))

def congratulation_easy3():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Checks whether all the images are matched or not. If they are matched Display the "dull screen" and the "Popup"
    if (rect_match and rect_Amatch  and hex_match and hex_Amatch and star_match and star_Amatch and circle_match and circle_Amatch and triangle_match and triangle_Amatch and opphex_match and opphex_Amatch and oval_match and oval_Amatch and heart_match and heart_Amatch and commstar_match and commstar_Amatch and splatpaint_match and splatpaint_Amatch and square_match ) == True:
        display.blit(table2, (0, 0))
        display.blit(congratsEasy, (255, 100))
        if 405 <= mouse_x <= 545 and 300 <= mouse_y <= 367:
            display.blit(congratsEasyretry, (405, 300))
        # If retry is clicked it loops back and starts the game again.
            if click[0] == 1:
                normalise_3()
                Hard_mode()
        # If Home is clicked it goes back to the Selection screen as well as resets the Hard mode.
        elif 575 <= mouse_x <=715 and 300 <= mouse_y <= 367:
            display.blit(congratsEasyhome, (575, 300))
            if click[0] == 1:
                normalise_3()
                selection_screen()
                exit(Hard_mode())

def medium_mode():
    global pos3, initiate_3, tacos_1, tacos_2, tacos_match, pizza_1, pizza_2 ,pizza_match, popcorn_1, popcorn_2, popcorn_match, burger_1, burger_2,burger_match, sandwich_1, sandwich_2,sandwich_match, cookies_1, cookies_2,cookies_match, icecream_1, icecream_2, icecream_match,  whitechoc_1, whitechoc_2,whitechoc_match, pancakecream_1,pancakecream_2, pancakecream_match, chips_1,chips_2, chips_match,fries_1,fries_2,fries_match,donut_1, donut_2, donut_match, drink_1,drink_2,drink_match, cupcake_1,cupcake_2,cupcake_match, hotdog_1, hotdog_2, hotdog_match
    run3 = True
    random.shuffle(pos3)
    while run3:
        display = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Mind Shaper')
        display.blit(table, (xs, ys))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] == 1:
            print(mouse_x, mouse_y)

        for i in range(30): # Gets the Fast Food images position from the "pos3" list and places it into the Screen.
            display.blit(multi_junks_L2[i],(pos3[i]))
        # These "if" statements follows the same concept as described in Easy mode function, however, the emoji is replaced with Fast Food Images.
        if (pos3[0][0]) <= mouse_x <= (pos3[0][0]) + 80 and (pos3[0][1]) <= mouse_y <= int(pos3[0][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not tacos_1:
                tacos_1 = True
                initiate_3 += 1
        elif (pos3[1][0]) <= mouse_x <= (pos3[1][0]) + 80 and (pos3[1][1]) <= mouse_y <= (pos3[1][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not tacos_2:
                tacos_2 = True
                initiate_3 += 1
        elif (pos3[2][0]) <= mouse_x <= (pos3[2][0]) + 80 and (pos3[2][1]) <= mouse_y <= (pos3[2][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not pizza_1:
                pizza_1 = True
                initiate_3 += 1
        elif (pos3[3][0]) <= mouse_x <= (pos3[3][0]) + 80 and (pos3[3][1]) <= mouse_y <= (pos3[3][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not pizza_2:
                pizza_2 = True
                initiate_3 += 1
        elif (pos3[4][0]) <= mouse_x <= (pos3[4][0]) + 80 and (pos3[4][1]) <= mouse_y <= (pos3[4][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not popcorn_1:
                popcorn_1 = True
                initiate_3 += 1
        elif (pos3[5][0]) <= mouse_x <= (pos3[5][0]) + 80 and (pos3[5][1]) <= mouse_y <= (pos3[5][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not popcorn_2:
                popcorn_2 = True
                initiate_3 += 1
        elif (pos3[6][0]) <= mouse_x <= (pos3[6][0]) + 80 and (pos3[6][1]) <= mouse_y <= (pos3[6][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not burger_1:
                burger_1 = True
                initiate_3 += 1
        elif (pos3[7][0]) <= mouse_x <= (pos3[7][0]) + 80 and (pos3[7][1]) <= mouse_y <= (pos3[7][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not burger_2:
                burger_2 = True
                initiate_3 += 1
        elif (pos3[8][0]) <= mouse_x <= (pos3[8][0]) + 80 and (pos3[8][1]) <= mouse_y <= (pos3[8][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not sandwich_1:
                sandwich_1 = True
                initiate_3 += 1
        elif (pos3[9][0]) <= mouse_x <= (pos3[9][0]) + 80 and (pos3[9][1]) <= mouse_y <= (pos3[9][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not sandwich_2:
                sandwich_2 = True
                initiate_3 += 1
        elif (pos3[10][0]) <= mouse_x <= (pos3[10][0]) + 80 and (pos3[10][1]) <= mouse_y <= (pos3[10][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not cookies_1:
                cookies_1 = True
                initiate_3 += 1
        elif (pos3[11][0]) <= mouse_x <= (pos3[11][0]) + 80 and (pos3[11][1]) <= mouse_y <= (pos3[11][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not cookies_2:
                cookies_2 = True
                initiate_3 += 1
        elif (pos3[12][0]) <= mouse_x <= (pos3[12][0]) + 80 and (pos3[12][1]) <= mouse_y <= (pos3[12][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not icecream_1:
                icecream_1 = True
                initiate_3 += 1
        elif (pos3[13][0]) <= mouse_x <= (pos3[13][0]) + 80 and (pos3[13][1]) <= mouse_y <= (pos3[13][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not icecream_2:
                icecream_2 = True
                initiate_3 += 1
        elif (pos3[14][0]) <= mouse_x <= (pos3[14][0]) + 80 and (pos3[14][1]) <= mouse_y <= (pos3[14][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not whitechoc_1:
                whitechoc_1 = True
                initiate_3 += 1
        elif (pos3[15][0]) <= mouse_x <= (pos3[15][0]) + 80 and (pos3[15][1]) <= mouse_y <= (pos3[15][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not whitechoc_2:
                whitechoc_2 = True
                initiate_3 += 1
        elif (pos3[16][0]) <= mouse_x <= (pos3[16][0]) + 80 and (pos3[16][1]) <= mouse_y <= (pos3[16][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not pancakecream_1:
                pancakecream_1 = True
                initiate_3 += 1
        elif (pos3[17][0]) <= mouse_x <= (pos3[17][0]) + 80 and (pos3[17][1]) <= mouse_y <= (pos3[17][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not pancakecream_2:
                pancakecream_2 = True
                initiate_3 += 1
        elif (pos3[18][0]) <= mouse_x <= (pos3[18][0]) + 80 and (pos3[18][1]) <= mouse_y <= (pos3[18][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not chips_1:
                chips_1 = True
                initiate_3 += 1
        elif (pos3[19][0]) <= mouse_x <= (pos3[19][0]) + 80 and (pos3[19][1]) <= mouse_y <= (pos3[19][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not chips_2:
                chips_2 = True
                initiate_3 += 1
        elif (pos3[20][0]) <= mouse_x <= (pos3[20][0]) + 80 and (pos3[20][1]) <= mouse_y <= (pos3[20][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not fries_1:
                fries_1 = True
                initiate_3 += 1
        elif (pos3[21][0]) <= mouse_x <= (pos3[21][0]) + 80 and (pos3[21][1]) <= mouse_y <= (pos3[21][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not fries_2:
                fries_2 = True
                initiate_3 += 1
        elif (pos3[22][0]) <= mouse_x <= (pos3[22][0]) + 80 and (pos3[22][1]) <= mouse_y <= (pos3[22][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not donut_1:
                donut_1 = True
                initiate_3 += 1
        elif (pos3[23][0]) <= mouse_x <= (pos3[23][0]) + 80 and (pos3[23][1]) <= mouse_y <= (pos3[23][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not donut_2:
                donut_2 = True
                initiate_3 += 1
        elif (pos3[24][0]) <= mouse_x <= (pos3[24][0]) + 80 and (pos3[24][1]) <= mouse_y <= (pos3[24][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not drink_1:
                drink_1 = True
                initiate_3 += 1
        elif (pos3[25][0]) <= mouse_x <= (pos3[25][0]) + 80 and (pos3[25][1]) <= mouse_y <= (pos3[25][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not drink_2:
                drink_2 = True
                initiate_3 += 1
        elif (pos3[26][0]) <= mouse_x <= (pos3[26][0]) + 80 and (pos3[26][1]) <= mouse_y <= (pos3[26][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not cupcake_1:
                cupcake_1 = True
                initiate_3 += 1
        elif (pos3[27][0]) <= mouse_x <= (pos3[27][0]) + 80 and (pos3[27][1]) <= mouse_y <= (pos3[27][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not cupcake_2:
                cupcake_2 = True
                initiate_3 += 1
        elif (pos3[28][0]) <= mouse_x <= (pos3[28][0]) + 80 and (pos3[28][1]) <= mouse_y <= (pos3[28][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not hotdog_1:
                hotdog_1 = True
                initiate_3 += 1
        elif (pos3[29][0]) <= mouse_x <= (pos3[29][0]) + 80 and (pos3[29][1]) <= mouse_y <= (pos3[29][1]) + 85 and canClick3:
            if mouse_click[0] == 1 and not hotdog_2:
                hotdog_2 = True
                initiate_3 += 1
        """ The "if" statements below adds the Boxes/Tiles in the Medium mode screen. It also adds the function which highlights the 
        boxes when the mouse is hovering on top of it."""
        if not tacos_1:
            hover2()
            display.blit(medium_box, (pos3[0][0], pos3[0][1]))
        if not tacos_2:
            hover2()
            display.blit(medium_box, (pos3[1][0], pos3[1][1]))
        if not pizza_1:
            hover2()
            display.blit(medium_box, (pos3[2][0], pos3[2][1] ))
        if not pizza_2:
            hover2()
            display.blit(medium_box, (pos3[3][0], pos3[3][1]))
        if not popcorn_1:
            hover2()
            display.blit(medium_box, (pos3[4][0], pos3[4][1]))
        if not popcorn_2:
            hover2()
            display.blit(medium_box, (pos3[5][0], pos3[5][1]))
        if not burger_1:
            hover2()
            display.blit(medium_box, (pos3[6][0], pos3[6][1]))
        if not burger_2:
            hover2()
            display.blit(medium_box, (pos3[7][0], pos3[7][1]))
        if not sandwich_1:
            hover2()
            display.blit(medium_box, (pos3[8][0], pos3[8][1]))
        if not sandwich_2:
            hover2()
            display.blit(medium_box, (pos3[9][0], pos3[9][1]))
        if not cookies_1:
            hover2()
            display.blit(medium_box, (pos3[10][0], pos3[10][1]))
        if not cookies_2:
            hover2()
            display.blit(medium_box, (pos3[11][0], pos3[11][1]))
        if not icecream_1:
            hover2()
            display.blit(medium_box, (pos3[12][0], pos3[12][1]))
        if not icecream_2:
            hover2()
            display.blit(medium_box, (pos3[13][0], pos3[13][1]))
        if not whitechoc_1:
            hover2()
            display.blit(medium_box, (pos3[14][0], pos3[14][1]))
        if not whitechoc_2:
            hover2()
            display.blit(medium_box, (pos3[15][0], pos3[15][1]))
        if not pancakecream_1:
            hover2()
            display.blit(medium_box, (pos3[16][0], pos3[16][1]))
        if not pancakecream_2:
            hover2()
            display.blit(medium_box, (pos3[17][0], pos3[17][1]))
        if not chips_1:
            hover2()
            display.blit(medium_box, (pos3[18][0], pos3[18][1]))
        if not chips_2:
            hover2()
            display.blit(medium_box, (pos3[19][0], pos3[19][1] ))
        if not fries_1:
            hover2()
            display.blit(medium_box, (pos3[20][0], pos3[20][1]))
        if not fries_2:
            hover2()
            display.blit(medium_box, (pos3[21][0], pos3[21][1]))
        if not donut_1:
            hover2()
            display.blit(medium_box, (pos3[22][0], pos3[22][1]))
        if not donut_2:
            hover2()
            display.blit(medium_box, (pos3[23][0], pos3[23][1]))
        if not drink_1:
            hover2()
            display.blit(medium_box, (pos3[24][0], pos3[24][1]))
        if not drink_2:
            hover2()
            display.blit(medium_box, (pos3[25][0], pos3[25][1]))
        if not cupcake_1:
            hover2()
            display.blit(medium_box, (pos3[26][0], pos3[26][1]))
        if not cupcake_2:
            hover2()
            display.blit(medium_box, (pos3[27][0], pos3[27][1]))
        if not hotdog_1:
            display.blit(medium_box, (pos3[28][0], pos3[28][1]))
            hover2()
        if not hotdog_2:
            display.blit(medium_box, (pos3[29][0], pos3[29][1]))
            hover2()

        """Once the user has made their 2 choices, the system checks whether the Fast food images matches or not. 
            If it matches the Boxes disappear and initiate is back to "0". Whereas, if they are not matched the Boxes 
            appear again and the game resumes. """
        if initiate_3 == 2:
            if tacos_1 == True and tacos_2 == True and not tacos_match:
                initiate_3 = 0
                tacos_match = True
            elif pizza_1 == True and pizza_2 == True and not pizza_match:
                initiate_3 = 0
                pizza_match = True
            elif popcorn_1 == True and popcorn_2 == True and not popcorn_match:
                initiate_3 = 0
                popcorn_match = True
            elif burger_1 == True and burger_2 == True and not burger_match:
                initiate_3 = 0
                burger_match = True
            elif sandwich_1 == True and sandwich_2 == True and not sandwich_match:
                initiate_3 = 0
                sandwich_match = True
            elif cookies_1 == True and cookies_2 == True and not cookies_match:
                initiate_3 = 0
                cookies_match = True
            elif icecream_1 == True and icecream_2 == True and not icecream_match:
                initiate_3 = 0
                icecream_match = True
            elif whitechoc_1 == True and  whitechoc_2 == True and not whitechoc_match:
                initiate_3 = 0
                whitechoc_match = True
            elif pancakecream_1 == True and pancakecream_2 == True and not pancakecream_match:
                initiate_3 = 0
                pancakecream_match = True
            elif chips_1 == True and chips_2 == True and not chips_match:
                initiate_3 = 0
                chips_match = True
            elif fries_1 == True and fries_2 == True and not fries_match:
                initiate_3 = 0
                fries_match = True
            elif donut_1 == True and donut_2 == True and not donut_match:
                initiate_3 = 0
                donut_match = True
            elif drink_1 == True and  drink_2 == True and not drink_match:
                initiate_3 = 0
                drink_match = True
            elif cupcake_1 == True and cupcake_2 == True and not cupcake_match:
                initiate_3 = 0
                cupcake_match = True
            elif hotdog_1 == True and hotdog_2 == True and not hotdog_match:
                initiate_3 = 0
                hotdog_match = True
            else:
                initiate_3 = 0
                t_3 = threading.Thread(target=display_pause3, name="something", args=(1000, "something"))
                t_3.start()
        menubutton2()      # Home Button
        retrybuttonfunc2() # Retry Button
        congratulation_easy2() # Well Done "Pop up"
        pygame.display.update()

def menubutton2():
    """ This function is a home button which will always be around the top left corner of the Screen, while the user is playing the game.
        This will allow the user to leave their current mode and go back to the selection screen in order to either quit the game or choose a new mode."""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 15 <= mouse_x <= 95 and 15 <= mouse_y <= 95:
        display.blit(homebutton2, (10, 10))
        if click[0] == 1:
            normalise_2()
            selection_screen()
            exit(medium_mode())
    else:
        display.blit(homebutton, (10, 10))

def retrybuttonfunc2():
    """ This function is a "retry" button which will always be around the top right corner of the Screen, while the user
    is playing the game.This will allow the user to restart their current mode"""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 1005 <= mouse_x <= 1085 and 15 <= mouse_y <= 95:
        display.blit(retrybutton2, (1005, 10))
        if click[0] == 1:
            normalise_2()
            medium_mode()
    else:
        display.blit(retrybutton, (1005, 10))

def hover2():
    global pos3,click, med_tilefade, highlight_med
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # This function will highligth the box if the mouse pointer is above it
    # Works for Medium mode only.
    for i in range(30):
        if (pos3[i][0]) <= mouse_x <= (pos3[i][0]) + 80 and (pos3[i][1]) <= mouse_y <= (pos3[i][1]) + 85:
            display.blit(highlight_med,(pos3[i][0]-2.5,pos3[i][1]-2.5))

def display_pause3(time, name3):
    global canClick3, tacos_1, tacos_2, pizza_1, pizza_2 , popcorn_1, popcorn_2, burger_1, burger_2, sandwich_1, sandwich_2, cookies_1,cookies_2, icecream_1, icecream_2,  whitechoc_1, whitechoc_2, pancakecream_1,pancakecream_2,  chips_1,chips_2,fries_1,fries_2,donut_1, donut_2,  drink_1,drink_2, cupcake_1,cupcake_2, hotdog_1, hotdog_2
    print('starting pause now3')
    canClick3 = False
    pygame.time.wait(time)
    if not tacos_match:
        tacos_1, tacos_2 = (False,) * 2
    if not pizza_match:
        pizza_1, pizza_2 = (False,) * 2
    if not popcorn_match:
        popcorn_1, popcorn_2 = (False,) * 2
    if not burger_match:
        burger_1, burger_2 = (False,) * 2
    if not sandwich_match:
        sandwich_1, sandwich_2 = (False,) * 2
    if not cookies_match:
        cookies_1, cookies_2 = (False,) * 2
    if not icecream_match:
        icecream_1, icecream_2 = (False,) * 2
    if not whitechoc_match:
        whitechoc_1, whitechoc_2 = (False,) * 2
    if not pancakecream_match:
        pancakecream_1, pancakecream_2 = (False,) * 2
    if not chips_match:
        chips_1, chips_2 = (False,) * 2
    if not fries_match:
        fries_1, fries_2 = (False,) * 2
    if not donut_match:
        donut_1, donut_2 = (False,) * 2
    if not drink_match:
        drink_1, drink_2 = (False,) * 2
    if not cupcake_match:
        cupcake_1, cupcake_2 = (False,) * 2
    if not hotdog_match:
        hotdog_1, hotdog_2 = (False,) * 2

    canClick3 = True

def congratulation_easy2():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Checks whether all the images are matched or not. If they are matched Display the "dull screen" and the "Popup"
    if (tacos_match and pizza_match  and popcorn_match and burger_match and sandwich_match and cookies_match and icecream_match and whitechoc_match and pancakecream_match and chips_match and fries_match and donut_match and drink_match and cupcake_match and hotdog_match ) == True:
        display.blit(table2, (0, 0))
        display.blit(congratsEasy, (236, 100))
        # If retry is clicked it loops back and starts the game again.
        if 386 <= mouse_x <= 526 and 300 <= mouse_y <= 367:
            display.blit(congratsEasyretry, (386, 300))
            if click[0] == 1:
                normalise_2()
                medium_mode()
        # If Home is clicked it goes back to the Selection screen as well as resets the Medium mode.
        elif 556 <= mouse_x <=696 and 300 <= mouse_y <= 367:
            display.blit(congratsEasyhome, (556, 300))
            if click[0] == 1:
                normalise_2()
                selection_screen()
                exit(medium_mode())
def normalise():
    # Resets all the Emojis back to False
    global angel_1, angel_2, angel_match,cool_1, cool_2, cool_match, whatever_1,whatever_2,whatever_match, worried_1, worried_2, worried_match
    angel_1, angel_2, angel_match,cool_1, cool_2, cool_match, whatever_1,whatever_2,whatever_match, worried_1, worried_2, worried_match = (False,) * 12

def normalise_2():
    # Resets all the Fast Food images back to False
    global tacos_1, tacos_2, tacos_match, pizza_1, pizza_2 ,pizza_match, popcorn_1, popcorn_2, popcorn_match, burger_1, burger_2,burger_match, sandwich_1, sandwich_2,sandwich_match, cookies_1,cookies_2,cookies_match, icecream_1, icecream_2, icecream_match,  whitechoc_1, whitechoc_2,whitechoc_match, pancakecream_1,pancakecream_2, pancakecream_match, chips_1,chips_2, chips_match,fries_1,fries_2,fries_match,donut_1, donut_2, donut_match, drink_1,drink_2,drink_match, cupcake_1,cupcake_2,cupcake_match, hotdog_1, hotdog_2,hotdog_match
    tacos_1, tacos_2, tacos_match, pizza_1, pizza_2, pizza_match, popcorn_1, popcorn_2, popcorn_match, burger_1, burger_2, burger_match, sandwich_1, sandwich_2, sandwich_match, cookies_1, cookies_2, cookies_match, icecream_1, icecream_2, icecream_match, whitechoc_1, whitechoc_2, whitechoc_match, pancakecream_1, pancakecream_2, pancakecream_match, chips_1, chips_2, chips_match, fries_1, fries_2, fries_match, donut_1, donut_2, donut_match, drink_1, drink_2, drink_match, cupcake_1, cupcake_2, cupcake_match, hotdog_1, hotdog_2, hotdog_match = (False,) * 45

def normalise_3():
    # Resets all the Shapes back to False
    global rect_1, rect_2,rect_1A,rect_2A, hex_1, hex_2, hex_1A, hex_2A, star_1, star_2, star_1A, star_2A,circle_1, circle_2, circle_1A, circle_2A, triangle_1, triangle_2, triangle_1A, triangle_2A, opphex_1, opphex_2, opphex_1A, opphex_2A, oval_1, oval_2, oval_1A, oval_2A, heart_1, heart_2, heart_1A, heart_2A,commstar_1,commstar_2, commstar_1A, commstar_2A,splatpaint_1, splatpaint_2,splatpaint_1A,splatpaint_2A, square_1, square_2, rect_match, hex_match, star_match, circle_match, triangle_match, opphex_match, rect_Amatch, hex_Amatch,star_Amatch, circle_Amatch,triangle_Amatch, opphex_Amatch, oval_match, oval_Amatch, heart_match, heart_Amatch, commstar_match, commstar_Amatch, splatpaint_match,splatpaint_Amatch, square_match
    rect_1, rect_2, rect_1A, rect_2A, hex_1, hex_2, hex_1A, hex_2A, star_1, star_2, star_1A, star_2A, circle_1, circle_2, circle_1A, circle_2A, triangle_1, triangle_2, triangle_1A, triangle_2A, opphex_1, opphex_2, opphex_1A, opphex_2A, oval_1, oval_2, oval_1A, oval_2A, heart_1, heart_2, heart_1A, heart_2A, commstar_1, commstar_2, commstar_1A, commstar_2A, splatpaint_1, splatpaint_2, splatpaint_1A, splatpaint_2A, square_1, square_2, rect_match, hex_match, star_match, circle_match, triangle_match, opphex_match, rect_Amatch, hex_Amatch, star_Amatch, circle_Amatch, triangle_Amatch, opphex_Amatch, oval_match, oval_Amatch, heart_match, heart_Amatch, commstar_match, commstar_Amatch, splatpaint_match, splatpaint_Amatch, square_match = (False,) * 63

selection_screen()
