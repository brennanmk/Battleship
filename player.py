import ships
import bot


class player:  # player class creates a player with its own board and ship locations, Written by Hank Pham & Brennan Miller-Klugman
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

    def getPlayerWon(self): #Written by Hank Pham & Brennan Miller-Klugman
        return self.playerWon

    # function to print the map visible to the enemy player (ship locations not included)
    def printEnemyMap(self): #Written by Brennan Miller-Klugman
        print("\n  0   1   2   3   4   5   6   7   8   9")
        print("-----------------------------------------")
        counter = 0

        for row in self.board:
            for columns in row:
                if columns == 1:
                    print("%s X" % ("|"), end=" ")
                elif columns == 2:
                    print("%s !" % ("|"), end=" ")
                else:
                    print("%s  " % ("|"), end=" ")
            print("| %s" % counter)
            print("-----------------------------------------")
            counter += 1

    # function to print the map visible to the enemy player (ship locations included)
    def printPlayerMap(self): #Written by Brennan Miller-Klugman
        print("\n  0   1   2   3   4   5   6   7   8   9")
        print("-----------------------------------------")
        counter = 0
        for row in self.board:
            for columns in row:
                if columns == 1:
                    print("%s X" % ("|"), end=" ")
                elif columns == 2:
                    print("%s !" % ("|"), end=" ")
                elif columns == 4:
                    print("%s -" % ("|"), end=" ")
                else:
                    print("%s  " % ("|"), end=" ")
            print("| %s" % counter)
            print("-----------------------------------------")
            counter += 1

    def hit(self):  # function that enemy player calls to hit a posistion on the players board, Written by Hank Pham & Brennan Miller-Klugman
        # ask enemy to enter a location to attack
        row = int(input("Enter Row To Hit: "))
        column = int(input("Enter column To Hit: "))
        try:  # try catch to determine if the player strikes an out of bounds spot
            # check to see if the posistion hit is housing a ship
            if self.board[row][column] == 4:
                # set the board posistion to 2 if the enemy hit a ship
                self.board[row][column] = 2
                print("Enemy ship hit!")
            elif self.board[row][column] == 0:
                # set the board posistion to 1 if the enemy missed a ship
                self.board[row][column] = 1
                print("Missed enemy target!")
            else:  # make sure the player has not attacked the spot previously
                print("You already attacked this spot")
                self.hit()
            
            if(self.isSunk()):
                print("You sunk a ship!")

        except Exception:
            print("Your value entered is out of bounds")
            self.hit()

    def botHit(self):  # function that enemy player calls to hit a posistion on the players board, Written by Hank Pham & Brennan Miller-Klugman
        # ask enemy to enter a location to attack
        hit = self.hitBot.generateHit()
        row = hit["row"]
        column = hit["column"]
        try:  # try catch to determine if the player strikes an out of bounds spot
            # check to see if the posistion hit is housing a ship
            if self.board[row][column] == 4:
                # set the board posistion to 2 if the enemy hit a ship
                self.board[row][column] = 2
                self.isSunk()
                if(self.hitBot.getHit() == False):
                    self.hitBot.setHit(row, column)
            elif self.board[row][column] == 0:
                # set the board posistion to 1 if the enemy missed a ship
                self.board[row][column] = 1
            else:  # make sure the player has not attacked the spot previously
                self.botHit()

        except Exception:
            self.botHit()

    def isSunk(self): #Written by Hank Pham
        for ship in self.playerArsenal:
            if ship.getSunk() == False:
                columnStart = ship.getStartColumn()
                columnEnd = ship.getEndColumn()
                RowStart = ship.getStartRow()
                RowEnd = ship.getEndRow()
                i = 0

                if columnStart == columnEnd:
                    while self.board[RowStart + i][columnStart] == 2 or self.board[RowStart - i][columnStart] == 2:
                        i = i + 1
                        if i == ship.getSize():
                            self.shipSunk += 1
                            ship.setSunk(True)
                            if self.shipSunk == 5:
                                print("%s Won!" % (self.playerName))  # if 5 ships have been sunk you lost!
                                self.playerWon = True
                            return True

                else:
                    while self.board[RowStart][columnStart + i] == 2 or self.board[RowStart][columnStart - i] == 2:
                        i = i + 1
                        if i == ship.getSize():
                            ship.setSunk(True)
                            self.shipSunk += 1
                            if self.shipSunk == 5:
                                print("%s Won!" % (self.playerName))  # if 5 ships have been sunk you lost!
                                self.playerWon = True              
                            return True
                        

        return False

    def createShip(self):  # function to populate the player board, Written by Hank Pham, and Brennan Miller-Klugman
        for ship in self.playerArsenal:  # for each ship in the player arsenal, prompt for a ship location and populate the ship on the map
            backupBoard = self.board
            try:  # try catch to reset the board incase the player enters overlapping ships
                if ship.isCreated() == False:
                    self.printPlayerMap()
                    ship.setCreated()
                    ShipcolumnStart = int(
                        input("Enter column For Start Position For %s: " % (ship.getName())))
                    ShipRowStart = int(
                        input("Enter Row For Start Posistion For %s : " % (ship.getName())))
                    shipOrientation = input(
                        "Enter Orientation for %s (up down left or right): " % (ship.getName()))

                    if shipOrientation.lower() == "up":  # check ship orientation, then populate the map based on the input
                        ShipRowEnd = ShipRowStart - ship.getSize()
                        if ShipRowEnd < 0:
                            raise Exception
                        ShipcolumnEnd = ShipcolumnStart
                        i = ShipRowStart
                        k = i
                        while k > ShipRowEnd:
                            if self.board[k][ShipcolumnEnd] == 4:
                                raise Exception
                            k -= 1
                        while i > ShipRowEnd:
                            self.board[i][ShipcolumnEnd] = 4
                            i = i-1

                    elif shipOrientation.lower() == "down":
                        ShipRowEnd = ShipRowStart + ship.getSize()
                        if ShipRowEnd > 9:
                            raise Exception
                        ShipcolumnEnd = ShipcolumnStart
                        i = ShipRowStart
                        k = i
                        while k < ShipRowEnd:
                            if self.board[k][ShipcolumnEnd] == 4:
                                raise Exception
                            k += 1
                        while i < ShipRowEnd:
                            self.board[i][ShipcolumnEnd] = 4
                            i = i+1

                    elif shipOrientation.lower() == "left":
                        ShipcolumnEnd = ShipcolumnStart - ship.getSize()
                        if ShipcolumnEnd < 0:
                            raise Exception
                        ShipRowEnd = ShipRowStart
                        i = ShipcolumnStart
                        k = i
                        while k > ShipcolumnEnd:
                            if self.board[ShipRowEnd][k] == 4:
                                raise Exception
                            k -= 1
                        while i > ShipcolumnEnd:
                            self.board[ShipRowEnd][i] = 4
                            i = i-1

                    elif shipOrientation.lower() == "right":
                        ShipcolumnEnd = ShipcolumnStart + ship.getSize()
                        if ShipcolumnEnd > 9:
                            raise Exception
                        ShipRowEnd = ShipRowStart
                        i = ShipcolumnStart
                        k = i
                        while k < ShipcolumnEnd:
                            if self.board[ShipRowEnd][k] == 4:
                                raise Exception
                            k += 1
                        while i < ShipcolumnEnd:
                            self.board[ShipRowEnd][i] = 4
                            i = i+1

                    else:  # for invalid ship orientation warn the player and then reset the function
                        print("Invalid Ship Location")
                        self.createShip()

                    # set ship location inside of ships.py
                    ship.setShipPos(ShipRowStart, ShipcolumnStart,
                                    ShipRowEnd, ShipcolumnEnd)
                    ship.printLocation()  # print ship location for user to see

                else:
                    continue
            except Exception:
                print("Invalid Ship Location, Please try again")
                self.board = backupBoard
                ship.setCreated()
                self.createShip()

    def botPopulateBoard(self):  # function to populate the bot board, Written by Hank Pham, and Brennan Miller-Klugman
        playerBot = bot.bot()
        for ship in self.playerArsenal:  # for each ship in the player arsenal, prompt for a ship location and populate the ship on the map
            backupBoard = self.board
            try:  # try catch to reset the board incase the player enters overlapping ships
                if ship.isCreated() == False:
                    ship.setCreated()
                    # Return a dictonary that consists of "column", "row", and "orientation"
                    boardLoc = playerBot.generateBoard()
                    ShipcolumnStart = boardLoc["column"]
                    ShipRowStart = boardLoc["row"]
                    shipOrientation = boardLoc["orientation"]

                    if shipOrientation.lower() == "up":  # check ship orientation, then populate the map based on the input
                        ShipRowEnd = ShipRowStart - ship.getSize()
                        if ShipRowEnd < 0:
                            raise Exception
                        ShipcolumnEnd = ShipcolumnStart
                        i = ShipRowStart
                        k = i
                        while k > ShipRowEnd:
                            if self.board[k][ShipcolumnEnd] == 4:
                                raise Exception
                            k -= 1
                        while i > ShipRowEnd:
                            self.board[i][ShipcolumnEnd] = 4
                            i = i-1

                    elif shipOrientation.lower() == "down":
                        ShipRowEnd = ShipRowStart + ship.getSize()
                        if ShipRowEnd > 9:
                            raise Exception
                        ShipcolumnEnd = ShipcolumnStart
                        i = ShipRowStart
                        k = i
                        while k < ShipRowEnd:
                            if self.board[k][ShipcolumnEnd] == 4:
                                raise Exception
                            k += 1
                        while i < ShipRowEnd:
                            self.board[i][ShipcolumnEnd] = 4
                            i = i+1

                    elif shipOrientation.lower() == "left":
                        ShipcolumnEnd = ShipcolumnStart - ship.getSize()
                        if ShipcolumnEnd < 0:
                            raise Exception
                        ShipRowEnd = ShipRowStart
                        i = ShipcolumnStart
                        k = i
                        while k > ShipcolumnEnd:
                            if self.board[ShipRowEnd][k] == 4:
                                raise Exception
                            k -= 1
                        while i > ShipcolumnEnd:
                            self.board[ShipRowEnd][i] = 4
                            i = i-1

                    elif shipOrientation.lower() == "right":
                        ShipcolumnEnd = ShipcolumnStart + ship.getSize()
                        if ShipcolumnEnd > 9:
                            raise Exception
                        ShipRowEnd = ShipRowStart
                        i = ShipcolumnStart
                        k = i
                        while k < ShipcolumnEnd:
                            if self.board[ShipRowEnd][k] == 4:
                                raise Exception
                            k += 1
                        while i < ShipcolumnEnd:
                            self.board[ShipRowEnd][i] = 4
                            i = i+1

                    else:  # for invalid ship orientation warn the player and then reset the function
                        print("Invalid Ship Location")
                        self.botPopulateBoard()

                    # set ship location inside of ships.py
                    ship.setShipPos(ShipRowStart, ShipcolumnStart,
                                    ShipRowEnd, ShipcolumnEnd)
                    ship.printLocation()  # print ship location for user to see

                else:
                    continue
            except Exception:
                self.board = backupBoard
                ship.setCreated()
                self.botPopulateBoard()
