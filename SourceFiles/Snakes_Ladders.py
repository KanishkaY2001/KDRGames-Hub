# Importing modules
import pygame, sys, os, threading, time, random
from random import seed

# Defining the file directories for easy access
snakes_script_dir = os.path.dirname(os.path.abspath(__file__))
snakes_image_dir = snakes_script_dir + "\\DataFile\\Audio_Images\\"
snakes_image_list = snakes_script_dir + "\\DataFile\\ImageList.txt"
snakes_variable_list = snakes_script_dir + "\\DataFile\\VariableList.txt"

# Setting up the Pygame module
pygame.init()
width, height = 1100, 605
display = pygame.display.set_mode((width, height))
snakesImageData, snakesVariableData = ({},)*2
clock = pygame.time.Clock()
FPS = 100

# Calling Images and variables from lists within game-related folders (snakes_image_list)
class Bunch(object):
    def __init__(self, adict):
        self.__dict__.update(adict)

with open(snakes_image_list) as f:
    helpLines = 0
    lines = f.read().splitlines()
    for item in lines:
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
rank1Image, rank2Image, rank3Image, rank4Image = ("",)*4
tutorialPage, iter1 = (1,)*2
leaveBridge, bridgeHover, settingsHover, memoryHover, snakesHover, battleshipsHover, transition, loadingSequence = (False,)*8
chosenGame = ""

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
diceImg = ["dice_One", "dice_Two", "dice_Three", "dice_Four", "dice_Five", "dice_Six"]
winImages = ["red_Male", "green_Male", "blue_Male", "yellow_Male", "red_Female", "green_Female", "blue_Female", "yellow_Female", "white_Male", "black_Female"]

# Main function for the Snakes and Ladders game
def snakes_and_ladders():
    pygame.init()
    
    # Function to check for events within the pygame window (Essential to not crashing the window)
    def events():

        # The first part of the event.get() if statements are for the GUI hover effects
        for event in pygame.event.get():
            
            # Global variable declaration
            global rank1Pos, rank2Pos, rank3Pos, rank4Pos, posList, playerList, tutorialPage

            # Getting the x and y coordinates of the mouse pointer
            mouse_x, mouse_y = pygame.mouse.get_pos()

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
                        vars2.firstTime = True
                        pygame.quit(), sys.exit()

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

                    # Card Click, selection Events
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
        x = 0
        while True:
            events()

            # Allowing the background to move vertically in a seamless manner by duplication of image at centre point
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

            # Dictating the speed of movement (how many pixels left/right the background should move)
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
            if not vars2.gameInProgress and not vars2.gameInProgress2 and not vars2.firstTime:

                # Main menu function
                main_menu()
            elif vars2.gameInProgress:

                # Main game function (Multiplayer)
                main_game()
            elif vars2.gameInProgress2:

                # Main game function (Singleplayer)
                main_game2()
            elif vars2.firstTime:

                # Tutorial function for when the user starts the game for the first time
                tutorial()

            # Function to display options based on which button is pressed on the main menu e.g theme options
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

    # Main function for resetting the in-game buttons
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

        count = 0

        #Checks which player won and displays that specific player's image
        for i in range(1, 5):
            if eval("rank" + str(i) + "win"):
                    for color in clr2:
                        count += 1
                        if eval("rank" + str(i) + "Image") == color:
                            display.blit(vars.__dict__[winImages[count-1]], (618, 400))

    # This calls the main loop for the program
    main_screen()

# This calls the main function for the program to begin
snakes_and_ladders()
