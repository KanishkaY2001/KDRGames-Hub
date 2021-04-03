# Importing modules
import pygame, sys, os, threading, time, random
from random import seed
from random import shuffle

# Defining the file directories for easy access
snakes_script_dir = os.path.dirname(__file__)
snakes_image_dir = "DataFile/Audio_Images/"
snakes_image_list = "DataFile/ImageList.txt"
snakes_variable_list = "DataFile/VariableList.txt"

# Setting up the Pygame module
pygame.init()
width, height = 1100, 605
display = pygame.display.set_mode((width, height))
snakesImageData, snakesVariableData = ({},)*2
clock = pygame.time.Clock()
FPS = 100

# Bridge variables: -------------------------------------------------------------------------------------------------------
settingsPage = False
userGuidePage = False
onHomeButton = False
bridgeHome_1 = pygame.image.load('DataFile/Battleships_images/HomeButton.png')
bridgeHome_1 = pygame.transform.scale(bridgeHome_1, (100, 100))
bridgeHome_2 = pygame.image.load('DataFile/Battleships_images/HomeButton2.png')
bridgeHome_2 = pygame.transform.scale(bridgeHome_2, (100, 100))

# Battleships content: -------------------------------------------------------------------------------------------------
"""
    Dear Reader: Comments are placed throughout the code. Some are explanations for certain sections of the code,
others are simply markers for enhanced readability.

Note: I understand that sections of large and repetitive chunks of code CAN be condensed using 'class' or/and 'for'
loops or/and lists. However, because of the limit of time, further condensation could perhaps be performed by future
programmers
"""
run_battleship = True  # Variable set in parent/bridge code when initiating the battleship sup-program
goToHome = False

# Memory content: ------------------------------------------------------------------------------------------------------
# Game Development in Python 3 With PyGame series by sentdex  (youtuber)
# Background Images
sunset = pygame.image.load("DataFile/IMAGES/SUNSET_.png")                     # Selection Screen
Space = pygame.image.load("DataFile/IMAGES/OuterSpace.png")                   # Easy mode Screen
table = pygame.image.load("DataFile/IMAGES/medium_mode_bg.png")               # Medium mode Screen
maths_background = pygame.image.load("DataFile/IMAGES/maths background.png")  # Hard mode Screen
snowyMountain = pygame.image.load("DataFile/IMAGES/snow.png")
snowyMountain = pygame.transform.scale(snowyMountain, (1100, 605))
strangePlanets = pygame.image.load("DataFile/IMAGES/StrangePlanets.png")
strangePlanets = pygame.transform.scale(strangePlanets, (1100, 605))

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
memory = False
intro = True

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

# Snakes and Ladders content: ------------------------------------------------------------------------------------------

# Calling Images and variables from lists within game-related folders (snakes_image_list)
class Bunch(object):
    def __init__(self, adict):
        self.__dict__.update(adict)


with open(snakes_image_list) as f:
    helpLines = 0
    lines = f.read().splitlines()
    for item in lines:
        # Reset temporary variables:
        resetCounter = 0
        varName = ""
        imageName = ""
        sizeX = 0
        sizeY = 0
        helpLines += 1
        if helpLines > 3:
            dataSet = item.split(",")
            for data in dataSet:
                resetCounter += 1
                if resetCounter == 1:
                    varName = data
                elif resetCounter == 2:
                    imageName = (data + ".png")
                elif resetCounter == 3:
                    sizeX = int(data)
                else:
                    sizeY = int(data)
            snakesImageData[varName] = pygame.transform.scale(pygame.image.load(snakes_image_dir + imageName).convert_alpha(),(sizeX, sizeY))
            vars = Bunch(snakesImageData)

# Calling Images and variables from lists within game-related folders (snakes_variable_list)
with open(snakes_variable_list) as f:
    helpLines = 0
    lines = f.read().splitlines()
    for item in lines:
        resetCounter = 0
        varName = False
        value = False
        helpLines += 1
        if helpLines > 3:
            dataSet = item.split(" = ")
            for data in dataSet:
                resetCounter += 1
                if resetCounter == 1:
                    varName = data
                if resetCounter == 2:
                    if data == "Nothing":
                        value = str(data)
                    elif data == "True":
                        value = True
                    elif data == "False":
                        value = False
                    elif data[0] != "(":
                        value = int(data)
            snakesVariableData[varName] = value
            vars2 = Bunch(snakesVariableData)

# Manual variable declaration of player character stats and general variables
rankOne, rankTwo, rankThree, rankFour, rank1Pos, rank2Pos, rank3Pos, rank4Pos = (0,)*8
rank1Image, rank2Image, rank3Image, rank4Image, chosenGame = ("",)*5
tutorialPage, iter1 = (1,)*2
leaveBridge, bridgeHover, settingsHover, memoryHover, snakesHover, battleshipsHover, transition, loadingSequence = (False,)*8

# Lists of board, snakes, ladders positions and general lists
playerList, posList = ([],)*2
boardPosList = [(1, 280, 530), (2, 336, 530), (3, 393, 530), (4, 449, 530), (5, 505, 530), (6, 561, 530), (7, 617, 530),(8, 673, 530), (9, 729, 530), (10, 785, 530), (11, 785, 475), (12, 729, 475), (13, 673, 475),(14, 617, 475), (15, 561, 475), (16, 505, 475), (17, 449, 475), (18, 393, 475), (19, 336, 475),(20, 280, 475), (21, 280, 419), (22, 336, 419), (23, 393, 419), (24, 449, 419), (25, 505, 419),(26, 561, 419), (27, 617, 419), (28, 673, 419), (29, 729, 419), (30, 785, 419), (31, 785, 362),(32, 729, 362), (33, 673, 362), (34, 617, 362), (35, 561, 362), (36, 505, 362), (37, 449, 362),(38, 393, 362), (39, 336, 362), (40, 280, 362), (41, 280, 306), (42, 336, 306), (43, 393, 306),(44, 449, 306), (45, 505, 306), (46, 561, 306), (47, 617, 306), (48, 673, 306), (49, 729, 306),(50, 785, 306), (51, 785, 250), (52, 729, 250), (53, 673, 250), (54, 617, 250), (55, 561, 250),(56, 505, 250), (57, 449, 250), (58, 393, 250), (59, 336, 250), (60, 280, 250), (61, 280, 194),(62, 336, 194), (63, 393, 194), (64, 449, 194), (65, 505, 194), (66, 561, 194), (67, 617, 194),(68, 673, 194), (69, 729, 194), (70, 785, 194), (71, 785, 138), (72, 729, 138), (73, 673, 138),(74, 617, 138), (75, 561, 138), (76, 505, 138), (77, 449, 138), (78, 393, 138), (79, 336, 138),(80, 280, 138), (81, 280, 82), (82, 336, 82), (83, 393, 82), (84, 449, 82), (85, 505, 82),(86, 561, 82), (87, 617, 82), (88, 673, 82), (89, 729, 82), (90, 785, 82), (91, 785, 26),(92, 729, 26), (93, 673, 26), (94, 617, 26), (95, 561, 26), (96, 505, 26), (97, 449, 26),(98, 393, 26), (99, 336, 26), (100, 280, 26)]
easyBoardLadders = [(14, 48), (17, 38), (43, 59), (56, 75), (73, 89)]
easyBoardSnakes = [(23, 19), (32, 11), (55, 47), (83, 62), (97, 85)]
toughBoardLadders = [(4, 38), (14, 28), (43, 59), (50, 52), (68, 89), (86, 94)]
toughBoardSnakes = [(16, 6), (23, 19), (32, 11), (55, 47), (83, 62), (93, 87), (97, 85)]
hardBoardLadders = [(3, 17), (14, 28), (43, 59), (50, 52), (68, 72), (86, 94)]
hardBoardSnakes = [(16, 6), (32, 11), (36, 26), (39, 21), (66, 56), (83, 62), (89, 70), (93, 87), (98, 82)]
deathBoardLadders = [(3, 17), (14, 28), (24, 38), (42, 60), (50, 52), (63, 77), (68, 72)]
deathBoardSnakes = [(20, 2), (16, 6), (12, 8), (32, 11), (39, 21), (46, 25), (49, 33), (56, 44), (59, 43), (79, 61),(76, 34), (83, 62), (89, 70), (93, 87), (97, 85), (98, 82)]
clr2 = ["RedMale", "GreenMale", "BlueMale", "YellowMale", "RedFemale", "GreenFemale", "BlueFemale", "YellowFemale", "WhiteMale", "BlackFemale"]
winImages = ["red_Male", "green_Male", "blue_Male", "yellow_Male", "red_Female", "green_Female", "blue_Female", "yellow_Female", "white_Male", "black_Female"]

# Main function for the Snakes and Ladders game
def main_function():
    pygame.init()

    # Function to check for events within the pygame window (Essential to not crashing the window)
    def events():

        # The first part of the event.get() if statements are for the GUI hover effects
        for event in pygame.event.get():

            # Global variable declaration
            global rank1Pos, rank2Pos, rank3Pos, rank4Pos, posList, playerList, tutorialPage, bridgeHover, settingsHover, memoryHover, snakesHover, battleshipsHover, transition, chosenGame, leaveBridge, userGuidePage, settingsPage

            # Getting the x and y coordinates of the mouse pointer
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Bridge application effects
            if display.get_at((mouse_x, mouse_y)) == (30, 181, 103, 255) or display.get_at((mouse_x, mouse_y)) == (190, 255, 221, 255) or display.get_at((mouse_x, mouse_y)) == (125, 125, 125, 255) or display.get_at((mouse_x, mouse_y)) == (255, 255, 255, 255):
                bridgeHover = True
            else:
                bridgeHover = False
            if display.get_at((mouse_x, mouse_y)) == (255, 195, 220, 255) or display.get_at((mouse_x, mouse_y)) == (219, 91, 142, 255) or display.get_at((mouse_x, mouse_y)) == (105, 105, 105, 255) or display.get_at((mouse_x, mouse_y)) == (240, 240, 240, 255):
                settingsHover = True
            else:
                settingsHover = False
            if display.get_at((mouse_x, mouse_y)) == (255, 225, 192, 255) or display.get_at((mouse_x, mouse_y)) == (202, 123, 32, 255) or display.get_at((mouse_x, mouse_y)) == (42, 42, 42, 255) or display.get_at((mouse_x, mouse_y)) == (166, 166, 166, 255):
                memoryHover = True
            else:
                memoryHover = False
            if display.get_at((mouse_x, mouse_y)) == (252, 255, 157, 255) or display.get_at((mouse_x, mouse_y)) == (195, 200, 57, 255) or display.get_at((mouse_x, mouse_y)) == (225, 225, 225, 255) or display.get_at((mouse_x, mouse_y)) == (70, 70, 70, 255):
                snakesHover = True
            else:
                snakesHover = False
            if display.get_at((mouse_x, mouse_y)) == (198, 247, 255, 255) or display.get_at((mouse_x, mouse_y)) == (91, 177, 247, 255) or display.get_at((mouse_x, mouse_y)) == (153, 153, 153, 255) or display.get_at((mouse_x, mouse_y)) == (215, 215, 215, 255)or display.get_at((mouse_x, mouse_y)) == (181, 236, 255, 255):
                battleshipsHover = True
            else:
                battleshipsHover = False

            # Game main menu buttons
            if vars2.mainMenu:
                if 894 <= mouse_x <= 1041 and 34 <= mouse_y <= 76:
                    if not vars2.modeHover:
                        vars2.modeHover = True
                elif 906 <= mouse_x <= 1026 and 336 <= mouse_y <= 367:
                    if not vars2.musicHover:
                        vars2.musicHover = True
                elif 894 <= mouse_x <= 1038 and 431 <= mouse_y <= 465:
                    if not vars2.themeHover:
                        vars2.themeHover = True
                elif 902 <= mouse_x <= 1031 and 530 <= mouse_y <= 565:
                    if not vars2.colourHover:
                        vars2.colourHover = True
                elif 745 <= mouse_x <= 784 and 464 <= mouse_y <= 517:
                    if not vars2.homeHover:
                        vars2.homeHover = True
                else:
                    vars2.modeHover, vars2.musicHover, vars2.themeHover, vars2.colourHover, vars2.homeHover = (False,)*5

            # Music button effects for in-game
            if vars2.gameInProgress2 or vars2.settingsApplied:
                if 79 <= mouse_x <= 200 and 238 <= mouse_y <= 276:
                    if not vars2.musicHover:
                        vars2.musicHover = True
                else:
                    vars2.musicHover = False

            # Tutorial button effects
            if tutorialPage and not tutorialPage == 5 and vars2.firstTime:
                if 75 <= mouse_x <= 182 and 197 <= mouse_y <= 248:
                    if not vars2.skipHover:
                        vars2.skipHover = True
                elif 72 <= mouse_x <= 182 and 335 <= mouse_y <= 388:
                    if not vars2.nextHover:
                        vars2.nextHover = True
                else:
                    vars2.skipHover = False
                    vars2.nextHover = False
            elif tutorialPage and tutorialPage == 5 and vars2.firstTime:
                if 54 <= mouse_x <= 203 and 523 <= mouse_y <= 573:
                    if not vars2.finishHover:
                        vars2.finishHover = True
                else:
                    vars2.finishHover = False

            # Button highlight effects for mainmenu
            if vars2.modeSelect or vars2.themeSelect or vars2.musicSelect or vars2.colourSelect:
                if 91 <= mouse_x <= 116 and 110 <= mouse_y <= 136 and not vars2.gameInProgress and not vars2.gameInProgress2:
                    if not vars2.boxHover:
                        vars2.boxHover = True
                elif 91 <= mouse_x <= 116 and 168 <= mouse_y <= 195 and not vars2.gameInProgress and not vars2.gameInProgress2:
                    if not vars2.box2Hover:
                        vars2.box2Hover = True
                elif 90 <= mouse_x <= 117 and 317 <= mouse_y <= 344:
                    if not vars2.boxHover:
                        vars2.boxHover = True
                elif 90 <= mouse_x <= 117 and 370 <= mouse_y <= 397:
                    if not vars2.box2Hover:
                        vars2.box2Hover = True
                elif 91 <= mouse_x <= 116 and 225 <= mouse_y <= 252 and vars2.colourSelect and not vars2.gameInProgress and not vars2.gameInProgress2:
                    if not vars2.box3Hover:
                        vars2.box3Hover = True
                elif 91 <= mouse_x <= 116 and 283 <= mouse_y <= 310 and vars2.colourSelect and not vars2.gameInProgress and not vars2.gameInProgress2:
                    if not vars2.box4Hover:
                        vars2.box4Hover = True
                else:
                    vars2.boxHover, vars2.box2Hover, vars2.box3Hover, vars2.box4Hover = (False,)*4

            # General button effects for in-game
            if vars2.gameInProgress or vars2.gameInProgress2:
                if 922 <= mouse_x <= 1006 and 531 <= mouse_y <= 567:
                    if not vars2.rollHover:
                        vars2.rollHover = True
                elif 81 <= mouse_x <= 205 and 40 <= mouse_y <= 69:
                    if not vars2.pauseHover:
                        vars2.pauseHover = True
                elif 80 <= mouse_x <= 196 and 132 <= mouse_y <= 170:
                    if not vars2.menuHover:
                        vars2.menuHover = True
                elif 58 <= mouse_x <= 220 and 41 <= mouse_y <= 76:
                    if not vars2.resumeHover and vars2.gamePaused:
                        vars2.resumeHover = True
                elif 77 <= mouse_x <= 199 and 531 <= mouse_y <= 575 and vars2.gameInProgress:
                    if not vars2.applyHover:
                        vars2.applyHover = True
                else:
                    vars2.rollHover, vars2.pauseHover, vars2.menuHover, vars2.resumeHover = (False,)*4
                    if vars2.gameInProgress:
                        vars2.applyHover = False

                # Hover effects for player character customisation; gender + colour + game mode
                if vars2.gameInProgress:
                    if 114 <= mouse_x <= 135 and 257 <= mouse_y <= 277:
                        if not vars2.maleHover:
                            vars2.maleHover = True
                    elif 114 <= mouse_x <= 135 and 318 <= mouse_y <= 338:
                        if not vars2.maleHover2:
                            vars2.maleHover2 = True
                    elif 114 <= mouse_x <= 135 and 380 <= mouse_y <= 400:
                        if not vars2.maleHover3:
                            vars2.maleHover3 = True
                    elif 114 <= mouse_x <= 135 and 441 <= mouse_y <= 461:
                        if not vars2.maleHover4:
                            vars2.maleHover4 = True
                    elif 114 <= mouse_x <= 135 and 284 <= mouse_y <= 304:
                        if not vars2.femaleHover:
                            vars2.femaleHover = True
                    elif 114 <= mouse_x <= 135 and 345 <= mouse_y <= 365:
                        if not vars2.femaleHover2:
                            vars2.femaleHover2 = True
                    elif 114 <= mouse_x <= 135 and 407 <= mouse_y <= 427:
                        if not vars2.femaleHover3:
                            vars2.femaleHover3 = True
                    elif 114 <= mouse_x <= 135 and 467 <= mouse_y <= 487:
                        if not vars2.femaleHover4:
                            vars2.femaleHover4 = True
                    elif 162 <= mouse_x <= 182 and 257 <= mouse_y <= 277:
                        if not vars2.redHover:
                            vars2.redHover = True
                    elif 162 <= mouse_x <= 182 and 318 <= mouse_y <= 338:
                        if not vars2.redHover2:
                            vars2.redHover2 = True
                    elif 162 <= mouse_x <= 182 and 380 <= mouse_y <= 400:
                        if not vars2.redHover3:
                            vars2.redHover3 = True
                    elif 162 <= mouse_x <= 182 and 441 <= mouse_y <= 461:
                        if not vars2.redHover4:
                            vars2.redHover4 = True
                    elif 162 <= mouse_x <= 182 and 284 <= mouse_y <= 304:
                        if not vars2.blueHover:
                            vars2.blueHover = True
                    elif 162 <= mouse_x <= 182 and 345 <= mouse_y <= 365:
                        if not vars2.blueHover2:
                            vars2.blueHover2 = True
                    elif 162 <= mouse_x <= 182 and 407 <= mouse_y <= 427:
                        if not vars2.blueHover3:
                            vars2.blueHover3 = True
                    elif 162 <= mouse_x <= 182 and 467 <= mouse_y <= 487:
                        if not vars2.blueHover4:
                            vars2.blueHover4 = True
                    elif 190 <= mouse_x <= 210 and 257 <= mouse_y <= 277:
                        if not vars2.greenHover:
                            vars2.greenHover = True
                    elif 190 <= mouse_x <= 210 and 318 <= mouse_y <= 338:
                        if not vars2.greenHover2:
                            vars2.greenHover2 = True
                    elif 190 <= mouse_x <= 210 and 380 <= mouse_y <= 400:
                        if not vars2.greenHover3:
                            vars2.greenHover3 = True
                    elif 190 <= mouse_x <= 210 and 441 <= mouse_y <= 461:
                        if not vars2.greenHover4:
                            vars2.greenHover4 = True
                    elif 190 <= mouse_x <= 210 and 284 <= mouse_y <= 304:
                        if not vars2.yellowHover:
                            vars2.yellowHover = True
                    elif 190 <= mouse_x <= 210 and 345 <= mouse_y <= 365:
                        if not vars2.yellowHover2:
                            vars2.yellowHover2 = True
                    elif 190 <= mouse_x <= 210 and 407 <= mouse_y <= 427:
                        if not vars2.yellowHover3:
                            vars2.yellowHover3 = True
                    elif 190 <= mouse_x <= 210 and 467 <= mouse_y <= 487:
                        if not vars2.yellowHover4:
                            vars2.yellowHover4 = True
                    elif 85 <= mouse_x <= 102 and 229 <= mouse_y <= 247:
                        if not vars2.twoPlayerHover:
                            vars2.twoPlayerHover = True
                    elif 134 <= mouse_x <= 150 and 229 <= mouse_y <= 247:
                        if not vars2.threePlayerHover:
                            vars2.threePlayerHover = True
                    elif 182 <= mouse_x <= 200 and 229 <= mouse_y <= 247:
                        if not vars2.fourPlayerHover:
                            vars2.fourPlayerHover = True
                    else:
                        vars2.twoPlayerHover, vars2.threePlayerHover, vars2.fourPlayerHover, vars2.maleHover, vars2.maleHover2, vars2.maleHover3, vars2.maleHover4, vars2.femaleHover, vars2.femaleHover2, vars2.femaleHover3, vars2.femaleHover4, vars2.redHover, vars2.redHover2, vars2.redHover3, vars2.redHover4, vars2.blueHover, vars2.blueHover2, vars2.blueHover3, vars2.blueHover4, vars2.greenHover, vars2.greenHover2, vars2.greenHover3, vars2.greenHover4, vars2.yellowHover, vars2.yellowHover2, vars2.yellowHover3, vars2.yellowHover4 = (False,)*27

                # Card Hover Effects
                if vars2.settingsApplied or vars2.gameInProgress2:
                    if 876 <= mouse_x <= 922 and 36 <= mouse_y <= 112:
                        if not vars2.cardOneHover:
                            vars2.cardOneHover = True
                    elif 945 <= mouse_x <= 990 and 36 <= mouse_y <= 112:
                        if not vars2.cardTwoHover:
                            vars2.cardTwoHover = True
                    elif 1014 <= mouse_x <= 1059 and 36 <= mouse_y <= 112:
                        if not vars2.cardThreeHover:
                            vars2.cardThreeHover = True
                    elif 876 <= mouse_x <= 922 and 144 <= mouse_y <= 220:
                        if not vars2.cardFourHover:
                            vars2.cardFourHover = True
                    elif 945 <= mouse_x <= 990 and 144 <= mouse_y <= 220:
                        if not vars2.cardFiveHover:
                            vars2.cardFiveHover = True
                    elif 1014 <= mouse_x <= 1059 and 144 <= mouse_y <= 220:
                        if not vars2.cardSixHover:
                            vars2.cardSixHover = True
                    else:
                        vars2.cardOneHover, vars2.cardTwoHover, vars2.cardThreeHover, vars2.cardFourHover, vars2.cardFiveHover, vars2.cardSixHover = (False,)*6

            # This is for when the player chooses to exit the program
            if event.type == pygame.QUIT:
                pygame.quit(), sys.exit()

            # This is for the individual button clicking events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if onHomeButton:
                    settingsPage, userGuidePage = False, False
                    #pygame.time.wait(200)

                # Checking which page is enabled and eventually going to the according function
                if bridgeHover:
                    userGuidePage = True
                elif settingsHover:
                    settingsPage = True
                elif memoryHover:
                    transition = True
                    chosenGame = "memory"
                elif snakesHover:
                    transition = True
                    chosenGame = "snakes"
                elif battleshipsHover:
                    transition = True
                    chosenGame = "ships"

                # Tutorial button events such as skipping, going to next page
                if not tutorialPage == 5 and vars2.firstTime:
                    if 75 <= mouse_x <= 182 and 197 <= mouse_y <= 248:
                        vars2.firstTime = False
                        vars2.mainMenu = True
                    elif 72 <= mouse_x <= 182 and 335 <= mouse_y <= 388:
                        tutorialPage += 1
                    else:
                        vars2.skipHover = False
                        vars2.nextHover = False
                elif tutorialPage == 5 and vars2.firstTime:
                    if 54 <= mouse_x <= 203 and 523 <= mouse_y <= 573:
                        vars2.firstTime = False
                        vars2.mainMenu = True

                # Sound effect for when the player character moves on the board
                if vars2.gameInProgress2 or vars2.settingsApplied:
                    if 79 <= mouse_x <= 200 and 238 <= mouse_y <= 276 and not vars2.musicSelect:
                        vars2.musicSelect = True
                        t = threading.Thread(target=sleeper, name='sleeperFunction', args=(0.5, 'sleeperFunction', True, False, False, False, True, False, False, False, False))
                        t.start()
                    elif 79 <= mouse_x <= 200 and 238 <= mouse_y <= 276 and vars2.musicSelect and not vars2.pauseDebounce:
                        vars2.musicSelect = False

                # Playing music repeatitively and fading out for in-game
                if 90 <= mouse_x <= 117 and 317 <= mouse_y <= 344:
                    if vars2.musicSelect and vars2.gameInProgress2 or vars2.settingsApplied:
                        vars2.musicOff, vars2.musicOn = False, True
                        pygame.mixer.music.play(-1)
                elif 90 <= mouse_x <= 117 and 370 <= mouse_y <= 397:
                    if vars2.musicSelect and vars2.gameInProgress2 or vars2.settingsApplied:
                        vars2.musicOff, vars2.musicOn = True, False
                        t = threading.Thread(target=sleeper, name='sleeperFunction', args=(2000, 'sleeperFunction', False, False, False, False, False, False, False, False, True))
                        t.start()

                # Theme buttons, changing music, and choosing board difficulty
                if 91 <= mouse_x <= 116 and 110 <= mouse_y <= 136:
                    if vars2.modeSelect:
                        vars2.single, vars2.multi, vars2.modeSelected = False, True, True
                    elif vars2.themeSelect:
                        vars2.theme2, vars2.theme1, vars2.musicPlaying = False, True, False
                    elif vars2.musicSelect and not vars2.gameInProgress2 and not vars2.settingsApplied:
                        vars2.musicOff, vars2.musicOn = False, True
                        if vars2.theme1:
                            pygame.mixer.music.load(snakes_image_dir + "Theme1Music.mp3")
                            pygame.mixer.music.play(-1)
                        elif vars2.theme2:
                            pygame.mixer.music.load(snakes_image_dir + "Theme2Music.mp3")
                            pygame.mixer.music.play(-1)
                    elif vars2.colourSelect:
                        colour_normalise()
                        vars2.colorRedEasy = True

                # Buttons to activate singleplayer and multiplayer modes and changing board difficulty
                elif 91 <= mouse_x <= 116 and 168 <= mouse_y <= 195:
                    if vars2.modeSelect:
                        vars2.multi, vars2.single, vars2.modeSelected = False, True, True
                    elif vars2.themeSelect:
                        vars2.theme1, vars2.theme2, vars2.musicPlaying = False, True, False
                    elif vars2.musicSelect and not vars2.gameInProgress2 and not vars2.settingsApplied:
                        vars2.musicOn, vars2.musicOff = False, True
                        t = threading.Thread(target=sleeper, name='sleeperFunction', args=(1, 'sleeperFunction', False, False, False, False, False, False, False, False, True))
                        t.start()
                    elif vars2.colourSelect:
                        colour_normalise()
                        vars2.colorBlueTough = True
                elif 91 <= mouse_x <= 116 and 225 <= mouse_y <= 252:
                    if vars2.colourSelect:
                        colour_normalise()
                        vars2.colorGreenHard = True
                elif 91 <= mouse_x <= 116 and 283 <= mouse_y <= 310:
                    if vars2.colourSelect:
                        colour_normalise()
                        vars2.colorYellowDeath = True

                # Buttons to allow player to begin the multiplayer game or singleplayer game
                elif 894 <= mouse_x <= 1041 and 34 <= mouse_y <= 76:
                    if vars2.mainMenu and not vars2.modeSelected:
                        menu_button_normalise()
                        vars2.modeSelect = True
                    elif vars2.mainMenu and vars2.modeSelected and vars2.multi:
                        menu_button_normalise()
                        vars2.gameInProgress = True
                    elif vars2.mainMenu and vars2.modeSelected and vars2.single:
                        menu_button_normalise()
                        vars2.gameInProgress2, vars2.onePlayerMode = (True,)*2
                        t = threading.Thread(target=sleeper, name='sleeperFunction', args=(1, 'sleeperFunction', True, False, False, False, False, False, True, False, False))
                        t.start()

                # Main menu buttons such as music and theme
                elif 906 <= mouse_x <= 1026 and 336 <= mouse_y <= 367:
                    if vars2.mainMenu:
                        menu_button_normalise()
                        vars2.musicSelect = True
                elif 894 <= mouse_x <= 1038 and 431 <= mouse_y <= 465:
                    if vars2.mainMenu:
                        menu_button_normalise()
                        vars2.themeSelect = True

                # Normally, this would go back to bridge application, but this will exit the program
                elif 745 <= mouse_x <= 784 and 464 <= mouse_y <= 517:
                    if vars2.mainMenu and not vars2.colourSelect and not vars2.gameInProgress and not vars2.gameInProgress2:
                        vars2.firstTime, leaveBridge, chosenGame, tutorialPage = True, False, "", 1
                        pygame.mixer_music.stop(), menu_button_normalise()

                # Button to reveal difficulty options
                elif 902 <= mouse_x <= 1031 and 530 <= mouse_y <= 565 and not vars2.settingsApplied and not vars2.gameInProgress2:
                    if vars2.mainMenu:
                        menu_button_normalise()
                        vars2.colourSelect = True

                # Buttons to pause and resume the game
                elif 81 <= mouse_x <= 205 and 40 <= mouse_y <= 69 and not vars2.gamePaused:
                    if vars2.gameInProgress or vars2.gameInProgress2 and not vars2.gameOver:
                        vars2.gamePaused, vars2.resumeHover = (True,)*2
                        t = threading.Thread(target=sleeper, name='sleeperFunction', args=(0.5, 'sleeperFunction', True, False, False, False, True, False, False, False, False))
                        t.start()
                elif 58 <= mouse_x <= 220 and 41 <= mouse_y <= 76 and vars2.gamePaused:
                    if not vars2.pauseDebounce and vars2.gameInProgress or vars2.gameInProgress2 and not vars2.gameOver:
                        vars2.gamePaused = False

                # Resetting variables and lists for when player quits the game
                elif 80 <= mouse_x <= 196 and 132 <= mouse_y <= 170:
                    if vars2.gameInProgress or vars2.gameInProgress2:
                        game_button_normalise()
                        vars2.menuHover = False
                        if vars2.gameInProgress2:
                            vars2.gameInProgress2 = False
                        elif vars2.gameInProgress:
                            vars2.gameInProgress = False
                        playerList, vars2.musicSelect = [], False

                # Multi-threading to allow players to move on the board in 0.2 second time gaps
                elif 922 <= mouse_x <= 1006 and 531 <= mouse_y <= 567:
                    if vars2.settingsApplied or vars2.gameInProgress2 and not vars2.gamePaused and not vars2.movement:
                        if vars2.card1Selected or vars2.card2Selected or vars2.card3Selected or vars2.card4Selected or vars2.card5Selected or vars2.card6Selected:
                            if vars2.currentRoller == rankOne and not vars2.onePlayerMode:
                                t = threading.Thread(target=sleeper, name='sleeperFunction', args=(0.2, 'sleeperFunction', True, False, False, False, False, True, False, False, False))
                                t.start()
                            elif vars2.currentRoller == rankTwo and not vars2.onePlayerMode:
                                t = threading.Thread(target=sleeper, name='sleeperFunction', args=(0.2, 'sleeperFunction', False, True, False, False, False, True, False, False, False))
                                t.start()
                            elif vars2.currentRoller == rankOne and vars2.onePlayerMode:
                                t = threading.Thread(target=sleeper, name='sleeperFunction', args=(0.2, 'sleeperFunction', True, False, False, False, False, True, False, False, False))
                                t.start()
                            elif vars2.currentRoller == rankThree:
                                t = threading.Thread(target=sleeper, name='sleeperFunction', args=(0.2, 'sleeperFunction', False, False, True, False, False, True, False, False, False))
                                t.start()
                            elif vars2.currentRoller == rankFour:
                                t = threading.Thread(target=sleeper, name='sleeperFunction', args=(0.2, 'sleeperFunction', False, False, False, True, False, True, False, False, False))
                                t.start()
                            vars2.card1Selected, vars2.card2Selected, vars2.card3Selected, vars2.card4Selected, vars2.card5Selected, vars2.card6Selected = (False,)*6
                            vars2.rollNumber = 0

                            # Changing the global variable values to indicate player position
                            if vars2.currentTurn != 2 and vars2.onePlayerMode:
                                vars2.currentTurn += 1
                            elif vars2.currentTurn == 2 and vars2.onePlayerMode:
                                vars2.currentTurn = 1

                            if vars2.currentTurn != 2 and vars2.twoPlayerMode:
                                vars2.currentTurn += 1
                            elif vars2.currentTurn == 2 and vars2.twoPlayerMode:
                                vars2.currentTurn = 1

                            if vars2.currentTurn != 3 and vars2.threePlayerMode:
                                vars2.currentTurn += 1
                            elif vars2.currentTurn == 3 and vars2.threePlayerMode:
                                vars2.currentTurn = 1

                            if vars2.currentTurn != 4 and vars2.fourPlayerMode:
                                vars2.currentTurn += 1
                            elif vars2.currentTurn == 4 and vars2.fourPlayerMode:
                                vars2.currentTurn = 1

                # Button for confirming the player customisation options in multiplayer mode
                elif 77 <= mouse_x <= 199 and 531 <= mouse_y <= 575:
                    if vars2.gameInProgress:
                        if vars2.twoPlayerMode:
                            if (vars2.redSelect or vars2.blueSelect or vars2.greenSelect or vars2.yellowSelect) and (vars2.redSelect2 or vars2.blueSelect2 or vars2.greenSelect2 or vars2.yellowSelect2):
                                vars2.settingsApplied = True
                        elif vars2.threePlayerMode:
                            if (vars2.redSelect or vars2.blueSelect or vars2.greenSelect or vars2.yellowSelect) and (vars2.redSelect2 or vars2.blueSelect2 or vars2.greenSelect2 or vars2.yellowSelect2) and (vars2.redSelect3 or vars2.blueSelect3 or vars2.greenSelect3 or vars2.yellowSelect3):
                                vars2.settingsApplied = True
                        elif vars2.fourPlayerMode:
                            if (vars2.redSelect or vars2.blueSelect or vars2.greenSelect or vars2.yellowSelect) and (vars2.redSelect2 or vars2.blueSelect2 or vars2.greenSelect2 or vars2.yellowSelect2) and (vars2.redSelect3 or vars2.blueSelect3 or vars2.greenSelect3 or vars2.yellowSelect3) and (vars2.redSelect4 or vars2.blueSelect4 or vars2.greenSelect4 or vars2.yellowSelect4):
                                vars2.settingsApplied = True

                # Changing boolean values for when the player changes their player customisation in multiplayer mode
                if vars2.gameInProgress and vars2.twoPlayerMode or vars2.threePlayerMode or vars2.fourPlayerMode:

                    # Gender customisation
                    if 114 <= mouse_x <= 135 and 257 <= mouse_y <= 277:
                        if not vars2.maleSelect:
                            player_one_gender_reset()
                            vars2.maleSelect = True
                    elif 114 <= mouse_x <= 135 and 318 <= mouse_y <= 338:
                        if not vars2.maleSelect2:
                            player_two_gender_reset()
                            vars2.maleSelect2 = True
                    elif 114 <= mouse_x <= 135 and 380 <= mouse_y <= 400:
                        if not vars2.maleSelect3:
                            player_three_gender_reset()
                            vars2.maleSelect3 = True
                    elif 114 <= mouse_x <= 135 and 441 <= mouse_y <= 461:
                        if not vars2.maleSelect4:
                            player_four_gender_reset()
                            vars2.maleSelect4 = True
                    elif 114 <= mouse_x <= 135 and 284 <= mouse_y <= 304:
                        if not vars2.femaleSelect:
                            player_one_gender_reset()
                            vars2.femaleSelect = True
                    elif 114 <= mouse_x <= 135 and 345 <= mouse_y <= 365:
                        if not vars2.femaleSelect2:
                            player_two_gender_reset()
                            vars2.femaleSelect2 = True
                    elif 114 <= mouse_x <= 135 and 407 <= mouse_y <= 427:
                        if not vars2.femaleSelect3:
                            player_three_gender_reset()
                            vars2.femaleSelect3 = True
                    elif 114 <= mouse_x <= 135 and 467 <= mouse_y <= 487:
                        if not vars2.femaleSelect4:
                            player_four_gender_reset()
                            vars2.femaleSelect4 = True

                    # Selection of the red colour in multiplayer customisation
                    elif 162 <= mouse_x <= 182 and 257 <= mouse_y <= 277:
                        if not vars2.redSelect and not vars2.redSelect2 and not vars2.redSelect3 and not vars2.redSelect4:
                            player_one_colour_reset()
                            vars2.redSelect = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 162 <= mouse_x <= 182 and 318 <= mouse_y <= 338:
                        if not vars2.redSelect2 and not vars2.redSelect and not vars2.redSelect3 and not vars2.redSelect4:
                            player_two_colour_reset()
                            vars2.redSelect2 = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 162 <= mouse_x <= 182 and 380 <= mouse_y <= 400:
                        if not vars2.redSelect3 and not vars2.redSelect and not vars2.redSelect2 and not vars2.redSelect4:
                            player_three_colour_reset()
                            vars2.redSelect3 = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 162 <= mouse_x <= 182 and 441 <= mouse_y <= 461:
                        if not vars2.redSelect4:
                            player_four_colour_reset()
                            vars2.redSelect4 = True
                            if vars2.redSelect:
                                vars2.redSelect = False
                            elif vars2.redSelect2:
                                vars2.redSelect2 = False
                            elif vars2.redSelect3:
                                vars2.redSelect3 = False

                    # Selection of the blue colour in multiplayer customisation
                    elif 162 <= mouse_x <= 182 and 284 <= mouse_y <= 304:
                        if not vars2.blueSelect and not vars2.blueSelect2 and not vars2.blueSelect3 and not vars2.blueSelect4:
                            player_one_colour_reset()
                            vars2.blueSelect = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 162 <= mouse_x <= 182 and 345 <= mouse_y <= 365:
                        if not vars2.blueSelect2 and not vars2.blueSelect and not vars2.blueSelect3 and not vars2.blueSelect4:
                            player_two_colour_reset()
                            vars2.blueSelect2 = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 162 <= mouse_x <= 182 and 407 <= mouse_y <= 427:
                        if not vars2.blueSelect3 and not vars2.blueSelect2 and not vars2.blueSelect and not vars2.blueSelect4:
                            player_three_colour_reset()
                            vars2.blueSelect3 = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 162 <= mouse_x <= 182 and 467 <= mouse_y <= 487:
                        if not vars2.blueSelect4:
                            player_four_colour_reset()
                            vars2.blueSelect4 = True
                            if vars2.blueSelect:
                                vars2.blueSelect = False
                            elif vars2.blueSelect2:
                                vars2.blueSelect2 = False
                            elif vars2.blueSelect3:
                                vars2.blueSelect3 = False

                    # Selection of the green colour in multiplayer customisation
                    elif 190 <= mouse_x <= 210 and 257 <= mouse_y <= 277:
                        if not vars2.greenSelect and not vars2.greenSelect2 and not vars2.greenSelect3 and not vars2.greenSelect4:
                            player_one_colour_reset()
                            vars2.greenSelect = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 190 <= mouse_x <= 210 and 318 <= mouse_y <= 338:
                        if not vars2.greenSelect2 and not vars2.greenSelect and not vars2.greenSelect3 and not vars2.greenSelect4:
                            player_two_colour_reset()
                            vars2.greenSelect2 = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 190 <= mouse_x <= 210 and 380 <= mouse_y <= 400:
                        if not vars2.greenSelect3 and not vars2.greenSelect2 and not vars2.greenSelect and not vars2.greenSelect4:
                            player_three_colour_reset()
                            vars2.greenSelect3 = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 190 <= mouse_x <= 210 and 441 <= mouse_y <= 461:
                        if not vars2.greenSelect4:
                            player_four_colour_reset()
                            vars2.greenSelect4 = True
                            if vars2.greenSelect:
                                vars2.greenSelect = False
                            elif vars2.greenSelect2:
                                vars2.greenSelect2 = False
                            elif vars2.greenSelect3:
                                vars2.greenSelect3 = False

                    # Selection of the yellow colour in multiplayer customisation
                    elif 190 <= mouse_x <= 210 and 284 <= mouse_y <= 304:
                        if not vars2.yellowSelect and not vars2.yellowSelect2 and not vars2.yellowSelect3 and not vars2.yellowSelect4:
                            player_one_colour_reset()
                            vars2.yellowSelect = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 190 <= mouse_x <= 210 and 345 <= mouse_y <= 365:
                        if not vars2.yellowSelect2 and not vars2.yellowSelect and not vars2.yellowSelect3 and not vars2.yellowSelect4:
                            player_two_colour_reset()
                            vars2.yellowSelect2 = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True
                    elif 190 <= mouse_x <= 210 and 407 <= mouse_y <= 427:
                        if not vars2.yellowSelect3 and not vars2.yellowSelect2 and not vars2.yellowSelect and not vars2.yellowSelect4:
                            player_three_colour_reset()
                            vars2.yellowSelect3 = True
                            vars2.colourError, vars2.colourError2 = (False,)*2
                        elif not vars2.fourPlayerMode:
                            vars2.colourError = True
                        else:
                            vars2.colourError, vars2.colourError2 = False, True

                    # A function to normalize the options (return them to default)
                    elif 190 <= mouse_x <= 210 and 467 <= mouse_y <= 487:
                        if not vars2.yellowSelect4:
                            player_four_colour_reset()
                            vars2.yellowSelect4 = True
                            if vars2.yellowSelect:
                                vars2.yellowSelect = False
                            elif vars2.yellowSelect2:
                                vars2.yellowSelect2 = False
                            elif vars2.yellowSelect3:
                                vars2.yellowSelect3 = False

                # Selection of two, three and four player modes in multiplayer mode
                if vars2.gameInProgress or vars2.gameInProgress2 and not vars2.singlePlayerWait:
                    if 85 <= mouse_x <= 102 and 229 <= mouse_y <= 247 and vars2.gameInProgress:
                        if not vars2.twoPlayerMode:
                            mode_reset()
                            vars2.twoPlayerMode, vars2.loopAmount = True, 4
                    elif 134 <= mouse_x <= 150 and 229 <= mouse_y <= 247 and vars2.gameInProgress:
                        if not vars2.threePlayerMode:
                            mode_reset()
                            vars2.threePlayerMode, vars2.loopAmount = True, 6
                    elif 182 <= mouse_x <= 200 and 229 <= mouse_y <= 247 and vars2.gameInProgress:
                        if not vars2.fourPlayerMode:
                            mode_reset()
                            vars2.fourPlayerMode, vars2.loopAmount = True, 8

                    # Card Click Events and selection events
                    if vars2.settingsApplied or vars2.gameInProgress2 and not vars2.movement:
                        if 876 <= mouse_x <= 922 and 36 <= mouse_y <= 112:
                            if not vars2.card1Selected and not vars2.card2Selected and not vars2.card3Selected and not vars2.card4Selected and not vars2.card5Selected and not vars2.card6Selected and not vars2.gamePaused and not vars2.movement:
                                vars2.card1Selected = True
                        elif 945 <= mouse_x <= 990 and 36 <= mouse_y <= 112:
                            if not vars2.card1Selected and not vars2.card2Selected and not vars2.card3Selected and not vars2.card4Selected and not vars2.card5Selected and not vars2.card6Selected and not vars2.gamePaused and not vars2.movement:
                                vars2.card2Selected = True
                        elif 1014 <= mouse_x <= 1059 and 36 <= mouse_y <= 112:
                            if not vars2.card1Selected and not vars2.card2Selected and not vars2.card3Selected and not vars2.card4Selected and not vars2.card5Selected and not vars2.card6Selected and not vars2.gamePaused and not vars2.movement:
                                vars2.card3Selected = True
                        elif 876 <= mouse_x <= 922 and 144 <= mouse_y <= 220:
                            if not vars2.card1Selected and not vars2.card2Selected and not vars2.card3Selected and not vars2.card4Selected and not vars2.card5Selected and not vars2.card6Selected and not vars2.gamePaused and not vars2.movement:
                                vars2.card4Selected = True
                        elif 945 <= mouse_x <= 990 and 144 <= mouse_y <= 220:
                            if not vars2.card1Selected and not vars2.card2Selected and not vars2.card3Selected and not vars2.card4Selected and not vars2.card5Selected and not vars2.card6Selected and not vars2.gamePaused and not vars2.movement:
                                vars2.card5Selected = True
                        elif 1014 <= mouse_x <= 1059 and 144 <= mouse_y <= 220:
                            if not vars2.card1Selected and not vars2.card2Selected and not vars2.card3Selected and not vars2.card4Selected and not vars2.card5Selected and not vars2.card6Selected and not vars2.gamePaused and not vars2.movement:
                                vars2.card6Selected = True
                                
    # randomising the card selection process
    seed(1)

    # Function for the entire program (the central point)
    def main_screen():
        global memory
        x = 0
        while True:
            # A continuous event that triggers to see if there is any input (prevents program from crashing)
            events()

            # Allowing the background to move vertically in a seamless manner by duplication of image at centre point
            if chosenGame == "snakes" and not transition:
                if vars2.theme1 and not vars2.firstTime:
                    rel_x = x % vars.background_Image.get_rect().width
                    display.blit(vars.background_Image, (rel_x-vars.background_Image.get_rect().width, 0))
                    if rel_x < width:
                        display.blit(vars.background_Image, (rel_x, 0))
                elif vars2.theme2 and not vars2.firstTime:
                    rel_x = x % vars.background_Image2.get_rect().width
                    display.blit(vars.background_Image2, (rel_x - vars.background_Image2.get_rect().width, 0))
                    if rel_x < width:
                        display.blit(vars.background_Image2, (rel_x, 0))
                else:
                    rel_x = x % vars.background_Image3.get_rect().width
                    display.blit(vars.background_Image3, (rel_x - vars.background_Image3.get_rect().width, 0))
                    if rel_x < width:
                        display.blit(vars.background_Image3, (rel_x, 0))
                if not vars2.gamePaused:
                    if not vars2.modeHover and not vars2.themeHover and not vars2.colourHover and not vars2.musicHover and not vars2.menuHover and not vars2.pauseHover and not vars2.rollHover and not vars2.firstTime:
                        x -= 1
                    else:
                        x -= 0.35
                else:
                    x -= 0

                # Choosing which music to play depending on the selected theme
                if not vars2.musicPlaying:
                    vars2.musicPlaying = True
                    if vars2.theme1 and vars2.musicOn:
                        pygame.mixer.music.load(snakes_image_dir + "Theme1Music.mp3")
                        pygame.mixer.music.play(-1)
                    elif vars2.theme2 and vars2.musicOn:
                        pygame.mixer.music.load(snakes_image_dir + "Theme2Music.mp3")
                        pygame.mixer.music.play(-1)

                # Allowing certain functions to take place depending on where the player is in the program
                if not vars2.gameInProgress and not vars2.gameInProgress2 and not vars2.firstTime and leaveBridge:
                    main_menu()
                elif vars2.gameInProgress:
                    main_game()
                elif vars2.gameInProgress2:
                    main_game2()
                elif vars2.firstTime and leaveBridge:
                    tutorial()

            # Checking if the program should be at the bridge or at a game (snakes, battleships, memory)
            if not leaveBridge:
                main_screen0()

            # Checks the variable 'chosenGame' or checks value of settingsPage and transition to decide which game/page the program should be at

            if chosenGame == "snakes" and not transition:
                
                # Snakes and Ladders program
                pygame.display.set_caption("Snakes and Ladders")
                pygame.display.set_icon(vars.icon_snake)
            elif chosenGame == "ships" and not transition:
                
                # battleships program
                pygame.display.set_caption("Battleships")
                pygame.display.set_icon(vars.icon_ship)
                main_battleship()
            elif chosenGame == "memory" and not transition:
                
                # Memory program
                pygame.display.set_caption("Mind Shape")
                pygame.display.set_icon(vars.icon_memory)
                if not memory:
                    memory = True
                    selection_screen()
            elif settingsPage and not transition:
                
                # Settings page
                settings_function()
                pygame.display.set_caption("Bridge")
                pygame.display.set_icon(vars.icon_bridge)
            elif userGuidePage and not transition:
                # userguide page
                userguide_function()
                pygame.display.set_caption("Bridge")
                pygame.display.set_icon(vars.icon_bridge)
            else:
                # main menu of the bridge page
                pygame.display.set_caption("Bridge")
                pygame.display.set_icon(vars.icon_bridge)

            # Function to display options based on which button is pressed on the main menu e.g theme options
            if chosenGame == "snakes" and not transition:
                if vars2.modeSelect:
                    mode_options()
                elif vars2.themeSelect:
                    theme_options()
                elif vars2.musicSelect:
                    music_options()
                elif vars2.colourSelect:
                    colour_options()

            # Constantly updating the screen to repeatedly display the images onto the pygame window
            pygame.display.update()
            clock.tick(FPS)

    # Main tutorial function
    def tutorial():

        # Global variable declaration for player stats
        global rank1Image, rank2Image, rank3Image, rank4Image, rankOne, rankTwo, rankThree, rankFour, rank1Pos, rank2Pos, rank3Pos, rank4Pos

        # Displaying the buttons in the tutorial aspect of the game
        if not vars2.nextHover and not tutorialPage == 5:
            display.blit(vars.next_Button, (20, 322))
        elif vars2.nextHover and not tutorialPage == 5:
            display.blit(vars.next_Button_Expanded, (11, 318))
        if not vars2.skipHover and not tutorialPage == 5:
            display.blit(vars.skip_Button, (20, 182))
        elif vars2.skipHover and not tutorialPage == 5:
            display.blit(vars.skip_Button_Expanded, (11, 178))

        if not vars2.finishHover and tutorialPage == 5:
            display.blit(vars.finish_Button, (20, 510))
        elif vars2.finishHover and tutorialPage == 5:
            display.blit(vars.finish_Button_Expanded, (11, 506))

        # Dictating which images to display depending on which page of the tutorial the user is in
        if tutorialPage > 0:
            display.blit(vars.dice_Roll_Box, (858, 17)), display.blit(vars.card_Four, (870, 130)), display.blit(vars.card_Five, (935, 130)), display.blit(vars.card_Six, (1000, 130))
            if tutorialPage == 1:
                display.blit(vars.card_One, (870, 25)), display.blit(vars.tut_Page1, (540, 45))
            display.blit(vars.card_Two, (935, 25)), display.blit(vars.card_Three, (1000, 25))
        if tutorialPage > 1:
            display.blit(vars.dice_Four, (867, 20)), display.blit(vars.tut_Page2, (540, 45))
        if tutorialPage > 2:
            display.blit(vars.ranking_Label, (858, 257)), display.blit(vars.white_Male, (997, 278)), display.blit(vars.black_Female, (893, 278)), display.blit(vars.tut_Page3, (540, 275))
        if tutorialPage > 3:
            display.blit(vars.roller_Label, (925, 394)), display.blit(vars.black_Female, (944, 415)), display.blit(vars.tut_Page4, (605, 413))
        if tutorialPage > 4:
            display.blit(vars.roll_Button, (858, 510)), display.blit(vars.tut_Page5, (578, 520))
            
    # Singleplayer game mode function
    def main_game2():

        # Global variable declaration for player stats
        global rank1Image, rank2Image, rank3Image, rank4Image, rankOne, rankTwo, rankThree, rankFour, rank1Pos, rank2Pos, rank3Pos, rank4Pos

        # If the game is currently running
        if not vars2.gameOver:

            # Displaying the board depending on difficulty
            if vars2.colorRedEasy:
                display.blit(vars.board_Image3, (264, 17))
            elif vars2.colorBlueTough:
                display.blit(vars.board_Image4, (264, 17))
            elif vars2.colorGreenHard:
                display.blit(vars.board_Image5, (264, 17))
            elif vars2.colorYellowDeath:
                display.blit(vars.board_Image6, (264, 17))

            # Displaying Card GUI
            if not vars2.gameOver:
                display.blit(vars.dice_Roll_Box, (858, 17)), display.blit(vars.ranking_Label, (858, 257)), display.blit(vars.roller_Label, (925, 394))
            rankOne, rank1Image, rankTwo, rank2Image = 1, 'WhiteMale', 2, 'BlackFemale'

            # Allowing the users to move their player characters
            if vars2.currentTurn == 1:
                vars2.currentRoller = rankOne
            elif vars2.currentTurn == 2 and not vars2.onePlayerMode:
                vars2.currentRoller = rankTwo
            elif vars2.currentTurn == 2 and vars2.onePlayerMode and not vars2.movement and vars2.rollNumber == 0 and not vars2.computerPause:
                if not vars2.computerPause and not vars2.movement:

                    # A thread to to start the moving process
                    computer_move()
                    t = threading.Thread(target=sleeper, name='sleeperFunction', args=(0.2, 'sleeperFunction', False, True, False, False, False, True, False, False, False))
                    t.start()

            # Displaying the player characters in first and last positions depending on their spot on the board
            posList = [rank1Pos, rank2Pos]
            if rank1Pos == max(posList):
                display.blit(vars.white_Male, (893, 278)), display.blit(vars.black_Female, (997, 278))
            elif rank1Pos == min(posList):
                display.blit(vars.white_Male, (997, 278)), display.blit(vars.black_Female, (893, 278))

            if vars2.currentTurn == 1:
                display.blit(vars.white_Male, (944, 415))
            elif vars2.currentTurn == 2:
                display.blit(vars.black_Female, (944, 415))
            display.blit(vars.white_Male, (boardPosList[rank1Pos][1], boardPosList[rank1Pos][2])), display.blit(vars.black_Female, (boardPosList[rank2Pos][1], boardPosList[rank2Pos][2]))

            # Effects and button events for the cards (dice)
            game_options()

            # Displaying text to act as a mini user-guide
            if vars2.gameInProgress2:
                display.blit(vars.card_Select_Error, (-17, 520)), display.blit(vars.roll_Error, (-17, 450))

            # Displaying music button effects
            if not vars2.musicHover:
                display.blit(vars.music_Button, (32, 217))
            else:
                display.blit(vars.music_Button_Expanded, (21, 213))

        # Checking if a player has won the game and triggering winner function
        if rank1Pos == 99:
            winner(True, False, False, False)
        elif rank2Pos == 99:
            winner(False, True, False, False)
        elif rank3Pos == 99:
            winner(False, False, True, False)
        elif rank4Pos == 99:
            winner(False, False, False, True)

        # Displaying menu button effects
        if not vars2.menuHover:
            display.blit(vars.menu_Button, (32, 117))
        else:
            display.blit(vars.menu_Button_Expanded, (21, 113))

    # Multiplayer game mode function
    def main_game():

        # Global declaration of player stat variables
        global rank1Pos, rank2Pos, rank3Pos, rank4Pos, rank1Image, rank2Image, rank3Image, rank4Image, rankOne, rankTwo, rankThree, rankFour, posList

        # Checks if game is not over
        if vars2.settingsApplied and not vars2.gameOver:

            # Displays board according to difficulty level chosen
            if vars2.colorRedEasy:
                display.blit(vars.board_Image3, (264, 17))
            elif vars2.colorBlueTough:
                display.blit(vars.board_Image4, (264, 17))
            elif vars2.colorGreenHard:
                display.blit(vars.board_Image5, (264, 17))
            elif vars2.colorYellowDeath:
                display.blit(vars.board_Image6, (264, 17))

            # Displaying music button effects
            if not vars2.musicHover:
                display.blit(vars.music_Button, (32, 217))
            else:
                display.blit(vars.music_Button_Expanded, (21, 213))
            display.blit(vars.dice_Roll_Box, (858, 17)), display.blit(vars.ranking_Label, (858, 257)), display.blit(vars.roller_Label, (925, 394))

            # Appending the custom player stats into a list in order to use them later in the code
            while len(playerList) != vars2.loopAmount:
                x = 0
                clr = ["redSelect", "greenSelect", "blueSelect", "yellowSelect"]
                random.seed()
                for i in range(10):

                    # Allows the randomisation of players (who goes first, last, etc..)
                    x = random.randint(1, 4)
                if x == 1 or x == 2 or x == 3 or x == 4:
                    if x == 1 and 1 not in playerList:
                        playerList.append(x)
                        for p in range(1, 5):
                            for z in vars2.__dict__:
                                if z == (clr[p - 1]) and vars2.__dict__[z] and vars2.maleSelect:
                                        playerList.append(clr2[p - 1])
                                elif z == (clr[p - 1]) and vars2.__dict__[z] and vars2.femaleSelect:
                                        playerList.append(clr2[p + 3])
                    elif x == 2 and 2 not in playerList:
                        playerList.append(x)
                        for p in range(1, 5):
                            for z in vars2.__dict__:
                                if z == (clr[p - 1] + str(x)) and vars2.__dict__[z] and vars2.maleSelect2:
                                        playerList.append(clr2[p - 1])
                                elif z == (clr[p - 1] + str(x)) and vars2.__dict__[z] and vars2.femaleSelect2:
                                        playerList.append(clr2[p + 3])
                    elif x == 3 and 3 not in playerList and vars2.loopAmount >= 6:
                        playerList.append(x)
                        for p in range(1, 5):
                            for z in vars2.__dict__:
                                if z == (clr[p - 1] + str(x)) and vars2.__dict__[z] and vars2.maleSelect3:
                                        playerList.append(clr2[p - 1])
                                elif z == (clr[p - 1] + str(x)) and vars2.__dict__[z] and vars2.femaleSelect3:
                                        playerList.append(clr2[p + 3])
                    elif x == 4 and 4 not in playerList and vars2.loopAmount == 8:
                        playerList.append(x)
                        for p in range(1, 5):
                            for z in vars2.__dict__:
                                if z == (clr[p - 1] + str(x)) and vars2.__dict__[z] and vars2.maleSelect4:
                                        playerList.append(clr2[p - 1])
                                elif z == (clr[p - 1] + str(x)) and vars2.__dict__[z] and vars2.femaleSelect4:
                                        playerList.append(clr2[p + 3])

            # Appending the chosen player stats into a new list
            rankOne, rank1Image, rankTwo, rank2Image, posList = playerList[0], playerList[1], playerList[2], playerList[3], [rank1Pos, rank2Pos]
            if vars2.threePlayerMode:
                rankThree, rank3Image, posList = playerList[4], playerList[5], [rank1Pos, rank2Pos, rank3Pos]
            elif vars2.fourPlayerMode:
                rankThree, rank3Image, rankFour, rank4Image, posList = playerList[4], playerList[5], playerList[6], playerList[7], [rank1Pos, rank2Pos, rank3Pos, rank4Pos]

            # Setting the player position in the game (first, second, etc...) randomly
            if vars2.currentTurn == 1:
                vars2.currentRoller = rankOne
            elif vars2.currentTurn == 2:
                vars2.currentRoller = rankTwo
            elif vars2.currentTurn == 3:
                vars2.currentRoller = rankThree
            elif vars2.currentTurn == 4:
                vars2.currentRoller = rankFour

            # Displaying the player in first, last positions and the current roller
            for j in range(1, 5):
                count = 0
                for x in clr2:
                    count += 1
                    if eval("rank" + str(j) + "Image") == x:
                        if eval("rank" + str(j) + "Pos") == max(posList):
                            display.blit(vars.__dict__[winImages[count - 1]], (893, 278))
                        elif eval("rank" + str(j) + "Pos") == min(posList):
                            display.blit(vars.__dict__[winImages[count - 1]], (997, 278))
                        if vars2.currentTurn == j:
                            display.blit(vars.__dict__[winImages[count - 1]], (944, 415))
                        display.blit(vars.__dict__[winImages[count - 1]], (boardPosList[eval("rank" + str(j) + "Pos")][1], boardPosList[eval("rank" + str(j) + "Pos")][2]))

            # Effects and button events for the cards (dice)
            game_options()

        # Checking to see if the settings for player character customisation have not been applied yet
        elif not vars2.settingsApplied and not vars2.gameOver:

            # Displaying game main menu icon depenging on chosen theme
            if vars2.theme1:
                display.blit(vars.board_Image, (264, 17)), display.blit(vars.settings_Label, (43, 195))
            elif vars2.theme2:
                display.blit(vars.board_Image2, (264, 17)), display.blit(vars.settings_Label2, (43, 195))

            # Checking the chosen mode (2, 3, 4 player)
            if vars2.twoPlayerMode:
                two_player()
            elif vars2.threePlayerMode:
                three_player()
            elif vars2.fourPlayerMode:
                four_player()

            # Displaying button highlight effects for the customisation button options
            if not vars2.twoPlayerHover:
                display.blit(vars.two_Player_Label, (94 - 11, 237 - 12))
            else:
                display.blit(vars.two_Player_Label2, (94 - 11, 237 - 12))

            if not vars2.threePlayerHover:
                display.blit(vars.three_Player_Label, (142 - 11, 237 - 12))
            else:
                display.blit(vars.three_Player_Label2, (142 - 11, 237 - 12))

            if not vars2.fourPlayerHover:
                display.blit(vars.four_Player_Label, (190 - 11, 237 - 12))
            else:
                display.blit(vars.four_Player_Label2, (190 - 11, 237 - 12))

            if not vars2.applyHover:
                display.blit(vars.apply_Button, (32, 510))
            else:
                display.blit(vars.apply_Button_Expanded, (21, 506))

            # Other display elements such as general text and buttons
            if vars2.gamePaused:
                display.blit(vars.theme_Info, (505, 396))
            elif vars2.colourError:
                display.blit(vars.colours_Error_Info, (505, 396))
            elif vars2.colourError2:
                display.blit(vars.colours_Error_Info2, (505, 396))
            else:
                display.blit(vars.stats_Info, (505, 396))

        # Checking if a player has won the game and triggering winner function
        if rank1Pos == 99:
            winner(True, False, False, False)
        elif rank2Pos == 99:
            winner(False, True, False, False)
        elif rank3Pos == 99:
            winner(False, False, True, False)
        elif rank4Pos == 99:
            winner(False, False, False, True)

        # Displaying menu button effects
        if not vars2.menuHover:
            display.blit(vars.menu_Button, (32, 117))
        else:
            display.blit(vars.menu_Button_Expanded, (21, 113))

    # This is the main menu function, basically the central point of the game itself
    def main_menu():
        if not vars2.mainMenu:
            vars2.mainMenu = True

        # Displaying design based off of selected theme
        if not vars2.colourSelect:
            if vars2.theme1:
                display.blit(vars.board_Image, (264, 17))
            elif vars2.theme2:
                display.blit(vars.board_Image2, (264, 17))

        # Displaying board depending on difficulty chosen
        elif vars2.colourSelect and vars2.colorRedEasy:
            display.blit(vars.board_Image3, (264, 17))
        elif vars2.colourSelect and vars2.colorBlueTough:
            display.blit(vars.board_Image4, (264, 17))
        elif vars2.colourSelect and vars2.colorGreenHard:
            display.blit(vars.board_Image5, (264, 17))
        elif vars2.colourSelect and vars2.colorYellowDeath:
            display.blit(vars.board_Image6, (264, 17))

        # Displaying button hover and normal effects for play and select button
        if not vars2.modeHover and not vars2.multi and not vars2.single:
            display.blit(vars.select_Button, (858, 17))
        elif vars2.modeHover and not vars2.multi and not vars2.single:
            display.blit(vars.select_Button_Expanded, (849, 13))
        elif not vars2.modeHover and (vars2.multi or vars2.single):
            display.blit(vars.play_Button, (861, 17))
        elif vars2.modeHover and (vars2.multi or vars2.single):
            display.blit(vars.play_Button_Expanded, (850, 13))

        # Displaying button hover and normal effects for music button
        if not vars2.musicHover:
            display.blit(vars.music_Button, (858, 310))
        else:
            display.blit(vars.music_Button_Expanded, (847, 306))

        # Displaying button hover and normal effects for theme button
        if not vars2.themeHover:
            display.blit(vars.themes_Button, (858, 410))
        else:
            display.blit(vars.themes_Button_Expanded, (847, 406))

        # Displaying button hover and normal effects for theme button
        if not vars2.colourHover:
            display.blit(vars.boards_Button, (858, 510))
        else:
            display.blit(vars.boards_Button_Expanded, (847, 506))

        # Displaying button hover and normal effects for home button
        if not vars2.homeHover and not vars2.colourSelect:
            display.blit(vars.home_Button, (724, 450))
        elif vars2.homeHover and not vars2.colourSelect:
            display.blit(vars.home_Button2, (724, 450))

        # Displaying general buttons in the main menu for players to customise their game-play
        if vars2.themeSelect:
            display.blit(vars.theme_Info, (505, 396))
        elif vars2.colourSelect:
            display.blit(vars.boards_Info, (-17, 520))
        elif vars2.musicSelect:
            display.blit(vars.music_Info, (505, 396))
        elif vars2.modeSelect:
            display.blit(vars.mode_Info, (505, 396))

    # The function for displaying the mode types; single and multiplayer
    def mode_options():
        display.blit(vars.mode_Label, (32, 17)), display.blit(vars.multi_Label, (62, 85)), display.blit(vars.box_Button, (-5, 83)), display.blit(vars.single_Label, (62, 143)), display.blit(vars.box2_Button, (-5, 141))

        # Displaying the check boxes for multiplayer
        if not vars2.boxHover and vars2.multi:
            display.blit(vars.box_Button, (-5, 83)), display.blit(vars.box_Button_Ticked, (-5, 83))
        elif vars2.boxHover and vars2.multi:
            display.blit(vars.box_Button2, (-5, 83)), display.blit(vars.box_Button_Ticked, (-5, 83))
        elif not vars2.boxHover:
            display.blit(vars.box_Button, (-5, 83))
        else:
            display.blit(vars.box_Button2, (-5, 83))

        # Displaying the check boxes for singleplayer
        if not vars2.box2Hover and vars2.single:
            display.blit(vars.box2_Button, (-5, 141)), display.blit(vars.box_Button_Ticked, (-5, 141))
        elif vars2.box2Hover and vars2.single:
            display.blit(vars.box2_Button2, (-5, 141)), display.blit(vars.box_Button_Ticked, (-5, 141))
        elif not vars2.box2Hover:
            display.blit(vars.box2_Button, (-5, 141))
        else:
            display.blit(vars.box2_Button2, (-5, 141))

    # The main function for displaying the themes
    def theme_options():
        display.blit(vars.themes_Button, (32, 17)), display.blit(vars.theme1_Label, (80, 85)), display.blit(vars.box_Button, (-5, 83)), display.blit(vars.theme2_Label, (80, 143)), display.blit(vars.box2_Button, (-5, 141))

        # Displaying the check boxes for the first theme (green and yellow)
        if not vars2.boxHover and vars2.theme1:
            display.blit(vars.box_Button, (-5, 83)), display.blit(vars.box_Button_Ticked, (-5, 83))
        elif vars2.boxHover and vars2.theme1:
            display.blit(vars.box_Button2, (-5, 83)), display.blit(vars.box_Button_Ticked, (-5, 83))
        elif not vars2.boxHover:
            display.blit(vars.box_Button, (-5, 83))
        else:
            display.blit(vars.box_Button2, (-5, 83))

        # Displaying the check boxes for the second theme (purple and dark blue)
        if not vars2.box2Hover and vars2.theme2:
            display.blit(vars.box2_Button, (-5, 141)), display.blit(vars.box_Button_Ticked, (-5, 141))
        elif vars2.box2Hover and vars2.theme2:
            display.blit(vars.box2_Button2, (-5, 141)), display.blit(vars.box_Button_Ticked, (-5, 141))
        elif not vars2.box2Hover:
            display.blit(vars.box2_Button, (-5, 141))
        else:
            display.blit(vars.box2_Button2, (-5, 141))

    # The main function for displaying the music options
    def music_options():

        # Displaying the music button whilst in the game modes
        if not vars2.gameInProgress2 and not vars2.settingsApplied:
            display.blit(vars.music_Button, (32, 17)), display.blit(vars.on_Label, (42, 85)), display.blit(vars.box_Button, (-5, 83)), display.blit(vars.off_Label, (42, 143)), display.blit(vars.box2_Button, (-5, 141))
        elif vars2.gameInProgress2 or vars2.settingsApplied:
            display.blit(vars.on_Label, (42, 291)), display.blit(vars.off_Label, (42, 345))

        # Displaying the check boxes for music both in and out of main menu, and the game modes
        # For music on display
        if not vars2.gameInProgress2 and not vars2.settingsApplied:
            if not vars2.boxHover and vars2.musicOn:
                display.blit(vars.box_Button, (-5, 83)), display.blit(vars.box_Button_Ticked, (-5, 83))
            elif vars2.boxHover and vars2.musicOn:
                display.blit(vars.box_Button2, (-5, 83)), display.blit(vars.box_Button_Ticked, (-5, 83))
            elif not vars2.boxHover:
                display.blit(vars.box_Button, (-5, 83))
            else:
                display.blit(vars.box_Button2, (-5, 83))
        elif vars2.gameInProgress2 or vars2.settingsApplied:
            if not vars2.boxHover and vars2.musicOn:
                display.blit(vars.box_Button, (-5, 289)), display.blit(vars.box_Button_Ticked, (-5, 289))
            elif vars2.boxHover and vars2.musicOn:
                display.blit(vars.box_Button2, (-5, 289)), display.blit(vars.box_Button_Ticked, (-5, 289))
            elif not vars2.boxHover:
                display.blit(vars.box_Button, (-5, 289))
            else:
                display.blit(vars.box_Button2, (-5, 289))

        # For music off display
        if not vars2.gameInProgress2 and not vars2.settingsApplied:
            if not vars2.box2Hover and vars2.musicOff:
                display.blit(vars.box2_Button, (-5, 141)), display.blit(vars.box_Button_Ticked, (-5, 141))
            elif vars2.box2Hover and vars2.musicOff:
                display.blit(vars.box2_Button2, (-5, 141)), display.blit(vars.box_Button_Ticked, (-5, 141))
            elif not vars2.box2Hover:
                display.blit(vars.box2_Button, (-5, 141))
            else:
                display.blit(vars.box2_Button2, (-5, 141))
        elif vars2.gameInProgress2 or vars2.settingsApplied:
            if not vars2.box2Hover and vars2.musicOff:
                display.blit(vars.box2_Button, (-5, 343)), display.blit(vars.box_Button_Ticked, (-5, 343))
            elif vars2.box2Hover and vars2.musicOff:
                display.blit(vars.box2_Button2, (-5, 343)), display.blit(vars.box_Button_Ticked, (-5, 343))
            elif not vars2.box2Hover:
                display.blit(vars.box2_Button, (-5, 343))
            else:
                display.blit(vars.box2_Button2, (-5, 343))

    # main function for displaying the colour options
    def colour_options():
        display.blit(vars.boards_Button, (32, 17)), display.blit(vars.red_Label, (47, 85)), display.blit(vars.box_Button, (-5, 83)), display.blit(vars.blue_Label, (62, 143)), display.blit(vars.box2_Button, (-5, 141)), display.blit(vars.green_Label, (63, 199)), display.blit(vars.box3_Button, (-5, 198)), display.blit(vars.yellow_Label, (68, 257)), display.blit(vars.box4_Button, (-5, 256))

        # Displaying the check boxes for easy mode board
        if not vars2.boxHover and vars2.colorRedEasy:
            display.blit(vars.box_Button, (-5, 83))
            display.blit(vars.box_Button_Ticked, (-5, 83))
        elif vars2.boxHover and vars2.colorRedEasy:
            display.blit(vars.box_Button2, (-5, 83))
            display.blit(vars.box_Button_Ticked, (-5, 83))
        elif not vars2.boxHover:
            display.blit(vars.box_Button, (-5, 83))
        else:
            display.blit(vars.box_Button2, (-5, 83))

        # Displaying the check boxes for tough mode board
        if not vars2.box2Hover and vars2.colorGreenHard:
            display.blit(vars.box2_Button, (-5, 141))
            display.blit(vars.box_Button_Ticked, (-5, 198))
        elif vars2.box2Hover and vars2.colorGreenHard:
            display.blit(vars.box2_Button2, (-5, 141))
            display.blit(vars.box_Button_Ticked, (-5, 198))
        elif not vars2.box2Hover:
            display.blit(vars.box2_Button, (-5, 141))
        else:
            display.blit(vars.box2_Button2, (-5, 141))

        # Displaying the check boxes for hard mode board
        if not vars2.box3Hover and vars2.colorBlueTough:
            display.blit(vars.box3_Button, (-5, 198))
            display.blit(vars.box_Button_Ticked, (-5, 141))
        elif vars2.box3Hover and vars2.colorBlueTough:
            display.blit(vars.box3_Button2, (-5, 198))
            display.blit(vars.box_Button_Ticked, (-5, 141))
        elif not vars2.box3Hover:
            display.blit(vars.box3_Button, (-5, 198))
        else:
            display.blit(vars.box3_Button2, (-5, 198))

        # Displaying the check boxes for death mode board
        if not vars2.box4Hover and vars2.colorYellowDeath:
            display.blit(vars.box4_Button, (-5, 256))
            display.blit(vars.box_Button_Ticked, (-5, 256))
        elif vars2.box4Hover and vars2.colorYellowDeath:
            display.blit(vars.box4_Button2, (-5, 256))
            display.blit(vars.box_Button_Ticked, (-5, 256))
        elif not vars2.box4Hover:
            display.blit(vars.box4_Button, (-5, 256))
        else:
            display.blit(vars.box4_Button2, (-5, 256))

    # Main function for resetting the main menu buttons
    def menu_button_normalise():
        vars2.mainMenu, vars2.modeSelect, vars2.themeSelect, vars2.colourSelect, vars2.modeHover, vars2.musicHover, vars2.themeHover, vars2.colourHover, vars2.musicSelect = (False,)*9

    # Main function for resetting the values of the in-game buttons
    def game_button_normalise():
        global rankOne, rankTwo, rankThree, rankFour, rank1Pos, rank2Pos, rank3Pos, rank4Pos, rank1Image, rank2Image, rank3Image, rank4Image
        vars2.colorRedEasy, vars2.maleSelect, vars2.maleSelect2, vars2.maleSelect3, vars2.maleSelect4 = (True,)*5
        vars2.gameInProgress, vars2.settingsApplied, vars2.gamePaused, vars2.modeSelected, vars2.multi, vars2.single, vars2.colorBlueTough, vars2.colorGreenHard, vars2.colorYellowDeath, vars2.onePlayerMode, vars2.twoPlayerMode, vars2.threePlayerMode, vars2.fourPlayerMode, vars2.femaleSelect, vars2.femaleSelect2, vars2.femaleSelect3, vars2.femaleSelect4, vars2.redSelect, vars2.redSelect2, vars2.redSelect3, vars2.redSelect4, vars2.greenSelect, vars2.greenSelect2, vars2.greenSelect3, vars2.greenSelect4, vars2.blueSelect, vars2.blueSelect2, vars2.blueSelect3, vars2.blueSelect4, vars2.yellowSelect, vars2.yellowSelect2, vars2.yellowSelect3, vars2.yellowSelect4, vars2.redMale, vars2.blueMale, vars2.greenMale, vars2.yellowMale, vars2.redFemale, vars2.blueFemale, vars2.greenFemale, vars2.yellowFemale, vars2.card1Selected, vars2.card2Selected, vars2.card3Selected, vars2.card4Selected, vars2.card5Selected, vars2.card6Selected, vars2.gameOver = (False,)*48
        vars2.currentRoller, vars2.rollNumber = (0,)*2
        vars2.currentTurn = 1
        rankOne, rankTwo, rankThree, rankFour, rank1Pos, rank2Pos, rank3Pos, rank4Pos = (0,)*8
        rank1Image, rank2Image, rank3Image, rank4Image = ("",)*4

    # Main function for resetting the colour options
    def colour_normalise():
        vars2.colorRedEasy, vars2.colorGreenHard, vars2.colorBlueTough, vars2.colorYellowDeath = (False,)*4

    # Main function for resetting the game mode
    def mode_reset():
        vars2.twoPlayerMode, vars2.threePlayerMode, vars2.fourPlayerMode = (False,)*3

    # Main function for triggering the two player mode
    def two_player():

        # Checking if the game mode is only two player
        if not vars2.threePlayerMode and not vars2.fourPlayerMode:
            player_three_colour_reset(), player_three_gender_reset(), player_four_gender_reset(), player_four_colour_reset()
            vars2.maleSelect4, vars2.maleSelect3 = (True,)*2

        # Displaying grey characters if the player has not chosen their character yet
        if vars2.maleSelect and not vars2.redSelect and not vars2.blueSelect and not vars2.greenSelect and not vars2.yellowSelect:
            display.blit(vars.grey_Male, (76 - 22, 285 - 35))
        elif vars2.femaleSelect and not vars2.redSelect and not vars2.blueSelect and not vars2.greenSelect and not vars2.yellowSelect:
            display.blit(vars.grey_Female, (76 - 22, 285 - 35))

        # Checking for male gender in customisation and displaying effects
        if not vars2.maleSelect:
            if not vars2.maleHover:
                display.blit(vars.male_Gender, (123 - 11, 271 - 17))
            else:
                display.blit(vars.male2_Gender, (123 - 11, 271 - 17))
        else:
            display.blit(vars.male2_Gender, (123 - 11, 271 - 17))

        # Checking for female gender in customisation and displaying effects
        if not vars2.femaleSelect:
            if not vars2.femaleHover:
                display.blit(vars.female_Gender, (123 - 11, 298 - 17))
            else:
                display.blit(vars.female2_Gender, (123 - 11, 298 - 17))
        else:
            display.blit(vars.female2_Gender, (123 - 11, 298 - 17))

        # Checking for red colour in customisation and displaying effects
        if not vars2.redSelect:
            if not vars2.redHover:
                display.blit(vars.red_Colour, (171 - 11, 271 - 17))
            else:
                display.blit(vars.red2_Colour, (171 - 11, 271 - 17))
        else:
            display.blit(vars.red2_Colour, (171 - 11, 271 - 17))
            if vars2.redSelect and vars2.maleSelect:
                display.blit(vars.red_Male, (76 - 22, 285 - 35))
            else:
                display.blit(vars.red_Female, (76 - 22, 285 - 35))

        # Checking for green colour in customisation and displaying effects
        if not vars2.greenSelect:
            if not vars2.greenHover:
                display.blit(vars.green_Colour, (198 - 11, 271 - 17))
            else:
                display.blit(vars.green2_Colour, (198 - 11, 271 - 17))
        else:
            display.blit(vars.green2_Colour, (198 - 11, 271 - 17))
            if vars2.greenSelect and vars2.maleSelect:
                display.blit(vars.green_Male, (76 - 22, 285 - 35))
            else:
                display.blit(vars.green_Female, (76 - 22, 285 - 35))

        # Checking for blue colour in customisation and displaying effects
        if not vars2.blueSelect:
            if not vars2.blueHover:
                display.blit(vars.blue_Colour, (171 - 11, 298 - 17))
            else:
                display.blit(vars.blue2_Colour, (171 - 11, 298 - 17))
        else:
            display.blit(vars.blue2_Colour, (171 - 11, 298 - 17))
            if vars2.blueSelect and vars2.maleSelect:
                display.blit(vars.blue_Male, (76 - 22, 285 - 35))
            else:
                display.blit(vars.blue_Female, (76 - 22, 285 - 35))

        # Checking for yellow colour in customisation and displaying effects
        if not vars2.yellowSelect:
            if not vars2.yellowHover:
                display.blit(vars.yellow_Colour, (198 - 11, 298 - 17))
            else:
                display.blit(vars.yellow2_Colour, (198 - 11, 298 - 17))
        else:
            display.blit(vars.yellow2_Colour, (198 - 11, 298 - 17))
            if vars2.yellowSelect and vars2.maleSelect:
                display.blit(vars.yellow_Male, (76 - 22, 285 - 35))
            else:
                display.blit(vars.yellow_Female, (76 - 22, 285 - 35))

        # Displaying grey characters if the player has not chosen their character yet
        if vars2.maleSelect2 and not vars2.redSelect2 and not vars2.blueSelect2 and not vars2.greenSelect2 and not vars2.yellowSelect2:
            display.blit(vars.grey_Male, (76 - 22, 346 - 35))
        elif vars2.femaleSelect2 and not vars2.redSelect2 and not vars2.blueSelect2 and not vars2.greenSelect2 and not vars2.yellowSelect2:
            display.blit(vars.grey_Female, (76 - 22, 346 - 35))

        # Checking for male gender in customisation and displaying effects
        if not vars2.maleSelect2:
            if not vars2.maleHover2:
                display.blit(vars.male_Gender2, (123 - 11, 333 - 17))
            else:
                display.blit(vars.male2_Gender2, (123 - 11, 333 - 17))
        else:
            display.blit(vars.male2_Gender2, (123 - 11, 333 - 17))

        # Checking for female gender in customisation and displaying effects
        if not vars2.femaleSelect2:
            if not vars2.femaleHover2:
                display.blit(vars.female_Gender2, (123 - 11, 359 - 17))
            else:
                display.blit(vars.female2_Gender2, (123 - 11, 359 - 17))
        else:
            display.blit(vars.female2_Gender2, (123 - 11, 359 - 17))

        # Checking for red colour in customisation and displaying effects
        if not vars2.redSelect2:
            if not vars2.redHover2:
                display.blit(vars.red_Colour2, (171 - 11, 333 - 17))
            else:
                display.blit(vars.red2_Colour2, (171 - 11, 333 - 17))
        else:
            display.blit(vars.red2_Colour2, (171 - 11, 333 - 17))
            if vars2.redSelect2 and vars2.maleSelect2:
                display.blit(vars.red_Male, (76 - 22, 346 - 35))
            else:
                display.blit(vars.red_Female, (76 - 22, 346 - 35))

        # Checking for green colour in customisation and displaying effects
        if not vars2.greenSelect2:
            if not vars2.greenHover2:
                display.blit(vars.green_Colour2, (198 - 11, 333 - 17))
            else:
                display.blit(vars.green2_Colour2, (198 - 11, 333 - 17))
        else:
            display.blit(vars.green2_Colour2, (198 - 11, 333 - 17))
            if vars2.greenSelect2 and vars2.maleSelect2:
                display.blit(vars.green_Male, (76 - 22, 346 - 35))
            else:
                display.blit(vars.green_Female, (76 - 22, 346 - 35))

        # Checking for blue colour in customisation and displaying effects
        if not vars2.blueSelect2:
            if not vars2.blueHover2:
                display.blit(vars.blue_Colour2, (171 - 11, 359 - 17))
            else:
                display.blit(vars.blue2_Colour2, (171 - 11, 359 - 17))
        else:
            display.blit(vars.blue2_Colour2, (171 - 11, 359 - 17))
            if vars2.blueSelect2 and vars2.maleSelect2:
                display.blit(vars.blue_Male, (76 - 22, 346 - 35))
            else:
                display.blit(vars.blue_Female, (76 - 22, 346 - 35))

        # Checking for yellow colour in customisation and displaying effects
        if not vars2.yellowSelect2:
            if not vars2.yellowHover2:
                display.blit(vars.yellow_Colour2, (198 - 11, 359 - 17))
            else:
                display.blit(vars.yellow2_Colour2, (198 - 11, 359 - 17))
        else:
            display.blit(vars.yellow2_Colour2, (198 - 11, 359 - 17))
            if vars2.yellowSelect2 and vars2.maleSelect2:
                display.blit(vars.yellow_Male, (76 - 22, 346 - 35))
            else:
                display.blit(vars.yellow_Female, (76 - 22, 346 - 35))

    # Main function for resetting the one player gender options
    def player_one_gender_reset():
        vars2.maleSelect, vars2.femaleSelect = (False,)*2

    # Main function for resetting the two player gender options
    def player_two_gender_reset():
        vars2.maleSelect2, vars2.femaleSelect2 = (False,)*2

    # Main function for resetting the one player colour options
    def player_one_colour_reset():
        vars2.redSelect, vars2.blueSelect, vars2.greenSelect, vars2.yellowSelect = (False,)*4

    # Main function for resetting the two player colour options
    def player_two_colour_reset():
        vars2.redSelect2, vars2.blueSelect2, vars2. greenSelect2, vars2.yellowSelect2 = (False,)*4

    # Main function for triggering the three player mode
    def three_player():

        # Allowing efficiency for the code by calling the two player function
        two_player()

        # Checking if the game mode is only 3 player
        if not vars2.fourPlayerMode:
            player_four_colour_reset()
            player_four_gender_reset()
            vars2.maleSelect4 = True

        # Displaying grey characters if the player has not chosen their character yet
        if vars2.maleSelect3 and not vars2.redSelect3 and not vars2.blueSelect3 and not vars2.greenSelect3 and not vars2.yellowSelect3:
            display.blit(vars.grey_Male, (76 - 22, 408 - 35))
        elif vars2.femaleSelect3 and not vars2.redSelect3 and not vars2.blueSelect3 and not vars2.greenSelect3 and not vars2.yellowSelect3:
            display.blit(vars.grey_Female, (76 - 22, 408 - 35))

        # Checking for male gender in customisation and displaying effects
        if not vars2.maleSelect3:
            if not vars2.maleHover3:
                display.blit(vars.male_Gender3, (123 - 11, 395 - 17))
            else:
                display.blit(vars.male2_Gender3, (123 - 11, 395 - 17))
        else:
            display.blit(vars.male2_Gender3, (123 - 11, 395 - 17))

        # Checking for female gender in customisation and displaying effects
        if not vars2.femaleSelect3:
            if not vars2.femaleHover3:
                display.blit(vars.female_Gender3, (123 - 11, 421 - 17))
            else:
                display.blit(vars.female2_Gender3, (123 - 11, 421 - 17))
        else:
            display.blit(vars.female2_Gender3, (123 - 11, 421 - 17))

        # Checking for red colour in customisation and displaying effects
        if not vars2.redSelect3:
            if not vars2.redHover3:
                display.blit(vars.red_Colour3, (171 - 11, 395 - 17))
            else:
                display.blit(vars.red2_Colour3, (171 - 11, 395 - 17))
        else:
            display.blit(vars.red2_Colour3, (171 - 11, 395 - 17))
            if vars2.redSelect3 and vars2.maleSelect3:
                display.blit(vars.red_Male, (76 - 22, 408 - 35))
            else:
                display.blit(vars.red_Female, (76 - 22, 408 - 35))

        # Checking for green colour in customisation and displaying effects
        if not vars2.greenSelect3:
            if not vars2.greenHover3:
                display.blit(vars.green_Colour3, (198 - 11, 395 - 17))
            else:
                display.blit(vars.green2_Colour3, (198 - 11, 395 - 17))
        else:
            display.blit(vars.green2_Colour3, (198 - 11, 395 - 17))
            if vars2.greenSelect3 and vars2.maleSelect3:
                display.blit(vars.green_Male, (76 - 22, 408 - 35))
            else:
                display.blit(vars.green_Female, (76 - 22, 408 - 35))

        # Checking for blue colour in customisation and displaying effects
        if not vars2.blueSelect3:
            if not vars2.blueHover3:
                display.blit(vars.blue_Colour3, (171 - 11, 421 - 17))
            else:
                display.blit(vars.blue2_Colour3, (171 - 11, 421 - 17))
        else:
            display.blit(vars.blue2_Colour3, (171 - 11, 421 - 17))
            if vars2.blueSelect3 and vars2.maleSelect3:
                display.blit(vars.blue_Male, (76 - 22, 408 - 35))
            else:
                display.blit(vars.blue_Female, (76 - 22, 408 - 35))

        # Checking for yellow colour in customisation and displaying effects
        if not vars2.yellowSelect3:
            if not vars2.yellowHover3:
                display.blit(vars.yellow_Colour3, (198 - 11, 421 - 17))
            else:
                display.blit(vars.yellow2_Colour3, (198 - 11, 421 - 17))
        else:
            display.blit(vars.yellow2_Colour3, (198 - 11, 421 - 17))
            if vars2.yellowSelect3 and vars2.maleSelect3:
                display.blit(vars.yellow_Male, (76 - 22, 408 - 35))
            else:
                display.blit(vars.yellow_Female, (76 - 22, 408 - 35))

    # Main function for resetting the one player gender options
    def player_three_gender_reset():
        vars2.maleSelect3, vars2.femaleSelect3 = (False,)*2

    # Main function for resetting the one player colour options
    def player_three_colour_reset():
        vars2.redSelect3, vars2.blueSelect3, vars2.greenSelect3, vars2.yellowSelect3 = (False,)*4

    # Main function for triggering the four player mode
    def four_player():

        # Allowing efficiency for the code by calling the three player function
        three_player()

        # Displaying grey characters if the player has not chosen their character yet
        if vars2.maleSelect4 and not vars2.redSelect4 and not vars2.blueSelect4 and not vars2.greenSelect4 and not vars2.yellowSelect4:
            display.blit(vars.grey_Male, (76 - 22, 469 - 35))
        elif vars2.femaleSelect4 and not vars2.redSelect4 and not vars2.blueSelect4 and not vars2.greenSelect4 and not vars2.yellowSelect4:
            display.blit(vars.grey_Female, (76 - 22, 469 - 35))

        # Checking for male gender in customisation and displaying effects
        if not vars2.maleSelect4:
            if not vars2.maleHover4:
                display.blit(vars.male_Gender4, (123 - 11, 456 - 17))
            else:
                display.blit(vars.male2_Gender4, (123 - 11, 456 - 17))
        else:
            display.blit(vars.male2_Gender4, (123 - 11, 456 - 17))

        # Checking for female gender in customisation and displaying effects
        if not vars2.femaleSelect4:
            if not vars2.femaleHover4:
                display.blit(vars.female_Gender4, (123 - 11, 482 - 17))
            else:
                display.blit(vars.female2_Gender4, (123 - 11, 482 - 17))
        else:
            display.blit(vars.female2_Gender4, (123 - 11, 482 - 17))

        # Checking for red colour in customisation and displaying effects
        if not vars2.redSelect4:
            if not vars2.redHover4:
                display.blit(vars.red_Colour4, (171 - 11, 456 - 17))
            else:
                display.blit(vars.red2_Colour4, (171 - 11, 456 - 17))
        else:
            display.blit(vars.red2_Colour4, (171 - 11, 456 - 17))
            if vars2.redSelect4 and vars2.maleSelect4:
                display.blit(vars.red_Male, (76 - 22, 469 - 35))
            else:
                display.blit(vars.red_Female, (76 - 22, 469 - 35))

        # Checking for green colour in customisation and displaying effects
        if not vars2.greenSelect4:
            if not vars2.greenHover4:
                display.blit(vars.green_Colour4, (198 - 11, 456 - 17))
            else:
                display.blit(vars.green2_Colour4, (198 - 11, 456 - 17))
        else:
            display.blit(vars.green2_Colour4, (198 - 11, 456 - 17))
            if vars2.greenSelect4 and vars2.maleSelect4:
                display.blit(vars.green_Male, (76 - 22, 469 - 35))
            else:
                display.blit(vars.green_Female, (76 - 22, 469 - 35))

        # Checking for blue colour in customisation and displaying effects
        if not vars2.blueSelect4:
            if not vars2.blueHover4:
                display.blit(vars.blue_Colour4, (171 - 11, 482 - 17))
            else:
                display.blit(vars.blue2_Colour4, (171 - 11, 482 - 17))
        else:
            display.blit(vars.blue2_Colour4, (171 - 11, 482 - 17))
            if vars2.blueSelect4 and vars2.maleSelect4:
                display.blit(vars.blue_Male, (76 - 22, 469 - 35))
            else:
                display.blit(vars.blue_Female, (76 - 22, 469 - 35))

        # Checking for yellow colour in customisation and displaying effects
        if not vars2.yellowSelect4:
            if not vars2.yellowHover4:
                display.blit(vars.yellow_Colour4, (198 - 11, 482 - 17))
            else:
                display.blit(vars.yellow2_Colour4, (198 - 11, 482 - 17))
        else:
            display.blit(vars.yellow2_Colour4, (198 - 11, 482 - 17))
            if vars2.yellowSelect4 and vars2.maleSelect4:
                display.blit(vars.yellow_Male, (76 - 22, 469 - 35))
            else:
                display.blit(vars.yellow_Female, (76 - 22, 469 - 35))

    # Main function for resetting the one player gender options
    def player_four_gender_reset():
        vars2.maleSelect4, vars2.femaleSelect4 = (False,)*2

    # Main function for resetting the one player colour options
    def player_four_colour_reset():
        vars2.redSelect4, vars2.blueSelect4, vars2.greenSelect4, vars2.yellowSelect4 = (False,)*4

    # Main function for selecting a random number for when player picks a card
    def random_card_selector():
        random.seed()
        if vars2.rollNumber == 0:
            for i in range(10):
                vars2.rollNumber = random.randint(1, 6)

    # The main function that is used for multi threading
    def sleeper(n, name, turnone, turntwo, turnthree, turnfour, pausing, moving, singlepause, computerturnpause, musicfadeout):

        # Global declaration of player character stats
        global rank1Pos, rank2Pos, rank3Pos, rank4Pos, posList

        # Checks if player character is moving
        if moving:
            vars2.movement = True

            # Checks if nobody had won the game yet
            if turntwo and (rank2Pos + vars2.rollNumber <= 99) and vars2.gameInProgress2:
                pygame.time.wait(2000)
            for i in range(vars2.rollNumber):

                #Moves the player character the number of steps shown on the cards every 0.2 seconds 
                if turnone and (rank1Pos + vars2.rollNumber <= 99):
                    rank1Pos += 1
                    time.sleep(n)
                elif turntwo and (rank2Pos + vars2.rollNumber <= 99):
                    rank2Pos += 1
                    time.sleep(n)
                elif turnthree and (rank3Pos + vars2.rollNumber <= 99):
                    rank3Pos += 1
                    time.sleep(n)
                elif turnfour and (rank4Pos + vars2.rollNumber <= 99):
                    rank4Pos += 1
                    time.sleep(n)

            # Checks to see if the game mode is easy
            # It checks the board first, and then loops the adhering ladder and snake positions
            if vars2.colorRedEasy:
                for p in easyBoardLadders:
                    for j in range(1, 5):
                        if eval("rank" + str(j) + "Pos") == (p[0]-1):
                            globals()["rank" + str(j) + "Pos"] += abs((p[0])-(p[1]))
                for p in easyBoardSnakes:
                    for j in range(1, 5):
                        if eval("rank" + str(j) + "Pos") == (p[0]-1):
                            globals()["rank" + str(j) + "Pos"] -= abs((p[0])-(p[1]))

            # Checks to see if the game mode is tough
            elif vars2.colorBlueTough:
                for p in toughBoardLadders:
                    for j in range(1, 5):
                        if eval("rank" + str(j) + "Pos") == (p[0]-1):
                            globals()["rank" + str(j) + "Pos"] += abs((p[0])-(p[1]))
                for p in toughBoardSnakes:
                    for j in range(1, 5):
                        if eval("rank" + str(j) + "Pos") == (p[0]-1):
                            globals()["rank" + str(j) + "Pos"] -= abs((p[0])-(p[1]))

            # Checks to see if the game mode is hard
            elif vars2.colorGreenHard:
                for p in hardBoardLadders:
                    for j in range(1, 5):
                        if eval("rank" + str(j) + "Pos") == (p[0]-1):
                            globals()["rank" + str(j) + "Pos"] += abs((p[0])-(p[1]))
                for p in hardBoardSnakes:
                    for j in range(1, 5):
                        if eval("rank" + str(j) + "Pos") == (p[0]-1):
                            globals()["rank" + str(j) + "Pos"] -= abs((p[0])-(p[1]))

            # Checks to see if the game mode is death
            elif vars2.colorYellowDeath:
                for p in deathBoardLadders:
                    for j in range(1, 5):
                        if eval("rank" + str(j) + "Pos") == (p[0]-1):
                            globals()["rank" + str(j) + "Pos"] += abs((p[0])-(p[1]))
                for p in deathBoardSnakes:
                    for j in range(1, 5):
                        if eval("rank" + str(j) + "Pos") == (p[0]-1):
                            globals()["rank" + str(j) + "Pos"] -= abs((p[0])-(p[1]))

            # Appending player stats into a list to use later in the code
            posList = [rank1Pos, rank2Pos]

            # Appending 3 players' stats if game mode is three player
            if vars2.threePlayerMode:
                posList = [rank1Pos, rank2Pos, rank3Pos]

            # Appending 4 players' stats if game mode is four player
            elif vars2.fourPlayerMode:
                posList = [rank1Pos, rank2Pos, rank3Pos, rank4Pos]
            vars2.movement = False

            # Appending 2 players' stats if game mode is two player
            if vars2.onePlayerMode and turntwo:
                vars2.card1Selected, vars2.card2Selected, vars2.card3Selected, vars2.card4Selected, vars2. card5Selected, vars2.card6Selected = (False,)*6
                vars2.rollNumber = 0
                if vars2.currentTurn != 2 and vars2.onePlayerMode:
                    vars2.currentTurn += 1
                elif vars2.currentTurn == 2 and vars2.onePlayerMode:
                    vars2.currentTurn = 1

        # The multi thread for pausing the game in multiplayer
        elif pausing:
            vars2.pauseDebounce = True
            time.sleep(n)
            vars2.pauseDebounce = False

        # The multi thread for pausing in singleplayer mode
        elif singlepause:
            vars2.singlePlayerWait = True
            time.sleep(n)
            vars2.singlePlayerWait = False

        # The multi thread for pausing the computer before allowing it to move its player character
        elif computerturnpause:
            vars2.computerPause = True
            time.sleep(n)
            vars2.computerPause = False

        # The multi thread for fading out the music
        elif musicfadeout:
            pygame.mixer.music.fadeout(n)

    # Main function for handling the effects and functionality of the game options
    def game_options():

        # Displaying the roll button effects
        if not vars2.rollHover:
            display.blit(vars.roll_Button, (858, 510))
        else:
            display.blit(vars.roll_Button_Expanded, (847, 506))

        # Displaying the pause button effects
        if not vars2.gamePaused:
            if not vars2.pauseHover:
                display.blit(vars.pause_Button, (32, 17))
            else:
                display.blit(vars.pause_Button_Expanded, (21, 13))

        # Displaying the resume button effects
        else:
            if not vars2.resumeHover:
                display.blit(vars.resume_Button, (32, 17))
            else:
                display.blit(vars.resume_Button_Expanded, (21, 13))

        # Displaying the effects for the first card in the card box
        if not vars2.cardOneHover and not vars2.card1Selected:
            display.blit(vars.card_One, (870, 27))
        else:
            display.blit(vars.card_One_Expanded, (870 - 3, 27 - 5))

        # Displaying the effects for the second card in the card box
        if not vars2.cardTwoHover and not vars2.card2Selected:
            display.blit(vars.card_Two, (935, 27))
        else:
            display.blit(vars.card_Two_Expanded, (935 - 3, 27 - 5))

        # Displaying the effects for the third card in the card box
        if not vars2.cardThreeHover and not vars2.card3Selected:
            display.blit(vars.card_Three, (1000, 27))
        else:
            display.blit(vars.card_Three_Expanded, (1000 - 3, 27 - 5))

        # Displaying the effects for the fourth card in the card box
        if not vars2.cardFourHover and not vars2.card4Selected:
            display.blit(vars.card_Four, (870, 135))
        else:
            display.blit(vars.card_Four_Expanded, (870 - 3, 135 - 5))

        # Displaying the effects for the fifth card in the card box
        if not vars2.cardFiveHover and not vars2.card5Selected:
            display.blit(vars.card_Five, (935, 135))
        else:
            display.blit(vars.card_Five_Expanded, (935 - 3, 135 - 5))

        # Displaying the effects for the sixth card in the card box
        if not vars2.cardSixHover and not vars2.card6Selected:
            display.blit(vars.card_Six, (1000, 135))
        else:
            display.blit(vars.card_Six_Expanded, (1000 - 3, 135 - 5))

        # Looping through to see which card is selected and then blitting the image corresponding to that card number
        diceImg = ["dice_One", "dice_Two", "dice_Three", "dice_Four", "dice_Five", "dice_Six"]
        for i in range(1, 7):
            if vars2.__dict__[("card" + str(i) + "Selected")]:
                random_card_selector()
                for j in range(1, 7):
                    if vars2.rollNumber == j and (i == 1 or i == 2 or i == 3):
                        display.blit(vars.__dict__[diceImg[j - 1]], (867 + (65*(i - 1)), 22))
                    elif vars2.rollNumber == j and (i == 4 or i == 5 or i == 6):
                        display.blit(vars.__dict__[diceImg[j - 1]], (867 + (65*(i - 4)), 130))

        # Displaying info to act as a mini user-guide
        if vars2.settingsApplied and (vars2.gameInProgress or vars2.gameInProgress2):
            display.blit(vars.card_Select_Error, (-17, 520)), display.blit(vars.roll_Error, (-17, 450))

    # Main function for allowing the computer to play its move in singleplayer mode
    def computer_move():

        # randomises according to the time of the monitor (very generalised answer)
        random.seed()

        # Looping through to pick a random number for the computer to move
        if vars2.rollNumber == 0:
            for i in range(10):
                vars2.rollNumber = random.randint(1, 6)
            for i in range(20):
                vars2.computerCardSelect = random.randint(1, 6)
            for i in range(1, 7):
                if vars2.computerCardSelect == i:
                    vars2.__dict__[("card" + str(i) + "Selected")] = True

    # Once the game finishes, this function displays the winner
    def winner(rank1win, rank2win, rank3win, rank4win):
        if not vars2.gameOver:
            vars2.gameOver, vars2.musicSelect = True, False

        # Depending on the selected theme, the main menu icon is displayed
        if vars2.theme1:
            display.blit(vars.board_Image, (264, 17)), display.blit(vars.winner_Label, (600, 380))
        elif vars2.theme2:
            display.blit(vars.board_Image2, (264, 17)), display.blit(vars.winner_Label2, (600, 380))

        #Checks which player won and displays that specific player's image
        count = 0
        for i in range(1, 5):
            if eval("rank" + str(i) + "win"):
                    for color in clr2:
                        count += 1
                        if eval("rank" + str(i) + "Image") == color:
                            display.blit(vars.__dict__[winImages[count-1]], (618, 400))

    def easybutton():
        # Easy Button function which is placed in the Selection Screen
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 400 <= mouse_x <= 700 and 100 <= mouse_y <= 200:
            display.blit(EASY_button2, (xe - 5, ye))
            if click[0] == 1:  # Checks if the left button of the mouse is clicked.
                easy_mode()  # Runs the Easy Mode function
        else:
            display.blit(EASY_button, (xe - 5, ye))

    def MediumButton():
        # Medium Button function which is placed in the Selection Screen
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 400 <= mouse_x <= 700 and 250 <= mouse_y <= 400:
            display.blit(medium_button, (xe - 5, 250))
            if click[0] == 1:  # Checks if the left button of the mouse is clicked.
                medium_mode()  # Runs the Medium Mode function
        else:
            display.blit(medium_button2, (xe - 5, 250))

    def HardButton():
        # Hard Button function which is placed in the Selection Screen
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 400 <= mouse_x <= 700 and 400 <= mouse_y <= 500:
            display.blit(hard_button2, (xe - 5, 400))
            if click[0] == 1:  # Checks if the left button of the mouse is clicked.
                Hard_mode()  # Runs the Medium Mode function
        else:
            display.blit(hard_button, (xe - 5, 400))

    def selection_screen():
        global intro
        intro = True
        display = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Mind Shaper')
        display.blit(sunset, (xs, ys))
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Closes the window when the "X" button is clicked.
                    pygame.quit()
                    quit()
            bridgebutton()  # Bridge Gate
            easybutton()  # Places Easy Button Function
            MediumButton()  # Places Medium Button Function
            HardButton()  # Places Hard Button Function
            pygame.display.update()
            clock.tick(15)

    def easy_mode():
        global pos, highLight, initiate, angel_1, angel_2, whatever_1, whatever_2, worried_1, worried_2, cool_1, cool_2, angel_match, whatever_match, worried_match, cool_match
        run = True
        random.shuffle(pos)
        while run and intro:
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
            if (pos[0][0]) - 10 <= mouse_x <= (pos[0][0]) + 115 and (pos[0][1]) - 5 <= mouse_y <= int(
                    pos[0][1]) + 129 and canClick:
                if mouse_click[0] == 1 and not angel_1:
                    angel_1 = True
                    initiate += 1
            elif (pos[1][0]) - 10 <= mouse_x <= (pos[1][0]) + 115 and (pos[1][1]) - 5 <= mouse_y <= (
            pos[1][1]) + 129 and canClick:
                if mouse_click[0] == 1 and not angel_2:
                    angel_2 = True
                    initiate += 1
            elif (pos[2][0]) - 10 <= mouse_x <= (pos[2][0]) + 115 and (pos[2][1]) - 5 <= mouse_y <= (
            pos[2][1]) + 129 and canClick:
                if mouse_click[0] == 1 and not whatever_1:
                    whatever_1 = True
                    initiate += 1
            elif (pos[3][0]) - 10 <= mouse_x <= (pos[3][0]) + 115 and (pos[3][1]) - 5 <= mouse_y <= (
            pos[3][1]) + 129 and canClick:
                if mouse_click[0] == 1 and not whatever_2:
                    whatever_2 = True
                    initiate += 1
            elif (pos[4][0]) - 10 <= mouse_x <= (pos[4][0]) + 115 and (pos[4][1]) - 5 <= mouse_y <= (
            pos[4][1]) + 129 and canClick:
                if mouse_click[0] == 1 and not worried_1:
                    worried_1 = True
                    initiate += 1
            elif (pos[5][0]) - 10 <= mouse_x <= (pos[5][0]) + 115 and (pos[5][1]) - 5 <= mouse_y <= (
            pos[5][1]) + 129 and canClick:
                if mouse_click[0] == 1 and not worried_2:
                    worried_2 = True
                    initiate += 1
            elif (pos[6][0]) - 10 <= mouse_x <= (pos[6][0]) + 115 and (pos[6][1]) - 5 <= mouse_y <= (
            pos[6][1]) + 129 and canClick:
                if mouse_click[0] == 1 and not cool_1:
                    cool_1 = True
                    initiate += 1
            elif (pos[7][0]) - 10 <= mouse_x <= (pos[7][0]) + 115 and (pos[7][1]) - 5 <= mouse_y <= int(
                    pos[7][1]) + 129 and canClick:
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
            menubutton()  # Home Button
            congratulation_easy()  # Well Done Popup
            pygame.display.update()
            clock.tick(15)

    def bridgebutton():
        global leaveBridge, chosenGame, intro, memory, transition
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 19.2 <= mouse_x <= 100.9 and 19.2 <= mouse_y <= 100.9:
            display.blit(bridgegate2, (19.2, 20))
            if click[0] == 1:
                pygame.time.wait(400)
                transition = False
                leaveBridge = False
                memory = False
                intro = False
                chosenGame = ""
                main_screen()
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
        # This function will highligth the box if the mouse pointer is above it
        # Works for Easy mode only.
        for i in range(8):
            if (pos[i][0]) - 8 <= mouse_x <= (pos[i][0]) + 108 and (pos[i][1]) - 5 <= mouse_y <= (pos[i][1]) + 115:
                display.blit(highlight, (int(pos[i][0]) - int(30), int(pos[i][1]) - int(20)))

    def display_pause(time, name):
        # This function is used for threading in the Easy mode function
        global canClick, angel_1, angel_2, whatever_1, whatever_2, worried_1, worried_2, cool_1, cool_2
        canClick = False  # Stops the user from clicking any other boxes/tiles.
        pygame.time.wait(time)
        # Converts the emoji back to False if the are not matched.
        if not angel_match:
            angel_1, angel_2 = (False,) * 2
        if not whatever_match:
            whatever_1, whatever_2 = (False,) * 2
        if not worried_match:
            worried_1, worried_2 = (False,) * 2
        if not cool_match:
            cool_1, cool_2 = (False,) * 2
        canClick = True  # Allows the user to click the boxes/tiles after 1 sec.

    def Hard_mode():
        global pos2, initiate_2, hard_box, rect_1, rect_2, rect_1A, rect_2A, hex_1, hex_2, hex_1A, hex_2A, star_1, star_2, star_1A, star_2A, circle_1, circle_2, circle_1A, circle_2A, triangle_1, triangle_2, triangle_1A, triangle_2A, opphex_1, opphex_2, opphex_1A, opphex_2A, oval_1, oval_2, oval_1A, oval_2A, heart_1, heart_2, heart_1A, heart_2A, commstar_1, commstar_2, commstar_1A, commstar_2A, splatpaint_1, splatpaint_2, splatpaint_1A, splatpaint_2A, square_1, square_2, rect_match, hex_match, star_match, circle_match, triangle_match, opphex_match, rect_Amatch, hex_Amatch, star_Amatch, circle_Amatch, triangle_Amatch, opphex_Amatch, oval_match, oval_Amatch, heart_match, heart_Amatch, commstar_match, commstar_Amatch, splatpaint_match, splatpaint_Amatch, square_match
        run2 = True
        random.shuffle(pos2)
        while run2 and intro:
            display = pygame.display.set_mode((width, height))
            pygame.display.set_caption('Mind Shaper')
            display.blit(maths_background, (xs, ys))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            for i in range(42):  # Gets the Shape's position from the "pos2" list and places it into the Screen.
                display.blit(multi_shapes_L2[i], (pos2[i]))

            # These "if" statements follows the same concept as described in Easy mode function, however, the emoji is replaced with shapes.
            if (pos2[0][0]) <= mouse_x <= (pos2[0][0]) + 75 and (pos2[0][1]) <= mouse_y <= int(
                    pos2[0][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not rect_1:
                    rect_1 = True
                    initiate_2 += 1
            elif (pos2[1][0]) <= mouse_x <= (pos2[1][0]) + 75 and (pos2[1][1]) <= mouse_y <= (
            pos2[1][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not rect_2:
                    rect_2 = True
                    initiate_2 += 1
            elif (pos2[2][0]) <= mouse_x <= (pos2[2][0]) + 75 and (pos2[2][1]) <= mouse_y <= (
            pos2[2][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not rect_1A:
                    rect_1A = True
                    initiate_2 += 1
            elif (pos2[3][0]) <= mouse_x <= (pos2[3][0]) + 75 and (pos2[3][1]) <= mouse_y <= (
            pos2[3][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not rect_2A:
                    rect_2A = True
                    initiate_2 += 1
            elif (pos2[4][0]) <= mouse_x <= (pos2[4][0]) + 75 and (pos2[4][1]) <= mouse_y <= (
            pos2[4][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not hex_1:
                    hex_1 = True
                    initiate_2 += 1
            elif (pos2[5][0]) <= mouse_x <= (pos2[5][0]) + 75 and (pos2[5][1]) <= mouse_y <= (
            pos2[5][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not hex_2:
                    hex_2 = True
                    initiate_2 += 1
            elif (pos2[6][0]) <= mouse_x <= (pos2[6][0]) + 75 and (pos2[6][1]) <= mouse_y <= (
            pos2[6][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not hex_1A:
                    hex_1A = True
                    initiate_2 += 1
            elif (pos2[7][0]) <= mouse_x <= (pos2[7][0]) + 75 and (pos2[7][1]) <= mouse_y <= int(
                    pos2[7][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not hex_2A:
                    hex_2A = True
                    initiate_2 += 1
            if (pos2[8][0]) <= mouse_x <= (pos2[8][0]) + 75 and (pos2[8][1]) <= mouse_y <= int(
                    pos2[8][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not star_1:
                    star_1 = True
                    initiate_2 += 1
            elif (pos2[9][0]) <= mouse_x <= (pos2[9][0]) + 75 and (pos2[9][1]) <= mouse_y <= (
            pos2[9][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not star_2:
                    star_2 = True
                    initiate_2 += 1
            elif (pos2[10][0]) <= mouse_x <= (pos2[10][0]) + 75 and (pos2[10][1]) <= mouse_y <= (
            pos2[10][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not star_1A:
                    star_1A = True
                    initiate_2 += 1
            elif (pos2[11][0]) <= mouse_x <= (pos2[11][0]) + 75 and (pos2[11][1]) <= mouse_y <= (
            pos2[11][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not star_2A:
                    star_2A = True
                    initiate_2 += 1
            elif (pos2[12][0]) <= mouse_x <= (pos2[12][0]) + 75 and (pos2[12][1]) <= mouse_y <= (
            pos2[12][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not circle_1:
                    circle_1 = True
                    initiate_2 += 1
            elif (pos2[13][0]) <= mouse_x <= (pos2[13][0]) + 75 and (pos2[13][1]) <= mouse_y <= (
            pos2[13][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not circle_2:
                    circle_2 = True
                    initiate_2 += 1
            elif (pos2[14][0]) <= mouse_x <= (pos2[14][0]) + 75 and (pos2[14][1]) <= mouse_y <= (
            pos2[14][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not circle_1A:
                    circle_1A = True
                    initiate_2 += 1
            elif (pos2[15][0]) <= mouse_x <= (pos2[15][0]) + 75 and (pos2[15][1]) <= mouse_y <= int(
                    pos2[15][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not circle_2A:
                    circle_2A = True
                    initiate_2 += 1
            elif (pos2[16][0]) <= mouse_x <= (pos2[16][0]) + 75 and (pos2[16][1]) <= mouse_y <= int(
                    pos2[16][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not triangle_1:
                    triangle_1 = True
                    initiate_2 += 1
            elif (pos2[17][0]) <= mouse_x <= (pos2[17][0]) + 75 and (pos2[17][1]) <= mouse_y <= (
            pos2[17][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not triangle_2:
                    triangle_2 = True
                    initiate_2 += 1
            elif (pos2[18][0]) <= mouse_x <= (pos2[18][0]) + 75 and (pos2[18][1]) <= mouse_y <= (
            pos2[18][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not triangle_1A:
                    triangle_1A = True
                    initiate_2 += 1
            elif (pos2[19][0]) <= mouse_x <= (pos2[19][0]) + 75 and (pos2[19][1]) <= mouse_y <= (
            pos2[19][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not triangle_2A:
                    triangle_2A = True
                    initiate_2 += 1
            elif (pos2[20][0]) <= mouse_x <= (pos2[20][0]) + 75 and (pos2[20][1]) <= mouse_y <= (
            pos2[20][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not opphex_1:
                    opphex_1 = True
                    initiate_2 += 1
            elif (pos2[21][0]) <= mouse_x <= (pos2[21][0]) + 75 and (pos2[21][1]) <= mouse_y <= (
            pos2[21][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not opphex_2:
                    opphex_2 = True
                    initiate_2 += 1
            elif (pos2[22][0]) <= mouse_x <= (pos2[22][0]) + 75 and (pos2[22][1]) <= mouse_y <= (
            pos2[22][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not opphex_1A:
                    opphex_1A = True
                    initiate_2 += 1
            elif (pos2[23][0]) <= mouse_x <= (pos2[23][0]) + 75 and (pos2[23][1]) <= mouse_y <= int(
                    pos2[23][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not opphex_2A:
                    opphex_2A = True
                    initiate_2 += 1
            elif (pos2[24][0]) <= mouse_x <= (pos2[24][0]) + 75 and (pos2[24][1]) <= mouse_y <= int(
                    pos2[24][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not oval_1:
                    oval_1 = True
                    initiate_2 += 1
            elif (pos2[25][0]) <= mouse_x <= (pos2[25][0]) + 75 and (pos2[25][1]) <= mouse_y <= (
            pos2[25][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not oval_2:
                    oval_2 = True
                    initiate_2 += 1
            elif (pos2[26][0]) <= mouse_x <= (pos2[26][0]) + 75 and (pos2[26][1]) <= mouse_y <= (
            pos2[26][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not oval_1A:
                    oval_1A = True
                    initiate_2 += 1
            elif (pos2[27][0]) <= mouse_x <= (pos2[27][0]) + 75 and (pos2[27][1]) <= mouse_y <= (
            pos2[27][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not oval_2A:
                    oval_2A = True
                    initiate_2 += 1
            elif (pos2[28][0]) <= mouse_x <= (pos2[28][0]) + 75 and (pos2[28][1]) <= mouse_y <= (
            pos2[28][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not heart_1:
                    heart_1 = True
                    initiate_2 += 1
            elif (pos2[29][0]) <= mouse_x <= (pos2[29][0]) + 75 and (pos2[29][1]) <= mouse_y <= (
            pos2[29][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not heart_2:
                    heart_2 = True
                    initiate_2 += 1
            elif (pos2[30][0]) <= mouse_x <= (pos2[30][0]) + 75 and (pos2[30][1]) <= mouse_y <= (
            pos2[30][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not heart_1A:
                    heart_1A = True
                    initiate_2 += 1
            elif (pos2[31][0]) <= mouse_x <= (pos2[31][0]) + 75 and (pos2[31][1]) <= mouse_y <= int(
                    pos2[31][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not heart_2A:
                    heart_2A = True
                    initiate_2 += 1
            elif (pos2[32][0]) <= mouse_x <= (pos2[32][0]) + 75 and (pos2[32][1]) <= mouse_y <= (
            pos2[32][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not commstar_1:
                    commstar_1 = True
                    initiate_2 += 1
            elif (pos2[33][0]) <= mouse_x <= (pos2[33][0]) + 75 and (pos2[33][1]) <= mouse_y <= (
            pos2[33][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not commstar_2:
                    commstar_2 = True
                    initiate_2 += 1
            elif (pos2[34][0]) <= mouse_x <= (pos2[34][0]) + 75 and (pos2[34][1]) <= mouse_y <= (
            pos2[34][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not commstar_1A:
                    commstar_1A = True
                    initiate_2 += 1
            elif (pos2[35][0]) <= mouse_x <= (pos2[35][0]) + 75 and (pos2[35][1]) <= mouse_y <= int(
                    pos2[35][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not commstar_2A:
                    commstar_2A = True
                    initiate_2 += 1
            elif (pos2[36][0]) <= mouse_x <= (pos2[36][0]) + 75 and (pos2[36][1]) <= mouse_y <= int(
                    pos2[36][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not splatpaint_1:
                    splatpaint_1 = True
                    initiate_2 += 1
            elif (pos2[37][0]) <= mouse_x <= (pos2[37][0]) + 75 and (pos2[37][1]) <= mouse_y <= (
            pos2[37][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not splatpaint_2:
                    splatpaint_2 = True
                    initiate_2 += 1
            elif (pos2[38][0]) <= mouse_x <= (pos2[38][0]) + 75 and (pos2[38][1]) <= mouse_y <= (
            pos2[38][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not splatpaint_1A:
                    splatpaint_1A = True
                    initiate_2 += 1
            elif (pos2[39][0]) <= mouse_x <= (pos2[39][0]) + 75 and (pos2[39][1]) <= mouse_y <= (
            pos2[39][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not splatpaint_2A:
                    splatpaint_2A = True
                    initiate_2 += 1
            elif (pos2[40][0]) <= mouse_x <= (pos2[40][0]) + 75 and (pos2[40][1]) <= mouse_y <= (
            pos2[40][1]) + 80 and canClick2:
                if mouse_click[0] == 1 and not square_1:
                    square_1 = True
                    initiate_2 += 1
            elif (pos2[41][0]) <= mouse_x <= (pos2[41][0]) + 75 and (pos2[41][1]) <= mouse_y <= (
            pos2[41][1]) + 80 and canClick2:
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
                elif circle_1A == True and circle_2A == True and not circle_Amatch:
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
        global canClick2, rect_1, rect_2, rect_1A, rect_2A, hex_1, hex_2, hex_1A, hex_2A, star_1, star_2, star_1A, star_2A, circle_1, circle_2, circle_1A, circle_2A, triangle_1, triangle_2, triangle_1A, triangle_2A, opphex_1, opphex_2, opphex_1A, opphex_2A, oval_1, oval_2, oval_1A, oval_2A, heart_1, heart_2, heart_1A, heart_2A, commstar_1, commstar_2, commstar_1A, commstar_2A, splatpaint_1, splatpaint_2, splatpaint_1A, splatpaint_2A, square_1, square_2
        canClick2 = False  # Stops the user from clicking any other boxes/tiles.
        pygame.time.wait(time)
        # Converts the emojis back to False if the are not matched.
        if not rect_match:
            rect_1, rect_2 = (False,) * 2
        if not rect_Amatch:
            rect_1A, rect_2A = (False,) * 2
        if not hex_match:
            hex_1, hex_2 = (False,) * 2
        if not hex_Amatch:
            hex_1A, hex_2A = (False,) * 2
        if not star_match:
            star_1, star_2 = (False,) * 2
        if not star_Amatch:
            star_1A, star_2A = (False,) * 2
        if not circle_match:
            circle_1, circle_2 = (False,) * 2
        if not circle_Amatch:
            circle_1A, circle_2A = (False,) * 2
        if not triangle_match:
            triangle_1, triangle_2 = (False,) * 2
        if not triangle_Amatch:
            triangle_1A, triangle_2A = (False,) * 2
        if not opphex_match:
            opphex_1, opphex_2 = (False,) * 2
        if not opphex_Amatch:
            opphex_1A, opphex_2A = (False,) * 2
        if not oval_match:
            oval_1, oval_2 = (False,) * 2
        if not oval_Amatch:
            oval_1A, oval_2A = (False,) * 2
        if not heart_match:
            heart_1, heart_2 = (False,) * 2
        if not heart_Amatch:
            heart_1A, heart_2A = (False,) * 2
        if not commstar_match:
            commstar_1, commstar_2 = (False,) * 2
        if not commstar_Amatch:
            commstar_1A, commstar_2A = (False,) * 2
        if not splatpaint_match:
            splatpaint_1, splatpaint_2 = (False,) * 2
        if not splatpaint_Amatch:
            splatpaint_1A, splatpaint_2A = (False,) * 2
        if not square_match:
            square_1, square_2 = (False,) * 2
        canClick2 = True  # Allows the user to click the boxes/tiles after 1 sec.

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
                display.blit(highlight_hard, (pos2[i][0] - 2, pos2[i][1] - 2))

    def congratulation_easy3():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # Checks whether all the images are matched or not. If they are matched Display the "dull screen" and the "Popup"
        if (rect_match and rect_Amatch and hex_match and hex_Amatch and star_match and star_Amatch and circle_match and circle_Amatch and triangle_match and triangle_Amatch and opphex_match and opphex_Amatch and oval_match and oval_Amatch and heart_match and heart_Amatch and commstar_match and commstar_Amatch and splatpaint_match and splatpaint_Amatch and square_match) == True:
            display.blit(table2, (0, 0))
            display.blit(congratsEasy, (255, 100))
            if 405 <= mouse_x <= 545 and 300 <= mouse_y <= 367:
                display.blit(congratsEasyretry, (405, 300))
                # If retry is clicked it loops back and starts the game again.
                if click[0] == 1:
                    normalise_3()
                    Hard_mode()
            # If Home is clicked it goes back to the Selection screen as well as resets the Hard mode.
            elif 575 <= mouse_x <= 715 and 300 <= mouse_y <= 367:
                display.blit(congratsEasyhome, (575, 300))
                if click[0] == 1:
                    normalise_3()
                    selection_screen()
                    exit(Hard_mode())

    def medium_mode():
        global pos3, initiate_3, tacos_1, tacos_2, tacos_match, pizza_1, pizza_2, pizza_match, popcorn_1, popcorn_2, popcorn_match, burger_1, burger_2, burger_match, sandwich_1, sandwich_2, sandwich_match, cookies_1, cookies_2, cookies_match, icecream_1, icecream_2, icecream_match, whitechoc_1, whitechoc_2, whitechoc_match, pancakecream_1, pancakecream_2, pancakecream_match, chips_1, chips_2, chips_match, fries_1, fries_2, fries_match, donut_1, donut_2, donut_match, drink_1, drink_2, drink_match, cupcake_1, cupcake_2, cupcake_match, hotdog_1, hotdog_2, hotdog_match
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

            for i in range(
                    30):  # Gets the Fast Food images position from the "pos3" list and places it into the Screen.
                display.blit(multi_junks_L2[i], (pos3[i]))
            # These "if" statements follows the same concept as described in Easy mode function, however, the emoji is replaced with Fast Food Images.
            if (pos3[0][0]) <= mouse_x <= (pos3[0][0]) + 80 and (pos3[0][1]) <= mouse_y <= int(
                    pos3[0][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not tacos_1:
                    tacos_1 = True
                    initiate_3 += 1
            elif (pos3[1][0]) <= mouse_x <= (pos3[1][0]) + 80 and (pos3[1][1]) <= mouse_y <= (
            pos3[1][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not tacos_2:
                    tacos_2 = True
                    initiate_3 += 1
            elif (pos3[2][0]) <= mouse_x <= (pos3[2][0]) + 80 and (pos3[2][1]) <= mouse_y <= (
            pos3[2][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not pizza_1:
                    pizza_1 = True
                    initiate_3 += 1
            elif (pos3[3][0]) <= mouse_x <= (pos3[3][0]) + 80 and (pos3[3][1]) <= mouse_y <= (
            pos3[3][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not pizza_2:
                    pizza_2 = True
                    initiate_3 += 1
            elif (pos3[4][0]) <= mouse_x <= (pos3[4][0]) + 80 and (pos3[4][1]) <= mouse_y <= (
            pos3[4][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not popcorn_1:
                    popcorn_1 = True
                    initiate_3 += 1
            elif (pos3[5][0]) <= mouse_x <= (pos3[5][0]) + 80 and (pos3[5][1]) <= mouse_y <= (
            pos3[5][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not popcorn_2:
                    popcorn_2 = True
                    initiate_3 += 1
            elif (pos3[6][0]) <= mouse_x <= (pos3[6][0]) + 80 and (pos3[6][1]) <= mouse_y <= (
            pos3[6][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not burger_1:
                    burger_1 = True
                    initiate_3 += 1
            elif (pos3[7][0]) <= mouse_x <= (pos3[7][0]) + 80 and (pos3[7][1]) <= mouse_y <= (
            pos3[7][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not burger_2:
                    burger_2 = True
                    initiate_3 += 1
            elif (pos3[8][0]) <= mouse_x <= (pos3[8][0]) + 80 and (pos3[8][1]) <= mouse_y <= (
            pos3[8][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not sandwich_1:
                    sandwich_1 = True
                    initiate_3 += 1
            elif (pos3[9][0]) <= mouse_x <= (pos3[9][0]) + 80 and (pos3[9][1]) <= mouse_y <= (
            pos3[9][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not sandwich_2:
                    sandwich_2 = True
                    initiate_3 += 1
            elif (pos3[10][0]) <= mouse_x <= (pos3[10][0]) + 80 and (pos3[10][1]) <= mouse_y <= (
            pos3[10][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not cookies_1:
                    cookies_1 = True
                    initiate_3 += 1
            elif (pos3[11][0]) <= mouse_x <= (pos3[11][0]) + 80 and (pos3[11][1]) <= mouse_y <= (
            pos3[11][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not cookies_2:
                    cookies_2 = True
                    initiate_3 += 1
            elif (pos3[12][0]) <= mouse_x <= (pos3[12][0]) + 80 and (pos3[12][1]) <= mouse_y <= (
            pos3[12][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not icecream_1:
                    icecream_1 = True
                    initiate_3 += 1
            elif (pos3[13][0]) <= mouse_x <= (pos3[13][0]) + 80 and (pos3[13][1]) <= mouse_y <= (
            pos3[13][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not icecream_2:
                    icecream_2 = True
                    initiate_3 += 1
            elif (pos3[14][0]) <= mouse_x <= (pos3[14][0]) + 80 and (pos3[14][1]) <= mouse_y <= (
            pos3[14][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not whitechoc_1:
                    whitechoc_1 = True
                    initiate_3 += 1
            elif (pos3[15][0]) <= mouse_x <= (pos3[15][0]) + 80 and (pos3[15][1]) <= mouse_y <= (
            pos3[15][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not whitechoc_2:
                    whitechoc_2 = True
                    initiate_3 += 1
            elif (pos3[16][0]) <= mouse_x <= (pos3[16][0]) + 80 and (pos3[16][1]) <= mouse_y <= (
            pos3[16][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not pancakecream_1:
                    pancakecream_1 = True
                    initiate_3 += 1
            elif (pos3[17][0]) <= mouse_x <= (pos3[17][0]) + 80 and (pos3[17][1]) <= mouse_y <= (
            pos3[17][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not pancakecream_2:
                    pancakecream_2 = True
                    initiate_3 += 1
            elif (pos3[18][0]) <= mouse_x <= (pos3[18][0]) + 80 and (pos3[18][1]) <= mouse_y <= (
            pos3[18][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not chips_1:
                    chips_1 = True
                    initiate_3 += 1
            elif (pos3[19][0]) <= mouse_x <= (pos3[19][0]) + 80 and (pos3[19][1]) <= mouse_y <= (
            pos3[19][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not chips_2:
                    chips_2 = True
                    initiate_3 += 1
            elif (pos3[20][0]) <= mouse_x <= (pos3[20][0]) + 80 and (pos3[20][1]) <= mouse_y <= (
            pos3[20][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not fries_1:
                    fries_1 = True
                    initiate_3 += 1
            elif (pos3[21][0]) <= mouse_x <= (pos3[21][0]) + 80 and (pos3[21][1]) <= mouse_y <= (
            pos3[21][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not fries_2:
                    fries_2 = True
                    initiate_3 += 1
            elif (pos3[22][0]) <= mouse_x <= (pos3[22][0]) + 80 and (pos3[22][1]) <= mouse_y <= (
            pos3[22][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not donut_1:
                    donut_1 = True
                    initiate_3 += 1
            elif (pos3[23][0]) <= mouse_x <= (pos3[23][0]) + 80 and (pos3[23][1]) <= mouse_y <= (
            pos3[23][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not donut_2:
                    donut_2 = True
                    initiate_3 += 1
            elif (pos3[24][0]) <= mouse_x <= (pos3[24][0]) + 80 and (pos3[24][1]) <= mouse_y <= (
            pos3[24][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not drink_1:
                    drink_1 = True
                    initiate_3 += 1
            elif (pos3[25][0]) <= mouse_x <= (pos3[25][0]) + 80 and (pos3[25][1]) <= mouse_y <= (
            pos3[25][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not drink_2:
                    drink_2 = True
                    initiate_3 += 1
            elif (pos3[26][0]) <= mouse_x <= (pos3[26][0]) + 80 and (pos3[26][1]) <= mouse_y <= (
            pos3[26][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not cupcake_1:
                    cupcake_1 = True
                    initiate_3 += 1
            elif (pos3[27][0]) <= mouse_x <= (pos3[27][0]) + 80 and (pos3[27][1]) <= mouse_y <= (
            pos3[27][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not cupcake_2:
                    cupcake_2 = True
                    initiate_3 += 1
            elif (pos3[28][0]) <= mouse_x <= (pos3[28][0]) + 80 and (pos3[28][1]) <= mouse_y <= (
            pos3[28][1]) + 85 and canClick3:
                if mouse_click[0] == 1 and not hotdog_1:
                    hotdog_1 = True
                    initiate_3 += 1
            elif (pos3[29][0]) <= mouse_x <= (pos3[29][0]) + 80 and (pos3[29][1]) <= mouse_y <= (
            pos3[29][1]) + 85 and canClick3:
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
                display.blit(medium_box, (pos3[2][0], pos3[2][1]))
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
                display.blit(medium_box, (pos3[19][0], pos3[19][1]))
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
                elif whitechoc_1 == True and whitechoc_2 == True and not whitechoc_match:
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
                elif drink_1 == True and drink_2 == True and not drink_match:
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
            menubutton2()  # Home Button
            retrybuttonfunc2()  # Retry Button
            congratulation_easy2()  # Well Done "Pop up"
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
        global pos3, click, med_tilefade, highlight_med
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # This function will highligth the box if the mouse pointer is above it
        # Works for Medium mode only.
        for i in range(30):
            if (pos3[i][0]) <= mouse_x <= (pos3[i][0]) + 80 and (pos3[i][1]) <= mouse_y <= (pos3[i][1]) + 85:
                display.blit(highlight_med, (pos3[i][0] - 2.5, pos3[i][1] - 2.5))

    def display_pause3(time, name3):
        global canClick3, tacos_1, tacos_2, pizza_1, pizza_2, popcorn_1, popcorn_2, burger_1, burger_2, sandwich_1, sandwich_2, cookies_1, cookies_2, icecream_1, icecream_2, whitechoc_1, whitechoc_2, pancakecream_1, pancakecream_2, chips_1, chips_2, fries_1, fries_2, donut_1, donut_2, drink_1, drink_2, cupcake_1, cupcake_2, hotdog_1, hotdog_2
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
        if (
                tacos_match and pizza_match and popcorn_match and burger_match and sandwich_match and cookies_match and icecream_match and whitechoc_match and pancakecream_match and chips_match and fries_match and donut_match and drink_match and cupcake_match and hotdog_match) == True:
            display.blit(table2, (0, 0))
            display.blit(congratsEasy, (236, 100))
            # If retry is clicked it loops back and starts the game again.
            if 386 <= mouse_x <= 526 and 300 <= mouse_y <= 367:
                display.blit(congratsEasyretry, (386, 300))
                if click[0] == 1:
                    normalise_2()
                    medium_mode()
            # If Home is clicked it goes back to the Selection screen as well as resets the Medium mode.
            elif 556 <= mouse_x <= 696 and 300 <= mouse_y <= 367:
                display.blit(congratsEasyhome, (556, 300))
                if click[0] == 1:
                    normalise_2()
                    selection_screen()
                    exit(medium_mode())

    def normalise():
        # Resets all the Emojis back to False
        global angel_1, angel_2, angel_match, cool_1, cool_2, cool_match, whatever_1, whatever_2, whatever_match, worried_1, worried_2, worried_match
        angel_1, angel_2, angel_match, cool_1, cool_2, cool_match, whatever_1, whatever_2, whatever_match, worried_1, worried_2, worried_match = (
                                                                                                                                                 False,) * 12

    def normalise_2():
        # Resets all the Fast Food images back to False
        global tacos_1, tacos_2, tacos_match, pizza_1, pizza_2, pizza_match, popcorn_1, popcorn_2, popcorn_match, burger_1, burger_2, burger_match, sandwich_1, sandwich_2, sandwich_match, cookies_1, cookies_2, cookies_match, icecream_1, icecream_2, icecream_match, whitechoc_1, whitechoc_2, whitechoc_match, pancakecream_1, pancakecream_2, pancakecream_match, chips_1, chips_2, chips_match, fries_1, fries_2, fries_match, donut_1, donut_2, donut_match, drink_1, drink_2, drink_match, cupcake_1, cupcake_2, cupcake_match, hotdog_1, hotdog_2, hotdog_match
        tacos_1, tacos_2, tacos_match, pizza_1, pizza_2, pizza_match, popcorn_1, popcorn_2, popcorn_match, burger_1, burger_2, burger_match, sandwich_1, sandwich_2, sandwich_match, cookies_1, cookies_2, cookies_match, icecream_1, icecream_2, icecream_match, whitechoc_1, whitechoc_2, whitechoc_match, pancakecream_1, pancakecream_2, pancakecream_match, chips_1, chips_2, chips_match, fries_1, fries_2, fries_match, donut_1, donut_2, donut_match, drink_1, drink_2, drink_match, cupcake_1, cupcake_2, cupcake_match, hotdog_1, hotdog_2, hotdog_match = (
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     False,) * 45

    def normalise_3():
        # Resets all the Shapes back to False
        global rect_1, rect_2, rect_1A, rect_2A, hex_1, hex_2, hex_1A, hex_2A, star_1, star_2, star_1A, star_2A, circle_1, circle_2, circle_1A, circle_2A, triangle_1, triangle_2, triangle_1A, triangle_2A, opphex_1, opphex_2, opphex_1A, opphex_2A, oval_1, oval_2, oval_1A, oval_2A, heart_1, heart_2, heart_1A, heart_2A, commstar_1, commstar_2, commstar_1A, commstar_2A, splatpaint_1, splatpaint_2, splatpaint_1A, splatpaint_2A, square_1, square_2, rect_match, hex_match, star_match, circle_match, triangle_match, opphex_match, rect_Amatch, hex_Amatch, star_Amatch, circle_Amatch, triangle_Amatch, opphex_Amatch, oval_match, oval_Amatch, heart_match, heart_Amatch, commstar_match, commstar_Amatch, splatpaint_match, splatpaint_Amatch, square_match
        rect_1, rect_2, rect_1A, rect_2A, hex_1, hex_2, hex_1A, hex_2A, star_1, star_2, star_1A, star_2A, circle_1, circle_2, circle_1A, circle_2A, triangle_1, triangle_2, triangle_1A, triangle_2A, opphex_1, opphex_2, opphex_1A, opphex_2A, oval_1, oval_2, oval_1A, oval_2A, heart_1, heart_2, heart_1A, heart_2A, commstar_1, commstar_2, commstar_1A, commstar_2A, splatpaint_1, splatpaint_2, splatpaint_1A, splatpaint_2A, square_1, square_2, rect_match, hex_match, star_match, circle_match, triangle_match, opphex_match, rect_Amatch, hex_Amatch, star_Amatch, circle_Amatch, triangle_Amatch, opphex_Amatch, oval_match, oval_Amatch, heart_match, heart_Amatch, commstar_match, commstar_Amatch, splatpaint_match, splatpaint_Amatch, square_match = (
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     False,) * 63
    # ------------------------------------------------------------------------------------------------------------------- BATTLESHIPS -----------------------------------------------------------------------------------------------------------------

    # ---------- Functions ----------

    def movement_battleship(x_change, y_change):  # Deals with movement of battleships during placement process
        global ship_x, ship_y
        ship_x += x_change
        ship_y += y_change
        print("x-coord: " + str(ship_x) + " / y-coord: " + str(ship_y))  # Indicator of coordinates

    def set_collision():  # Function: Creates a collision box for grid and ships (code is inefficient I know)
        global Destroyer1_box, Destroyer2_box, Submarine1_box, Submarine2_box, Cruiser1_box, Cruiser2_box, \
            Battleship1_box, Battleship2_box, Carrier1_box, Carrier2_box, Shooting_box

        # --- Creating collision boxes for both player's battleships ---

        # -- Destroyer's collision box
        if Placing_Destroyer:
            # 18 lines of code below: draws a rectangle on a sprite which can be used to detect collisions
            if Placing_Battleships_1:
                Destroyer1_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Destroyer1_box.rect = pygame.Rect(ship_x, ship_y, 106, 52)
                    Destroyer1_box.image = pygame.Surface((106, 52))
                else:
                    Destroyer1_box.rect = pygame.Rect(ship_x, ship_y, 52, 106)
                    Destroyer1_box.image = pygame.Surface((52, 106))
                Destroyer1_box.image.fill((60, 60, 60))
            else:
                Destroyer2_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Destroyer2_box.rect = pygame.Rect(ship_x, ship_y, 106, 52)
                    Destroyer2_box.image = pygame.Surface((106, 52))
                else:
                    Destroyer2_box.rect = pygame.Rect(ship_x, ship_y, 52, 106)
                    Destroyer2_box.image = pygame.Surface((52, 106))
                Destroyer2_box.image.fill((60, 60, 60))

        # -- Submarine's collision box --
        elif Placing_Submarine:
            # 18 lines of code below: draws a rectangle on a sprite which can be used to detect collisions
            if Placing_Battleships_1:
                Submarine1_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Submarine1_box.rect = pygame.Rect(ship_x, ship_y, 160, 52)
                    Submarine1_box.image = pygame.Surface((160, 52))
                else:
                    Submarine1_box.rect = pygame.Rect(ship_x, ship_y, 52, 160)
                    Submarine1_box.image = pygame.Surface((52, 160))
                Submarine1_box.image.fill((60, 60, 60))
            else:
                Submarine2_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Submarine2_box.rect = pygame.Rect(ship_x, ship_y, 160, 52)
                    Submarine2_box.image = pygame.Surface((160, 52))
                else:
                    Submarine2_box.rect = pygame.Rect(ship_x, ship_y, 52, 160)
                    Submarine2_box.image = pygame.Surface((52, 160))
                Submarine2_box.image.fill((60, 60, 60))

        # -- Cruiser's collision box --
        elif Placing_Cruiser:
            # 18 lines of code below: draws a rectangle on a sprite which can be used to detect collisions
            if Placing_Battleships_1:
                Cruiser1_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Cruiser1_box.rect = pygame.Rect(ship_x, ship_y, 160, 52)
                    Cruiser1_box.image = pygame.Surface((160, 52))
                else:
                    Cruiser1_box.rect = pygame.Rect(ship_x, ship_y, 52, 160)
                    Cruiser1_box.image = pygame.Surface((52, 160))
                Cruiser1_box.image.fill((60, 60, 60))
            else:
                Cruiser2_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Cruiser2_box.rect = pygame.Rect(ship_x, ship_y, 160, 52)
                    Cruiser2_box.image = pygame.Surface((160, 52))
                else:
                    Cruiser2_box.rect = pygame.Rect(ship_x, ship_y, 52, 160)
                    Cruiser2_box.image = pygame.Surface((52, 160))
                Cruiser2_box.image.fill((60, 60, 60))

        # -- Battleship's collision box --
        elif Placing_Battleship:
            # 18 lines of code below: draws a rectangle on a sprite which can be used to detect collisions
            if Placing_Battleships_1:
                Battleship1_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Battleship1_box.rect = pygame.Rect(ship_x, ship_y, 214, 52)
                    Battleship1_box.image = pygame.Surface((214, 52))
                else:
                    Battleship1_box.rect = pygame.Rect(ship_x, ship_y, 52, 214)
                    Battleship1_box.image = pygame.Surface((52, 214))
                Battleship1_box.image.fill((60, 60, 60))
            else:
                Battleship2_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Battleship2_box.rect = pygame.Rect(ship_x, ship_y, 214, 52)
                    Battleship2_box.image = pygame.Surface((214, 52))
                else:
                    Battleship2_box.rect = pygame.Rect(ship_x, ship_y, 52, 214)
                    Battleship2_box.image = pygame.Surface((52, 214))
                Battleship2_box.image.fill((60, 60, 60))

        # -- Carrier's collision box --
        elif Placing_Carrier:
            # 18 lines of code below: draws a rectangle on a sprite which can be used to detect collisions
            if Placing_Battleships_1:
                Carrier1_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Carrier1_box.rect = pygame.Rect(ship_x, ship_y, 268, 52)
                    Carrier1_box.image = pygame.Surface((268, 52))
                else:
                    Carrier1_box.rect = pygame.Rect(ship_x, ship_y, 52, 268)
                    Carrier1_box.image = pygame.Surface((52, 268))
                Carrier1_box.image.fill((60, 60, 60))
            else:
                Carrier2_box = pygame.sprite.Sprite()
                if Rotated:  # If the ship is rotated, obviously the width and height would differ from when it's not
                    Carrier2_box.rect = pygame.Rect(ship_x, ship_y, 268, 52)
                    Carrier2_box.image = pygame.Surface((268, 52))
                else:
                    Carrier2_box.rect = pygame.Rect(ship_x, ship_y, 52, 268)
                    Carrier2_box.image = pygame.Surface((52, 268))
                Carrier2_box.image.fill((60, 60, 60))

        # -- Shoot_Border's Collision (the red box that allows players to choose a grid to shoot)
        elif Shooting:
            Shoot_box = pygame.sprite.Sprite()
            Shoot_box.rect = pygame.Rect(ship_x, ship_y, 52, 53)
            Shoot_box.image = pygame.Surface((52, 268))
            Shoot_box.image.fill((60, 60, 60))

    def check_collision():  # Function: checks if any ships collide with the grid border or other ships
        global ship_x, ship_y, Shoot_box

        """ 
            In this Function, I used the "except pass" code. Even though I highly discouraged myself from using it, every
            method I tried doesn't seem to work. If you're able to find another method, please email me the solution at 
            <Raywu527@Hotmail.com>
            """

        if not Rotated:
            if ship_x > 820:
                ship_x -= 54
            elif ship_x < 280:
                ship_x += 54
            if ship_y < 32.5:
                ship_y += 54
        if Rotated:
            if ship_x < 280:
                ship_x += 54
            if ship_y > 572.5:
                ship_y -= 54

        # --- Destroyer's (Grid) Border Control ---
        try:
            if Placing_Destroyer:
                if pygame.sprite.collide_rect(Destroyer1_box, Grid_box) or pygame.sprite.collide_rect(Destroyer2_box,
                                                                                                      Grid_box):
                    if Rotated:
                        if ship_x > 766:
                            ship_x -= 54
                    else:
                        if ship_y > 518.5:
                            ship_y -= 54
        except:
            pass

        # --- Submarine's (Grid) Border Control ---
        try:
            if Placing_Submarine:
                if pygame.sprite.collide_rect(Submarine1_box, Grid_box) or \
                        pygame.sprite.collide_rect(Submarine2_box, Grid_box):
                    if Rotated:
                        if ship_x > 712:
                            if ship_x > 766:
                                ship_x -= 108
                            else:
                                ship_x -= 54
                    else:
                        if ship_y > 464.5:
                            if ship_y > 518.5:
                                ship_y -= 108
                            else:
                                ship_y -= 54
        except:
            pass

        # --- Cruiser's (Grid) Border Control ---
        try:
            if Placing_Cruiser:
                if pygame.sprite.collide_rect(Cruiser1_box, Grid_box) or pygame.sprite.collide_rect(Cruiser2_box,
                                                                                                    Grid_box):
                    if Rotated:
                        if ship_x > 712:
                            if ship_x > 766:
                                ship_x -= 108
                            else:
                                ship_x -= 54
                    else:
                        if ship_y > 464.5:
                            if ship_y > 518.5:
                                ship_y -= 108
                            else:
                                ship_y -= 54
        except:
            pass

        # --- Battleship's (Grid) Border Control ---
        try:
            if Placing_Battleship:
                if pygame.sprite.collide_rect(Battleship1_box, Grid_box) or pygame.sprite.collide_rect(Battleship2_box,
                                                                                                       Grid_box):
                    if Rotated:
                        if ship_x > 658:
                            if ship_x > 712:
                                if ship_x > 766:
                                    ship_x -= 162
                                else:
                                    ship_x -= 108
                            else:
                                ship_x -= 54

                    else:
                        if ship_y > 410.5:
                            if ship_y > 464.5:
                                if ship_y > 518.5:
                                    ship_y -= 162
                                else:
                                    ship_y -= 108
                            else:
                                ship_y -= 54

        except:
            pass

        # --- Carrier's (Grid) Border Control ---
        try:
            if Placing_Carrier:
                if pygame.sprite.collide_rect(Carrier1_box, Grid_box) or pygame.sprite.collide_rect(Carrier2_box,
                                                                                                    Grid_box):
                    if Rotated:
                        if ship_x > 604:
                            if ship_x > 658:
                                if ship_x > 712:
                                    if ship_x > 766:
                                        ship_x -= 216
                                    else:
                                        ship_x -= 162
                                else:
                                    ship_x -= 108
                            else:
                                ship_x -= 54
                    else:
                        if ship_y > 356.5:
                            if ship_y > 410.5:
                                if ship_y > 464.5:
                                    if ship_y > 518.5:
                                        ship_y -= 216
                                    else:
                                        ship_y -= 162
                                else:
                                    ship_y -= 108
                            else:
                                ship_y -= 54

        except:
            pass

        # --- Shoot Box's Border Control ---
        try:
            if Shooting:
                if pygame.sprite.collide_rect(Shoot_box, Grid_box):
                    if ship_x > 820:
                        ship_x -= 54
                    if ship_y > 572.5:
                        print("why")
                        ship_y -= 54
        except:
            pass

    def rotation_battleship():  # Function: Allows the rotation of ships
        global img_Destroyer, img_Submarine, img_Cruiser, img_Battleship, img_Carrier, Rotated
        if Placing_Destroyer:
            img_Destroyer = pygame.transform.rotate(img_Destroyer, 90)
        elif Placing_Submarine:
            img_Submarine = pygame.transform.rotate(img_Submarine, 90)
        elif Placing_Cruiser:
            img_Cruiser = pygame.transform.rotate(img_Cruiser, 90)
        elif Placing_Battleship:
            img_Battleship = pygame.transform.rotate(img_Battleship, 90)
        else:
            img_Carrier = pygame.transform.rotate(img_Carrier, 90)
        if Rotated:
            Rotated = False
        else:
            Rotated = True

    def placement_battleship():  # --Function: Allows the transition from the placement of one ship to another + blit's ship
        global Placing_Battleships_2, Placing_Battleships_1, Destroyer1_box, Destroyer2_box, Submarine1_box, \
            Submarine2_box, Cruiser1_box, Cruiser2_box, Battleship1_box, Battleship2_box, Carrier1_box, Carrier2_box

        # --- Destroyer's ship placement ---
        if Placing_Destroyer:
            if Placing_Battleships_1:
                img_Tiles_1.blit(img_Destroyer, (ship_x, ship_y))
                data_controller("placing_new_ship", "Destroyer")
            elif Placing_Battleships_2:
                img_Tiles_2.blit(img_Destroyer, (ship_x, ship_y))
            data_controller("placing_new_ship", "Destroyer")

        # --- Submarine's ship placement ---
        elif Placing_Submarine:
            if Placing_Battleships_1:
                if not pygame.sprite.collide_rect(Submarine1_box,
                                                  Destroyer1_box):  # Detects interceptions with other ships
                    img_Tiles_1.blit(img_Submarine, (ship_x, ship_y))
                    data_controller("placing_new_ship", "Submarine")
                else:
                    print("nope")
            else:
                if not pygame.sprite.collide_rect(Submarine2_box,
                                                  Destroyer2_box):  # Same purpose but for Player2's ships
                    img_Tiles_2.blit(img_Submarine, (ship_x, ship_y))
                    data_controller("placing_new_ship", "Submarine")
                else:
                    print("interception detected")

        # --- Cruiser's ship placement ---
        elif Placing_Cruiser:
            if Placing_Battleships_1:
                if not pygame.sprite.collide_rect(Cruiser1_box, Destroyer1_box) and \
                        not pygame.sprite.collide_rect(Cruiser1_box, Submarine1_box):
                    img_Tiles_1.blit(img_Cruiser, (ship_x, ship_y))
                    data_controller("placing_new_ship", "Cruiser")
                else:
                    print("nope")
            else:
                if not pygame.sprite.collide_rect(Cruiser2_box, Destroyer2_box) and \
                        not pygame.sprite.collide_rect(Cruiser2_box, Submarine2_box):
                    img_Tiles_2.blit(img_Cruiser, (ship_x, ship_y))
                    data_controller("placing_new_ship", "Cruiser")
                else:
                    print("nope")

        # --- Battleship's ship placement ---
        elif Placing_Battleship:
            if Placing_Battleships_1:
                if not pygame.sprite.collide_rect(Battleship1_box, Destroyer1_box) and \
                        not pygame.sprite.collide_rect(Battleship1_box, Submarine1_box) and \
                        not pygame.sprite.collide_rect(Battleship1_box, Cruiser1_box):
                    img_Tiles_1.blit(img_Battleship, (ship_x, ship_y))
                    data_controller("placing_new_ship", "Battleship")
                else:
                    print("nope")
            else:
                if not pygame.sprite.collide_rect(Battleship2_box, Destroyer2_box) and \
                        not pygame.sprite.collide_rect(Battleship2_box, Submarine2_box) and \
                        not pygame.sprite.collide_rect(Battleship2_box, Cruiser2_box):
                    img_Tiles_2.blit(img_Battleship, (ship_x, ship_y))
                    data_controller("placing_new_ship", "Battleship")
                else:
                    print("nope")

        # --- Carrier's ship placement ---
        elif Placing_Carrier:
            if Placing_Battleships_1:
                if not pygame.sprite.collide_rect(Carrier1_box, Destroyer1_box) and \
                        not pygame.sprite.collide_rect(Carrier1_box, Submarine1_box) and \
                        not pygame.sprite.collide_rect(Carrier1_box, Cruiser1_box) and \
                        not pygame.sprite.collide_rect(Carrier1_box, Battleship1_box):
                    img_Tiles_1.blit(img_Carrier, (ship_x, ship_y))
                    data_controller("placing_new_ship", "Carrier")
                else:
                    print("nope")
            else:
                if not pygame.sprite.collide_rect(Carrier2_box, Destroyer2_box) and \
                        not pygame.sprite.collide_rect(Carrier2_box, Submarine2_box) and \
                        not pygame.sprite.collide_rect(Carrier2_box, Cruiser2_box) and \
                        not pygame.sprite.collide_rect(Carrier2_box, Battleship2_box):
                    img_Tiles_2.blit(img_Carrier, (ship_x, ship_y))
                    data_controller("placing_new_ship", "Carrier")
                else:
                    print("nope")

    def data_controller(command, extra_helper_variable):  # Deals with setting/resetting data
        # Note: Not all data are set here, some are established in other functions

        global img_Destroyer, img_Submarine, img_Cruiser, img_Battleship, img_Carrier, Rotated, \
            Placing_Destroyer, Placing_Submarine, Placing_Cruiser, Placing_Battleship, Placing_Carrier, \
            Placing_Battleships_1, Placing_Battleships_2, Shooting

        if command == "placing_new_ship":  # When ship images are rotated, they have to be rotated back
            img_Destroyer = pygame.image.load('DataFile/Battleships_images/Destroyer.png')
            img_Submarine = pygame.image.load('DataFile/Battleships_images/Submarine.png')
            img_Cruiser = pygame.image.load('DataFile/Battleships_images/Cruiser.png')
            img_Battleship = pygame.image.load('DataFile/Battleships_images/Battleship.png')
            img_Carrier = pygame.image.load('DataFile/Battleships_images/Carrier.png')
            Rotated = False
            if extra_helper_variable == "Destroyer":
                Placing_Destroyer = False
                Placing_Submarine = True
            elif extra_helper_variable == "Submarine":
                Placing_Submarine = False
                Placing_Cruiser = True
            elif extra_helper_variable == "Cruiser":
                Placing_Cruiser = False
                Placing_Battleship = True
            elif extra_helper_variable == "Battleship":
                Placing_Battleship = False
                Placing_Carrier = True
            else:
                if Placing_Battleships_1:
                    Placing_Carrier = False
                    Placing_Destroyer = True
                    Placing_Battleships_1 = False
                    Placing_Battleships_2 = True
                else:
                    Placing_Carrier = False
                    Placing_Battleships_2 = False
                    Shooting = True

    def shoot():  # Function: Allows users to choose a grid and shoot it to reveal a "hit" or "miss"
        global Shoot_box, Collision, Player_1_Turn, Player_2_Turn

        # 4 lines of code Below: The coordinates of the grid shot are transformed into a collision hit box
        Shoot_box = pygame.sprite.Sprite()
        Shoot_box.rect = pygame.Rect(ship_x, ship_y, 52, 53)
        Shoot_box.image = pygame.Surface((52, 53))
        Shoot_box.image.fill((60, 60, 60))
        print(Shots_Fired1_x)
        print(Shots_Fired1_y)

        # --- Player 1's Turn to Shoot
        if Player_1_Turn:
            global Destroyer1, Destroyer2, Submarine1, Submarine2, Cruiser1, Cruiser2, Battleship1, Battleship2, Carrier1, \
                Carrier2
            """ Below: This is a rather genius piece of code (made by the only Raymond). The hit-boxes of previously fired 
            shots are saved in a list, the coordinates in that list is then used to detect collision with the current shot
            made. The FOR loop is used to detect collision until all coordinates in the list is calculated.
            """
            for i in range(len(Shots_Fired1_x)):
                dummy_box = pygame.sprite.Sprite()
                dummy_box.rect = pygame.Rect(Shots_Fired1_x[i], Shots_Fired1_y[i], 52, 53)
                dummy_box.image = pygame.Surface((52, 53))
                dummy_box.image.fill((60, 60, 60))
                # Below: If Collision is true, this means that they've already shot the grid before
                if pygame.sprite.collide_rect(Shoot_box, dummy_box):
                    Collision = True

            if Collision:
                print("Already shot there")
                Collision = False
            else:
                # If the shot hit any ships, the "if" statement below will run
                if pygame.sprite.collide_rect(Shoot_box, Destroyer2_box) or \
                        pygame.sprite.collide_rect(Shoot_box, Submarine2_box) or \
                        pygame.sprite.collide_rect(Shoot_box, Cruiser2_box) or \
                        pygame.sprite.collide_rect(Shoot_box, Battleship2_box) or \
                        pygame.sprite.collide_rect(Shoot_box, Carrier2_box):
                    if pygame.sprite.collide_rect(Shoot_box, Destroyer2_box):
                        Destroyer2 += 1
                    elif pygame.sprite.collide_rect(Shoot_box, Submarine2_box):
                        Submarine2 += 1
                    elif pygame.sprite.collide_rect(Shoot_box, Cruiser2_box):
                        Cruiser2 += 1
                    elif pygame.sprite.collide_rect(Shoot_box, Battleship2_box):
                        Battleship2 += 1
                    elif pygame.sprite.collide_rect(Shoot_box, Carrier2_box):
                        Carrier2 += 1
                    img_Tiles_1_Field.blit(img_Hit_Field, (ship_x, ship_y))
                    img_Tiles_2.blit(img_Hit, (ship_x, ship_y))
                    img_Tiles_1_Field.blit(img_instructions_hit, (15, 290))
                    img_Tiles_2_Field.blit(img_instructions_hit, (15, 290))
                # Otherwise if the shot misses
                else:
                    # 2 lines of code Below: blit's "miss" indication on grid board, "hit" indications are set in a function
                    img_Tiles_1_Field.blit(img_Miss, (ship_x, ship_y))
                    img_Tiles_2.blit(img_Miss, (ship_x, ship_y))
                    img_Tiles_1_Field.blit(img_instructions_miss, (15, 290))
                    img_Tiles_2_Field.blit(img_instructions_miss, (15, 290))
                # 2 lines of code Below: The two lists mentioned before then store the coordinates of the grid shot
                Shots_Fired1_x.append(ship_x)
                Shots_Fired1_y.append(ship_y)
                Player_1_Turn = False
                Player_2_Turn = True

        # --- Player 2's Turn to Shoot
        else:

            for i in range(len(Shots_Fired2_x)):
                dummy_box = pygame.sprite.Sprite()
                dummy_box.rect = pygame.Rect(Shots_Fired2_x[i], Shots_Fired2_y[i], 52, 53)
                dummy_box.image = pygame.Surface((52, 53))
                dummy_box.image.fill((60, 60, 60))
                # Below: If Collision is true, this means that they've already shot the grid before
                if pygame.sprite.collide_rect(Shoot_box, dummy_box):
                    Collision = True

            if Collision:
                print("Already shot there")
                Collision = False
            else:
                # If the shot hit any ships, the "if" statement below will run
                if pygame.sprite.collide_rect(Shoot_box, Destroyer1_box) or \
                        pygame.sprite.collide_rect(Shoot_box, Submarine1_box) or \
                        pygame.sprite.collide_rect(Shoot_box, Cruiser1_box) or \
                        pygame.sprite.collide_rect(Shoot_box, Battleship1_box) or \
                        pygame.sprite.collide_rect(Shoot_box, Carrier1_box):
                    if pygame.sprite.collide_rect(Shoot_box, Destroyer1_box):
                        Destroyer1 += 1
                    elif pygame.sprite.collide_rect(Shoot_box, Submarine1_box):
                        Submarine1 += 1
                    elif pygame.sprite.collide_rect(Shoot_box, Cruiser1_box):
                        Cruiser1 += 1
                    elif pygame.sprite.collide_rect(Shoot_box, Battleship1_box):
                        Battleship1 += 1
                    elif pygame.sprite.collide_rect(Shoot_box, Carrier1_box):
                        Carrier1 += 1
                    img_Tiles_2_Field.blit(img_Hit_Field, (ship_x, ship_y))
                    img_Tiles_1.blit(img_Hit, (ship_x, ship_y))
                    img_Tiles_2_Field.blit(img_instructions_hit, (866, 290))
                    img_Tiles_1_Field.blit(img_instructions_hit, (866, 290))
                    # Otherwise if the shot misses
                else:
                    # 2 lines of code Below: blit's "miss" indication on grid board, "hit" indications are set in code above
                    img_Tiles_2_Field.blit(img_Miss, (ship_x, ship_y))
                    img_Tiles_1.blit(img_Miss, (ship_x, ship_y))
                    img_Tiles_2_Field.blit(img_instructions_miss, (866, 290))
                    img_Tiles_1_Field.blit(img_instructions_miss, (866, 290))
                # 2 lines of code Below: The two lists mentioned before then store the coordinates of the grid shot
                Shots_Fired2_x.append(ship_x)
                Shots_Fired2_y.append(ship_y)
                Player_1_Turn = True
                Player_2_Turn = False

        check_battleship_hits()  # Check if any battleships are sunk

    def check_battleship_hits():  # Checks the amount of hits a ship has taken and then blit's a message for ships destroyed
        global Destroyer1, Destroyer2, Submarine1, Submarine2, Cruiser1, Cruiser2, Battleship1, Battleship2, Carrier1, \
            Carrier2, Shooting
        if Destroyer1 == 2:
            img_Tiles_1_Field.blit(img_instructions_destroyer_destroyed, (0, 150))
            img_Tiles_2_Field.blit(img_instructions_destroyer_destroyed, (0, 150))
        if Submarine1 == 3:
            img_Tiles_1_Field.blit(img_instructions_submarine_destroyed, (0, 175))
            img_Tiles_2_Field.blit(img_instructions_submarine_destroyed, (0, 175))
        if Cruiser1 == 3:
            img_Tiles_1_Field.blit(img_instructions_cruiser_destroyed, (0, 200))
            img_Tiles_2_Field.blit(img_instructions_cruiser_destroyed, (0, 200))
        if Battleship1 == 4:
            img_Tiles_1_Field.blit(img_instructions_battleship_destroyed, (0, 225))
            img_Tiles_2_Field.blit(img_instructions_battleship_destroyed, (0, 225))
        if Carrier1 == 5:
            img_Tiles_1_Field.blit(img_instructions_carrier_destroyed, (0, 250))
            img_Tiles_2_Field.blit(img_instructions_carrier_destroyed, (0, 250))

        if Destroyer2 == 2:
            img_Tiles_1_Field.blit(img_instructions_destroyer_destroyed, (850, 150))
            img_Tiles_2_Field.blit(img_instructions_destroyer_destroyed, (850, 150))
        if Submarine2 == 3:
            img_Tiles_1_Field.blit(img_instructions_submarine_destroyed, (850, 175))
            img_Tiles_2_Field.blit(img_instructions_submarine_destroyed, (850, 175))
        if Cruiser2 == 3:
            img_Tiles_1_Field.blit(img_instructions_cruiser_destroyed, (850, 200))
            img_Tiles_2_Field.blit(img_instructions_cruiser_destroyed, (850, 200))
        if Battleship2 == 4:
            img_Tiles_1_Field.blit(img_instructions_battleship_destroyed, (850, 225))
            img_Tiles_2_Field.blit(img_instructions_battleship_destroyed, (850, 225))
        if Carrier2 == 5:
            img_Tiles_1_Field.blit(img_instructions_carrier_destroyed, (850, 250))
            img_Tiles_2_Field.blit(img_instructions_carrier_destroyed, (850, 250))

        # -- Checks if all the ships of a player is destroyed to initiate end game
        if Destroyer1 == 2 and Submarine1 == 3 and Cruiser1 == 3 and Battleship1 == 4 and Carrier1 == 5:
            print("Player 2 won!")
            Shooting = False
            display.blit(img_player_2_wins, (0, 0))

        elif Destroyer2 == 2 and Submarine2 == 3 and Cruiser2 == 3 and Battleship2 == 4 and Carrier2 == 5:
            print("Player 1 won!")
            Shooting = False
            display.blit(img_player_1_wins, (0, 0))

    def constant_blit():  # Function: Deals with displaying images on screen in a manner as smooth as possible
        # Note: not all blit's are performed here, some are initiated in other functions
        if Title_battleship:  # --Title Screen/Home Page
            global rel_x, bg_x, stop_blit, event_test, goToHome
            rel_x = bg_x % img_Title.get_rect().width
            display.blit(img_Title_Ship, (0, 10))
            display.blit(img_Title, (rel_x - img_Title.get_rect().width, 0))
            if rel_x < 2200:
                display.blit(img_Title, (rel_x, 0))
            bg_x -= 10
        if Title_battleship:
            x, y = pygame.mouse.get_pos()
            display.blit(img_Title_Ship, (0, 0))
            display.blit(img_Title_Submarine, (0, 0))
            if 32 <= x <= 109 and 471 <= y <= 581:
                display.blit(bridgeHome_2, (20, 480))
                if not goToHome:
                    goToHome = True
            else:
                display.blit(bridgeHome_1, (20, 480))
                if goToHome:
                    goToHome = False

        # --Below: every time the ship is moved, the new image replaces the old
        elif Placing_Battleships_1 or Placing_Battleships_2:
            if Placing_Battleships_1:
                display.blit(img_Tiles_1, (0, 0))
                display.blit(img_instructions_placement, (40, 96))
            else:
                display.blit(img_Tiles_2, (0, 0))
                display.blit(img_instructions_placement, (888, 98))
            display.blit(img_back, (0, 0))
            if Placing_Destroyer:
                display.blit(img_Destroyer, (ship_x, ship_y))
            elif Placing_Submarine:
                display.blit(img_Submarine, (ship_x, ship_y))
            elif Placing_Cruiser:
                display.blit(img_Cruiser, (ship_x, ship_y))
            elif Placing_Battleship:
                display.blit(img_Battleship, (ship_x, ship_y))
            elif Placing_Carrier:
                display.blit(img_Carrier, (ship_x, ship_y))

        elif Shooting:  # --Code is initiated after both players have finished placing battleships and enter shooting phase
            if Player_1_Turn and not stop_blit:
                display.blit(img_Tiles_1_Field, (0, 0))
                display.blit(img_instructions_shooting, (36, 96))
            elif not Player_2_Turn:
                display.blit(img_Tiles_1, (0, 0))
                event_test = True
            display.blit(img_back, (0, 0))

            if Player_2_Turn and not stop_blit:
                display.blit(img_Tiles_2_Field, (0, 0))
                display.blit(img_instructions_shooting, (885, 98))
            elif not Player_1_Turn:
                display.blit(img_Tiles_2, (0, 0))
                event_test = True
            display.blit(img_Hit_Box, (ship_x, ship_y))
            display.blit(img_back, (0, 0))

    # ---------------- Normalising the variables ----------------
    def normalise_ships():
        global Destroyer1, Destroyer2, Submarine1, Submarine2, Cruiser1, Cruiser2, Battleship1, Battleship2, Carrier1, Carrier2, Shots_Fired1_x, Shots_Fired1_y, Shots_Fired2_x, Shots_Fired2_y, Placing_Battleship, Placing_Battleships_1, Placing_Battleships_2
        global Placing_Carrier, Placing_Cruiser, Placing_Submarine, Placing_Destroyer, battleship_loop, Player_1_Turn, Rotated, Title_battleship, Shooting, Collision, ship_x, ship_y, bg_x
        # --- Data and Variables ---
        Destroyer1 = Destroyer2 = Submarine1 = Submarine2 = Cruiser1 = Cruiser2 = Battleship1 = Battleship2 = Carrier1 = \
            Carrier2 = 0  # These variables are used to detect the amount of hits on a specific ship
        Shots_Fired1_x = []
        Shots_Fired1_y = []  # For some reason these lists add on to each other when placed like this: "a = b = c = d = []"
        Shots_Fired2_y = []
        Shots_Fired2_x = []
        Placing_Battleships_1 = False  # Game always start with player 1 placing battleships first
        Placing_Battleships_2 = False
        Placing_Destroyer = True
        Placing_Submarine = Placing_Cruiser = Placing_Battleship = Placing_Carrier = False
        battleship_loop = True  # Used to detect if the user closed the program
        Player_1_Turn = True  # Determines which player's turn it is to shoot a grid
        Rotated = False  # Determines if the ships are rotated during placement
        Title_battleship = True  # Displays Title screen
        Shooting = False  # Determines whether the players have finished placing ships to enter shooting phase
        Collision = False  # Used to determine whether collision between two sprites exist [specifically used in "shoot()"]
        ship_y = 33.5
        ship_x = 281
        bg_x = 0

    # ----------------- Main Program -----------------
    def main_battleship():
        print("main")

        # --- Global variables ---
        global Destroyer1, Destroyer2, Submarine1, Submarine2, Cruiser1, Cruiser2, Battleship1, Battleship2, Carrier1, \
            Carrier2, Shots_Fired1_x, Shots_Fired1_y, Shots_Fired2_x, Shots_Fired2_y, Placing_Battleships_2, \
            battleship_loop, Player_1_Turn, Rotated, Title_battleship, ship_y, ship_x, event, Placing_Battleships_1, \
            Placing_Destroyer, Placing_Submarine, Placing_Cruiser, Placing_Battleship, Placing_Carrier, Grid_box, \
            Shooting, Collision, img_Tiles_1, img_Tiles_2, img_Tiles_1_Field, img_Tiles_2_Field, img_Destroyer, \
            img_Submarine, img_Cruiser, img_Battleship, img_Carrier, img_Hit_Box, img_Miss, img_Hit, img_Hit_Field, \
            img_Title, display, img_Title_Ship, img_Title_Submarine, img_Red_Button, img_instructions_placement, \
            bg_x, img_instructions_shooting, img_instructions_destroyer_destroyed, img_instructions_submarine_destroyed, \
            img_instructions_cruiser_destroyed, img_instructions_battleship_destroyed, img_instructions_carrier_destroyed, \
            img_player_1_wins, img_player_2_wins, img_instructions_miss, img_instructions_hit, Player_2_Turn, stop_blit, \
            event_test, img_back

        # ---------- Images ----------
        img_Tiles_1 = pygame.image.load('DataFile/Battleships_images/Tiles.png')
        img_Tiles_2 = pygame.image.load('DataFile/Battleships_images/Tiles.png')
        img_Tiles_1_Field = pygame.image.load('DataFile/Battleships_images/Tiles.png')
        img_Tiles_2_Field = pygame.image.load('DataFile/Battleships_images/Tiles.png')
        img_Destroyer = pygame.image.load('DataFile/Battleships_images/Destroyer.png')
        img_Submarine = pygame.image.load('DataFile/Battleships_images/Submarine.png')
        img_Cruiser = pygame.image.load('DataFile/Battleships_images/Cruiser.png')
        img_Battleship = pygame.image.load('DataFile/Battleships_images/Battleship.png')
        img_Carrier = pygame.image.load('DataFile/Battleships_images/Carrier.png')
        img_Hit_Box = pygame.image.load('DataFile/Battleships_images/Hit_Box.png')
        img_Miss = pygame.image.load('DataFile/Battleships_images/Miss.png')
        img_Hit = pygame.image.load('DataFile/Battleships_images/Hit.png')
        img_Hit_Field = pygame.image.load('DataFile/Battleships_images/Hit.png')
        img_instructions_placement = pygame.image.load('DataFile/Battleships_images/instruct_Placement.png')
        img_instructions_shooting = pygame.image.load('DataFile/Battleships_images/instruct_Shooting.png')
        img_instructions_destroyer_destroyed = pygame.image.load(
            'DataFile/Battleships_images/instruct_destroyer_destroyed.png')
        img_instructions_submarine_destroyed = pygame.image.load(
            'DataFile/Battleships_images/instruct_submarine_destroyed.png')
        img_instructions_cruiser_destroyed = pygame.image.load(
            'DataFile/Battleships_images/instruct_cruiser_destroyed.png')
        img_instructions_battleship_destroyed = pygame.image.load(
            'DataFile/Battleships_images/instruct_battleship_destroyed.png')
        img_instructions_carrier_destroyed = pygame.image.load(
            'DataFile/Battleships_images/instruct_carrier_destroyed.png')
        img_player_1_wins = pygame.image.load('DataFile/Battleships_images/player_1_win.png')
        img_player_2_wins = pygame.image.load('DataFile/Battleships_images/player_2_win.png')
        img_instructions_miss = pygame.image.load('DataFile/Battleships_images/instruct_miss.png')
        img_instructions_hit = pygame.image.load('DataFile/Battleships_images/instruct_hit.png')
        img_back = pygame.image.load('DataFile/Battleships_images/Back.png')

        # ---Images needed for title screen
        img_Title = pygame.image.load('DataFile/Battleships_images/Battleship_Title.png')
        img_Title_Ship = pygame.image.load('DataFile/Battleships_images/Title_Ship.png')
        img_Title_Submarine = pygame.image.load('DataFile/Battleships_images/Title_Submarine.png')

        # ---------- Screen Adjustments + Clock + Caption ----------
        display = pygame.display.set_mode((1100, 605))
        display.blit(img_Title, (0, 0))
        pygame.display.set_caption("Battleship")
        clock = pygame.time.Clock()  # Manages the rate that the screen updates

        # --- Data and Variables ---
        Destroyer1 = Destroyer2 = Submarine1 = Submarine2 = Cruiser1 = Cruiser2 = Battleship1 = Battleship2 = Carrier1 = \
            Carrier2 = 0  # These variables are used to detect the amount of hits on a specific ship
        # 4 lines of code below: Used to store coordinates of grids previously shot to avoid the same grid being shot twice
        Shots_Fired1_x = []
        Shots_Fired1_y = []  # For some reason these lists add on to each other when placed like this: "a = b = c = d = []"
        Shots_Fired2_y = []
        Shots_Fired2_x = []
        Placing_Battleships_1 = False  # Game always start with player 1 placing battleships first
        Placing_Battleships_2 = False
        # 2 lines of code below: Determines which ship is being placed on the board
        Placing_Destroyer = True
        Placing_Submarine = Placing_Cruiser = Placing_Battleship = Placing_Carrier = False
        battleship_loop = True  # Used to detect if the user closed the program
        Player_1_Turn = True  # Determines which player's turn it is to shoot a grid
        Player_2_Turn = False
        Rotated = False  # Determines if the ships are rotated during placement
        Title_battleship = True  # Displays Title screen
        Shooting = False  # Determines whether the players have finished placing ships to enter shooting phase
        Collision = False  # Used to determine whether collision between two sprites exist [specifically used in "shoot()"]
        # variables 'ship_y' and 'ship_x' are used to
        stop_blit = False
        ship_y = 33.5
        ship_x = 281
        event_test = False

        # -- Variables for Aesthetics ---
        bg_x = 0

        # --- Extra variables ---
        # 4 lines of code below: creates a collision box for the grid board
        Grid_box = pygame.sprite.Sprite()
        Grid_box.rect = pygame.Rect(280, 32.5, 540, 540)
        Grid_box.image = pygame.Surface((540, 540))
        Grid_box.image.fill((60, 60, 60))

        # --- Main Loop ---
        while battleship_loop:
            pygame.display.flip()  # --Updates Screen
            constant_blit()  # --constantly blit's images on to screen to provide smooth transitions
            set_collision()  # --Runs the function that sets collision boxes
            clock.tick(60)  # --60 frames per second
            check_collision()  # ---placed here to constantly update position without error

            for event in pygame.event.get():  # --Detects user inputs
                # --- Detection of program closing ---
                if event.type == pygame.QUIT:
                    battleship_loop = False
                    pygame.quit(), sys.exit()

                print(pygame.mouse.get_pos())

                # --- Detection of keyboard inputs ---
                if event.type == pygame.KEYDOWN:

                    # -- RIGHT KEY --
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        print("Right/'d'")
                        movement_battleship(54, 0)  # 54 units right
                        if event_test:
                            # Because of nearing the deadline, the 8 lines of code below is repeated for every movement made
                            if Player_1_Turn:
                                display.blit(img_Tiles_1, (0, 0))
                                stop_blit = False
                                event_test = False
                            elif Player_2_Turn:
                                display.blit(img_Tiles_2, (0, 0))
                                stop_blit = False
                                event_test = False

                    # -- LEFT KEY --
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        print("Left/'a'")
                        movement_battleship(-54, 0)  # 54 units left
                        if event_test:
                            if Player_1_Turn:
                                display.blit(img_Tiles_1, (0, 0))
                                stop_blit = False
                                event_test = False
                            elif Player_2_Turn:
                                display.blit(img_Tiles_2, (0, 0))
                                stop_blit = False
                                event_test = False

                    # -- UP KEY --
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        print("Up/'w'")
                        movement_battleship(0, -54)  # 54 units up
                        if event_test:
                            if Player_1_Turn:
                                display.blit(img_Tiles_1, (0, 0))
                                stop_blit = False
                                event_test = False
                            elif Player_2_Turn:
                                display.blit(img_Tiles_2, (0, 0))
                                stop_blit = False
                                event_test = False

                    # -- DOWN KEY --
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        print("Down/'s'")
                        movement_battleship(0, 54)  # 54 units down
                        if event_test:
                            if Player_1_Turn:
                                display.blit(img_Tiles_1, (0, 0))
                                stop_blit = False
                                event_test = False
                            elif Player_2_Turn:
                                display.blit(img_Tiles_2, (0, 0))
                                stop_blit = False
                                event_test = False

                    # -- SPACE KEY --
                    elif event.key == pygame.K_SPACE:
                        print("Space_Bar")
                        if Title_battleship:
                            Title_battleship = False
                            Placing_Battleships_1 = True
                        elif Placing_Battleships_1 or Placing_Battleships_2:
                            set_collision()  # --Runs the function that sets collision boxes
                            placement_battleship()
                        elif Shooting:
                            shoot()

                    # --- pressing '1' and '2' allows the player shooting to see the location of their ships + enemy shots
                    # -- '1' KEY --
                    elif event.key == pygame.K_1:
                        if Shooting:
                            if Player_1_Turn:
                                stop_blit = True

                    # -- '2' KEY --
                    elif event.key == pygame.K_2:
                        if Shooting:
                            if Player_2_Turn:
                                stop_blit = True

                    # -- 'r' KEY --
                    elif event.key == pygame.K_r:
                        print("'r'")
                        if Placing_Battleships_1 or Placing_Battleships_2:
                            rotation_battleship()

                    # -- '5' KEY --
                    elif event.key == pygame.K_5:
                        main_battleship()

                    check_collision()  # --checks if a ship intercept the grid border

                # -- Mouse Button Pressed
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    global transition, leaveBridge, chosenGame
                    if Title_battleship:
                        if (758, 485) < pygame.mouse.get_pos() < (1058, 564):
                            Title_battleship = False
                            Placing_Battleships_1 = True
                    else:
                        if (0, 45) < pygame.mouse.get_pos() < (59, 0):
                            main_battleship()
                    if goToHome:
                        normalise_ships()
                        transition, leaveBridge, chosenGame, battleship_loop = False, False, "", False
                        #pygame.time.wait(200)

    # The function for the settings page of the bridge
    def settings_function():

        # Global decleration of variables
        global onHomeButton

        # Gets the position of the mouse
        x, y = pygame.mouse.get_pos()

        # Displaying the adhering settings page and home button
        display.blit(snowyMountain, (0, 0))
        if 32 <= x <= 109 and 471 <= y <= 581:
            display.blit(bridgeHome_2, (20, 480))
            if not onHomeButton:
                onHomeButton = True
        else:
            display.blit(bridgeHome_1, (20, 480))
            if onHomeButton:
                onHomeButton = False

    # The function for the userguide page of the bridge
    def userguide_function():

        # Global decleration of variables
        global onHomeButton

        # Gets the position of the mouse
        x, y = pygame.mouse.get_pos()

        # Displaying the adhering userguide page and home button
        display.blit(strangePlanets, (0, 0))
        if 32 <= x <= 109 and 471 <= y <= 581:
            display.blit(bridgeHome_2, (20, 480))
            if not onHomeButton:
                onHomeButton = True
        else:
            display.blit(bridgeHome_1, (20, 480))
            if onHomeButton:
                onHomeButton = False

    # The function for the loading screen (transition screen)
    def loading(n, name):

        # Global decleration of variables
        global iter1, transition, leaveBridge, loadingSequence

        # Looping 10 times to display the changing 'loading bar' text (), (.), (..), (...)
        for i in range(1, 10):
            if iter1 == 4:
                pygame.time.wait(n)
                iter1 = 1
            pygame.time.wait(n)
            iter1 += 1

        # Declaring end of transition
        transition, iter1 = False, 1

        # Just a reminder of which game is being picked, and for Snakes & Ladders, enabling the Tutorial page
        if not leaveBridge:
            leaveBridge, loadingSequence = True, False
            if chosenGame == "snakes":
                vars.firstTime = True
            elif chosenGame == "ships":
                print('battleships')
            elif chosenGame == "memory":
                print('memory')

    # Main function for the bridge page
    def main_screen0():

        # Global decleration of variable
        global loadingSequence

        # Displaying the various colored images depending on whether the mouse is hovering over the according image
        if not memoryHover:
            display.blit(vars.memory_Bridge2, (0, 0))
        else:
            display.blit(vars.memory_Bridge, (0, 0))
        if not bridgeHover:
            display.blit(vars.about_Bridge2, (0, 0))
        else:
            display.blit(vars.about_Bridge, (0, 0))
        if not settingsHover:
            display.blit(vars.settings_Bridge2, (0, 0))
        else:
            display.blit(vars.settings_Bridge, (0, 0))
        if not battleshipsHover:
            display.blit(vars.battleships_Bridge2, (0, 0))
        else:
            display.blit(vars.battleships_Bridge, (0, 0))
        if not snakesHover:
            display.blit(vars.snakes_Bridge2, (0, 0))
        else:
            display.blit(vars.snakes_Bridge, (0, 0))

        # Starting the loading bar transition once a game has been selected
        if transition:
            display.blit(vars.__dict__["loading" + str(iter1)], (0, 0))
            if not loadingSequence:

                # Thread for allowing the game to start the transition process
                loadingSequence = True
                t = threading.Thread(target=loading, name='sleeperFunction', args=(500, 'sleeperFunction'))
                t.start()
                
    # Starts the main while loop to begin the 'blit' or displaying process according to set precepts (variables/functions and such)
    main_screen()

# Starting the main function of the program once everything has finished loading (This causes short unresponsiveness, but nothing majour)
main_function()
