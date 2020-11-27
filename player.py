import ships

class player:       
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.playerArsenal  = []
        self.playerArsenal.append(ships.carrier(0,0,0,0))
        self.playerArsenal.append(ships.battleShip(0,0,0,0))
        self.playerArsenal.append(ships.cruiser(0,0,0,0))
        self.playerArsenal.append(ships.submarine(0,0,0,0))
        self.playerArsenal.append(ships.destroyer(0,0,0,0))

    def printMap(self):
      print("\n-------------------------------------")
      for row in self.board:
         for collumns in row:
            if collumns == 1:
               print("%s X" % ("|"), end = " ")
            elif collumns == 2:
               print("%s !" % ("|"), end = " ")
            else:
               print("%s  " % ("|"), end = " ")
         print("\n-------------------------------------")


    def hit(self):
      row = input("Enter Row To Hit: ")
      collumn = input("Enter Collumn To Hit: ")
      try:
         if [row][collumn] == 4:
            Board[row][collumn] = 2
         elif [row][collumn] == 0: 
            Board[row][collumn] = 1
         else:
            print("You already attacked this spot")
            hit() 

      except Exception:
         print("Your value entered is out of bounds")
         hit()
             

    def createShip(self):
        try:
            for ship in self.playerArsenal:
                if ship.isCreated() == Fase:
                    ShipRowStart = int(input("Enter Row For Start Posistion For %s: " % (ship.getName())))
                    ShipCollumnStart = int(input("Enter Collumn For Start Position For %s: " % (ship.getName())))
                    shipOrientation = input("Enter Orientation for %s (up down left or right): " % (ship.getName()))
                    if shipOrientation.lower() == "up":
                        ShipRowEnd = ShipRowStart + ship.getSize()
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        while i < ShipRowEnd:
                            self.board[i][ShipCollumnEnd] = 4
                            i+1

                    elif shipOrientation.lower() == "down":
                        ShipRowEnd = ShipRowStart - ship.getSize()
                        ShipCollumnEnd = ShipCollumnStart
                        i = ShipRowStart
                        while i > ShipRowEnd:
                            self.board[i][ShipCollumnEnd] = 4
                            i-1

                    elif shipOrientation.lower() == "left":
                        ShipRowEnd = ShipRowStart
                        ShipCollumnEnd = ShipCollumnStart - ship.getSize()
                        i = ShipCollumnStart
                        while i > ShipCollumnStart:
                            self.board[ShipRowEnd][i] = 4
                            i-1

                    elif shipOrientation.lower() == "right":
                        ShipRowEnd = ShipRowStart
                        ShipCollumnEnd = ShipCollumnStart + ship.getSize()
                        i = ShipCollumnStart
                        while i < ShipRowEnd:
                            self.board[ShipRowEnd][i] = 4
                            i+1

                    else:
                        print("Invalid Ship Location")    
                        createShip()

                    ship.setShip(ShipRowStart, ShipCollumnStart, ShipRowEnd, ShipCollumnEnd)   #set ship location inside of ships.py
                    ship.printLocation() #print ship location for user to see

                else:
                    continue
        except Exception:
            print("Invalid Ship Location")
            self.createShip()