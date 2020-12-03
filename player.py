import ships
import bot

class player:  # player class creates a player with its own board and ship locations
    def __init__(self):  # blank constructor for player class
        # setup default board
        self.playerWon = False
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # player arsenal is used to keep track of which ships are created inside of the createShips method
        self.playerArsenal = []
        # add instances of each ship type into the player arsenal list
        self.playerArsenal.append(ships.carrier(0, 0, 0, 0))
        self.playerArsenal.append(ships.battleShip(0, 0, 0, 0))
        self.playerArsenal.append(ships.cruiser(0, 0, 0, 0))
        self.playerArsenal.append(ships.submarine(0, 0, 0, 0))
        self.playerArsenal.append(ships.destroyer(0, 0, 0, 0))

    def getPlayerWon(self):
        return self.playerWon

    # function to print the map visible to the enemy player (ship locations not included)
    def printEnemyMap(self):
        print("\n-----------------------------------------")
        for row in self.board:
            for collumns in row:
                if collumns == 1:
                    print("%s X" % ("|"), end=" ")
                elif collumns == 2:
                    print("%s !" % ("|"), end=" ")
                else:
                    print("%s  " % ("|"), end=" ")
            print("|")
            print("-----------------------------------------")

    # function to print the map visible to the enemy player (ship locations included)
    def printPlayerMap(self):
        print("\n-----------------------------------------")
        for row in self.board:
            for collumns in row:
                if collumns == 1:
                    print("%s X" % ("|"), end=" ")
                elif collumns == 2:
                    print("%s !" % ("|"), end=" ")
                elif collumns == 4:
                    print("%s -" % ("|"), end=" ")
                else:
                    print("%s  " % ("|"), end=" ")
            print("|")
            print("-----------------------------------------")

    def hit(self):  # function that enemy player calls to hit a posistion on the players board
        # ask enemy to enter a location to attack
        row = int(input("Enter Row To Hit: "))
        collumn = int(input("Enter Collumn To Hit: "))
        try:  # try catch to determine if the player strikes an out of bounds spot
            # check to see if the posistion hit is housing a ship
            if self.board[row][collumn] == 4:
                # set the board posistion to 2 if the enemy hit a ship
                self.board[row][collumn] = 2
                print("Enemy ship hit!")
            elif self.board[row][collumn] == 0:
                # set the board posistion to 1 if the enemy missed a ship
                self.board[row][collumn] = 1
                print("Missed enemy target!")
            else:  # make sure the player has not attacked the spot previously
                print("You already attacked this spot")
                self.hit()

        except Exception:
            print("Your value entered is out of bounds")
            self.hit()

    def botHit(self):  # function that enemy player calls to hit a posistion on the players board
        # ask enemy to enter a location to attack
        playerBot = bot.bot()
        row = playerBot.generateHit()["row"]
        collumn = bot.bot.generateHit()["collumn"]
        try:  # try catch to determine if the player strikes an out of bounds spot
            # check to see if the posistion hit is housing a ship
            if self.board[row][collumn] == 4:
                # set the board posistion to 2 if the enemy hit a ship
                self.board[row][collumn] = 2
                print("Enemy hit you ship")
            elif self.board[row][collumn] == 0:
                # set the board posistion to 1 if the enemy missed a ship
                self.board[row][collumn] = 1
                print("Enemy missed your ships!")
            else:  # make sure the player has not attacked the spot previously
                self.hit()

        except Exception:
            print("Your value entered is out of bounds")
            self.hit()

    def isSunk(self):
        shipSunk = 0

        for ship in self.playerArsenal:
            if not ship.getSunk():
                CollumnStart = ship.getStartColumn()
                CollumnEnd = ship.getEndColumn()
                RowStart = ship.getStartRow()
                RowEnd = ship.getEndRow()
                i = 0

                if (CollumnStart - CollumnEnd) == 0:
                    while self.board[RowStart + i][CollumnStart] == 2:
                        i += 1
                        if (RowStart + i) == RowEnd:
                            shipSunk += 1
                            ship.setSunk(True)
                            print(ship.getName() + " is sunk!")
                            break
                else:
                    while self.board[RowStart][CollumnStart + i] == 2:
                        i += 1
                        if (CollumnStart + i) == CollumnEnd:
                            print(ship.getName() + " is sunk!")
                            ship.setSunk(True)
                            shipSunk += 1
                            break

        if shipSunk == 5:
            print("You Lost!")  # if 5 ships have been sunk you lost!
            self.playerWon = True

    def createShip(self):  # function to populate the player board
        for ship in self.playerArsenal:  # for each ship in the player arsenal, prompt for a ship location and populate the ship on the map
            backupBoard = self.board
            try:  # try catch to reset the board incase the player enters overlapping ships
                self.printPlayerMap()
                if ship.isCreated() == False:
                    ship.setCreated()
                    ShipCollumnStart = int(
                        input("Enter Collumn For Start Position For %s: " % (ship.getName())))
                    ShipRowStart = int(
                        input("Enter Row For Start Posistion For %s : " % (ship.getName())))
                    shipOrientation = input(
                        "Enter Orientation for %s (up down left or right): " % (ship.getName()))
                    if shipOrientation.lower() == "up":  # check ship orientation, then populate the map based on the input
                        ShipRowEnd = ShipRowStart - ship.getSize()
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        while i > ShipRowEnd:
                            if self.board[i][ShipCollumnEnd] == 4:
                                raise Exception
                            else:
                                self.board[i][ShipCollumnEnd] = 4
                                i = i-1

                    elif shipOrientation.lower() == "down":
                        ShipRowEnd = ShipRowStart + ship.getSize()
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        while i < ShipRowEnd:
                            if self.board[i][ShipCollumnEnd] == 4:
                                raise Exception
                            else:
                                self.board[i][ShipCollumnEnd] = 4
                                i = i+1

                    elif shipOrientation.lower() == "left":
                        ShipRowEnd = ShipRowStart
                        ShipCollumnEnd = ShipCollumnStart - ship.getSize()
                        i = ShipCollumnStart
                        while i > ShipCollumnEnd:
                            if self.board[ShipRowEnd][i] == 4:
                                raise Exception
                            else:
                                self.board[ShipRowEnd][i] = 4
                                i = i-1

                    elif shipOrientation.lower() == "right":
                        ShipRowEnd = ShipRowStart
                        ShipCollumnEnd = ShipCollumnStart + ship.getSize()
                        i = ShipCollumnStart
                        while i < ShipCollumnEnd:
                            if self.board[ShipRowEnd][i] == 4:
                                raise Exception
                            else:
                                self.board[ShipRowEnd][i] = 4
                                i = i+1

                    else:  # for invalid ship orientation warn the player and then reset the function
                        print("Invalid Ship Location")
                        createShip()

                    # set ship location inside of ships.py
                    ship.setShipPos(ShipRowStart, ShipCollumnStart,
                                    ShipRowEnd, ShipCollumnEnd)
                    ship.printLocation()  # print ship location for user to see

                else:
                    continue
            except Exception:
                print("Invalid Ship Location, Please try again")
                self.board = backupBoard
                ship.setCreated()
                self.createShip()

    
    def botPopulateBoard(self):  # function to populate the bot board
        playerBot = bot.bot()
        for ship in self.playerArsenal:  # for each ship in the player arsenal, prompt for a ship location and populate the ship on the map
            backupBoard = self.board
            try:  # try catch to reset the board incase the player enters overlapping ships
                
                if ship.isCreated() == False:
                    
                    boardLoc = playerBot.generateBoard()
                    print(boardLoc["collumn"])
                    ShipCollumnStart = boardLoc["collumn"]
                    ShipRowStart = boardLoc["row"]
                    shipOrientation = boardLoc["orientation"]
                    if shipOrientation.lower() == "up":  # check ship orientation, then populate the map based on the input
                        ShipRowEnd = ShipRowStart - ship.getSize()
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        while i > ShipRowEnd:
                            if self.board[i][ShipCollumnEnd] == 4:
                                raise Exception
                            else:
                                self.board[i][ShipCollumnEnd] = 4
                                i = i-1
                                ship.setCreated()

                    elif shipOrientation.lower() == "down":
                        ShipRowEnd = ShipRowStart + ship.getSize()
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        while i < ShipRowEnd:
                            if self.board[i][ShipCollumnEnd] == 4:
                                raise Exception
                            else:
                                self.board[i][ShipCollumnEnd] = 4
                                i = i+1
                                ship.setCreated()

                    elif shipOrientation.lower() == "left":
                        ShipRowEnd = ShipRowStart
                        ShipCollumnEnd = ShipCollumnStart - ship.getSize()
                        i = ShipCollumnStart
                        while i > ShipCollumnEnd:
                            if self.board[ShipRowEnd][i] == 4:
                                raise Exception
                            else:
                                self.board[ShipRowEnd][i] = 4
                                i = i-1
                                ship.setCreated()

                    elif shipOrientation.lower() == "right":
                        ShipRowEnd = ShipRowStart
                        ShipCollumnEnd = ShipCollumnStart + ship.getSize()
                        i = ShipCollumnStart
                        while i < ShipCollumnEnd:
                            if self.board[ShipRowEnd][i] == 4:
                                raise Exception
                            else:
                                self.board[ShipRowEnd][i] = 4
                                i = i+1
                                ship.setCreated()

                    else:  # for invalid ship orientation warn the player and then reset the function
                        print("Invalid Ship Location")
                        boardLoc = playerBot.generateBoard()

                    # set ship location inside of ships.py
                    ship.setShipPos(ShipRowStart, ShipCollumnStart,
                                    ShipRowEnd, ShipCollumnEnd)
                    ship.printLocation()  # print ship location for user to see

                else:
                    continue
            except Exception:
                self.board = backupBoard
                boardLoc = playerBot.generateBoard()