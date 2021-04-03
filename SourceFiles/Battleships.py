"""
    Dear Reader: Comments are placed throughout the code. Some are explanations for certain sections of the code,
others are simply markers for enhanced readability.

Note: I understand that sections of large and repetitive chunks of code CAN be condensed using 'class' or/and 'for'
loops or/and lists. However, because of the limit of time, further condensation could perhaps be performed by future
programmers
"""

import pygame, sys

run_battleship = True  # Variable set in parent/bridge code when initiating the battleship sup-program

pygame.init()


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
            if pygame.sprite.collide_rect(Destroyer1_box, Grid_box) or pygame.sprite.collide_rect(Destroyer2_box, Grid_box):
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
            if pygame.sprite.collide_rect(Cruiser1_box, Grid_box) or pygame.sprite.collide_rect(Cruiser2_box, Grid_box):
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
            if pygame.sprite.collide_rect(Battleship1_box, Grid_box) or pygame.sprite.collide_rect(Battleship2_box, Grid_box):
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
            if pygame.sprite.collide_rect(Carrier1_box, Grid_box) or pygame.sprite.collide_rect(Carrier2_box, Grid_box):
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
            if not pygame.sprite.collide_rect(Submarine1_box, Destroyer1_box):  # Detects interceptions with other ships
                img_Tiles_1.blit(img_Submarine, (ship_x, ship_y))
                data_controller("placing_new_ship", "Submarine")
            else:
                print("nope")
        else:
            if not pygame.sprite.collide_rect(Submarine2_box, Destroyer2_box):  # Same purpose but for Player2's ships
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
        global rel_x, bg_x, stop_blit, event_test
        rel_x = bg_x % img_Title.get_rect().width
        display.blit(img_Title_Ship, (0, 10))
        display.blit(img_Title, (rel_x - img_Title.get_rect().width, 0))
        if rel_x < 2200:
            display.blit(img_Title, (rel_x, 0))
        bg_x -= 10
    if Title_battleship:
        display.blit(img_Title_Ship, (0, 0))
        display.blit(img_Title_Submarine, (0, 0))

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
    img_instructions_destroyer_destroyed = pygame.image.load('DataFile/Battleships_images/instruct_destroyer_destroyed.png')
    img_instructions_submarine_destroyed = pygame.image.load('DataFile/Battleships_images/instruct_submarine_destroyed.png')
    img_instructions_cruiser_destroyed = pygame.image.load('DataFile/Battleships_images/instruct_cruiser_destroyed.png')
    img_instructions_battleship_destroyed = pygame.image.load('DataFile/Battleships_images/instruct_battleship_destroyed.png')
    img_instructions_carrier_destroyed = pygame.image.load('DataFile/Battleships_images/instruct_carrier_destroyed.png')
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
                if Title_battleship:
                    if (758, 485) < pygame.mouse.get_pos() < (1058, 564):
                        Title_battleship = False
                        Placing_Battleships_1 = True
                else:
                    if (0, 45) < pygame.mouse.get_pos() < (59, 0):
                        main_battleship()


# ---------- Runs the functions from parent program ----------
if run_battleship:
    main_battleship()  # Once this line of code is run, battleship will run
else:
    # Goes back to parent/bridge code
    pass
