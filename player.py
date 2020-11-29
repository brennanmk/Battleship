import ships

class player: #player class creates a player with its own board and ship locations
    def __init__(self): #blank constructor for player class
        #setup default board
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] 
        self.playerArsenal = [] #player arsenal is used to keep track of which ships are created inside of the createShips method
        self.playerArsenal.append(ships.carrier(0, 0, 0, 0)) #add instances of each ship type into the player arsenal list
        self.playerArsenal.append(ships.battleShip(0, 0, 0, 0))
        self.playerArsenal.append(ships.cruiser(0, 0, 0, 0))
        self.playerArsenal.append(ships.submarine(0, 0, 0, 0))
        self.playerArsenal.append(ships.destroyer(0, 0, 0, 0))

    def printEnemyMap(self): #function to print the map visible to the enemy player (ship locations not included)
        print("\n-------------------------------------")
        for row in self.board:
            for collumns in row:
                if collumns == 1:
                    print("%s X" % ("|"), end=" ")
                elif collumns == 2:
                    print("%s !" % ("|"), end=" ")
                else:
                    print("%s  " % ("|"), end=" ")
            print("\n-------------------------------------")

    def printPlayerMap(self): #function to print the map visible to the enemy player (ship locations included)
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

    def hit(self): #function that enemy player calls to hit a posistion on the players board
        row = input("Enter Row To Hit: ") #ask enemy to enter a location to attack
        collumn = input("Enter Collumn To Hit: ")
        try: #try catch to determine if the player strikes an out of bounds spot
            if [row][collumn] == 4: #check to see if the posistion hit is housing a ship
                Board[row][collumn] = 2 #set the board posistion to 2 if the enemy hit a ship
            elif [row][collumn] == 0: 
                Board[row][collumn] = 1 #set the board posistion to 1 if the enemy missed a ship
            else: #make sure the player has not attacked the spot previously
                print("You already attacked this spot")
                hit()

        except Exception:
            print("Your value entered is out of bounds")
            hit()

    def createShip(self): #function to populate the player board
        try: #try catch to reset the board incase the player enters overlapping ships
            for ship in self.playerArsenal: #for each ship in the player arsenal, prompt for a ship location and populate the ship on the map
                self.printPlayerMap()
                if ship.isCreated() == False:
                    ShipCollumnStart = int(
                        input("Enter Collumn For Start Position For %s: " % (ship.getName())))
                    ShipRowStart = int(
                        input("Enter Row For Start Posistion For %s : " % (ship.getName())))
                    shipOrientation = input(
                        "Enter Orientation for %s (up down left or right): " % (ship.getName()))
                    if shipOrientation.lower() == "up": #check ship orientation, then populate the map based on the input
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

                    else: #for invalid ship orientation warn the player and then reset the function
                        print("Invalid Ship Location")
                        createShip()

                    # set ship location inside of ships.py
                    ship.setShipPos(ShipRowStart, ShipCollumnStart,
                                    ShipRowEnd, ShipCollumnEnd)
                    ship.printLocation()  # print ship location for user to see

                else:
                    continue
        except Exception:
            print("Invalid Ship Location")
            self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            self.createShip()
