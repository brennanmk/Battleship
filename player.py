import ships
import bot


class player:  # player class creates a player with its own board and ship locations
    def __init__(self, name):  # blank constructor for player class
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
        self.hitBot = bot.bot()
        self.shipSunk = 0
        self.playerName = name

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
            
            if(self.isSunk()):
                print("You sunk a ship!")

        except Exception:
            print("Your value entered is out of bounds")
            self.hit()

    def botHit(self):  # function that enemy player calls to hit a posistion on the players board
        # ask enemy to enter a location to attack
        hit = self.hitBot.generateHit()
        row = hit["row"]
        collumn = hit["collumn"]
        try:  # try catch to determine if the player strikes an out of bounds spot
            # check to see if the posistion hit is housing a ship
            if self.board[row][collumn] == 4:
                # set the board posistion to 2 if the enemy hit a ship
                self.board[row][collumn] = 2
                self.isSunk()
                if(self.hitBot.getHit() == False):
                    self.hitBot.setHit(row, collumn)
            elif self.board[row][collumn] == 0:
                # set the board posistion to 1 if the enemy missed a ship
                self.board[row][collumn] = 1
            else:  # make sure the player has not attacked the spot previously
                self.botHit()

        except Exception:
            self.botHit()

    def isSunk(self):
        for ship in self.playerArsenal:
            if ship.getSunk() == False:
                CollumnStart = ship.getStartColumn()
                CollumnEnd = ship.getEndColumn()
                RowStart = ship.getStartRow()
                RowEnd = ship.getEndRow()
                i = 0

                if CollumnStart == CollumnEnd:
                    while self.board[RowStart + i][CollumnStart] == 2 or self.board[RowStart - i][CollumnStart] == 2:
                        i = i + 1
                        if i == ship.getSize():
                            self.shipSunk += 1
                            ship.setSunk(True)
                            if self.shipSunk == 5:
                                print("%s Won!" % (self.playerName))  # if 5 ships have been sunk you lost!
                                self.playerWon = True
                            return True

                else:
                    while self.board[RowStart][CollumnStart + i] == 2 or self.board[RowStart][CollumnStart - i] == 2:
                        i = i + 1
                        if i == ship.getSize():
                            ship.setSunk(True)
                            self.shipSunk += 1
                            if self.shipSunk == 5:
                                print("%s Won!" % (self.playerName))  # if 5 ships have been sunk you lost!
                                self.playerWon = True              
                            return True
                        

        return False



    def createShip(self):  # function to populate the player board
        for ship in self.playerArsenal:  # for each ship in the player arsenal, prompt for a ship location and populate the ship on the map
            backupBoard = self.board
            try:  # try catch to reset the board incase the player enters overlapping ships
                if ship.isCreated() == False:
                    self.printPlayerMap()
                    ship.setCreated()
                    ShipCollumnStart = int(
                        input("Enter Collumn For Start Position For %s: " % (ship.getName())))
                    ShipRowStart = int(
                        input("Enter Row For Start Posistion For %s : " % (ship.getName())))
                    shipOrientation = input(
                        "Enter Orientation for %s (up down left or right): " % (ship.getName()))

                    if shipOrientation.lower() == "up":  # check ship orientation, then populate the map based on the input
                        ShipRowEnd = ShipRowStart - ship.getSize()
                        if ShipRowEnd < 0:
                            raise Exception
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        k = i
                        while k > ShipRowEnd:
                            if self.board[k][ShipCollumnEnd] == 4:
                                raise Exception
                            k += 1
                        while i > ShipRowEnd:
                            self.board[i][ShipCollumnEnd] = 4
                            i = i-1

                    elif shipOrientation.lower() == "down":
                        ShipRowEnd = ShipRowStart + ship.getSize()
                        if ShipRowEnd > 9:
                            raise Exception
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        k = i
                        while k < ShipRowEnd:
                            if self.board[k][ShipCollumnEnd] == 4:
                                raise Exception
                            k += 1
                        while i < ShipRowEnd:
                            self.board[i][ShipCollumnEnd] = 4
                            i = i+1

                    elif shipOrientation.lower() == "left":
                        ShipCollumnEnd = ShipCollumnStart - ship.getSize()
                        if ShipCollumnEnd < 0:
                            raise Exception
                        ShipRowEnd = ShipRowStart
                        i = ShipCollumnStart
                        k = i
                        while k > ShipCollumnEnd:
                            if self.board[ShipRowEnd][k] == 4:
                                raise Exception
                            k += 1
                        while i > ShipCollumnEnd:
                            self.board[ShipRowEnd][i] = 4
                            i = i-1

                    elif shipOrientation.lower() == "right":
                        ShipCollumnEnd = ShipCollumnStart + ship.getSize()
                        if ShipCollumnEnd > 9:
                            raise Exception
                        ShipRowEnd = ShipRowStart
                        i = ShipCollumnStart
                        k = i
                        while k < ShipCollumnEnd:
                            if self.board[ShipRowEnd][k] == 4:
                                raise Exception
                            k += 1
                        while i < ShipCollumnEnd:
                            self.board[ShipRowEnd][i] = 4
                            i = i+1

                    else:  # for invalid ship orientation warn the player and then reset the function
                        print("Invalid Ship Location")
                        self.createShip()

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
                    ship.setCreated()
                    # Return a dictonary that consists of "column", "row", and "orientation"
                    boardLoc = playerBot.generateBoard()
                    ShipCollumnStart = boardLoc["collumn"]
                    ShipRowStart = boardLoc["row"]
                    shipOrientation = boardLoc["orientation"]

                    if shipOrientation.lower() == "up":  # check ship orientation, then populate the map based on the input
                        ShipRowEnd = ShipRowStart - ship.getSize()
                        if ShipRowEnd < 0:
                            raise Exception
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        k = i
                        while k > ShipRowEnd:
                            if self.board[k][ShipCollumnEnd] == 4:
                                raise Exception
                            k += 1
                        while i > ShipRowEnd:
                            self.board[i][ShipCollumnEnd] = 4
                            i = i-1

                    elif shipOrientation.lower() == "down":
                        ShipRowEnd = ShipRowStart + ship.getSize()
                        if ShipRowEnd > 9:
                            raise Exception
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        k = i
                        while k < ShipRowEnd:
                            if self.board[k][ShipCollumnEnd] == 4:
                                raise Exception
                            k += 1
                        while i < ShipRowEnd:
                            self.board[i][ShipCollumnEnd] = 4
                            i = i+1

                    elif shipOrientation.lower() == "left":
                        ShipCollumnEnd = ShipCollumnStart - ship.getSize()
                        if ShipCollumnEnd < 0:
                            raise Exception
                        ShipRowEnd = ShipRowStart
                        i = ShipCollumnStart
                        k = i
                        while k > ShipCollumnEnd:
                            if self.board[ShipRowEnd][k] == 4:
                                raise Exception
                            k += 1
                        while i > ShipCollumnEnd:
                            self.board[ShipRowEnd][i] = 4
                            i = i-1

                    elif shipOrientation.lower() == "right":
                        ShipCollumnEnd = ShipCollumnStart + ship.getSize()
                        if ShipCollumnEnd > 9:
                            raise Exception
                        ShipRowEnd = ShipRowStart
                        i = ShipCollumnStart
                        k = i
                        while k < ShipCollumnEnd:
                            if self.board[ShipRowEnd][k] == 4:
                                raise Exception
                            k += 1
                        while i < ShipCollumnEnd:
                            self.board[ShipRowEnd][i] = 4
                            i = i+1

                    else:  # for invalid ship orientation warn the player and then reset the function
                        print("Invalid Ship Location")
                        self.botPopulateBoard()

                    # set ship location inside of ships.py
                    ship.setShipPos(ShipRowStart, ShipCollumnStart,
                                    ShipRowEnd, ShipCollumnEnd)
                    ship.printLocation()  # print ship location for user to see

                else:
                    continue
            except Exception:
                self.board = backupBoard
                ship.setCreated()
                self.botPopulateBoard()
