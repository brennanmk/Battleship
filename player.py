import ships

class player:
    def chooseSide(self):
        side = input("Choose your side of the board: Left or Right?")
        side = side.lower()
        if side != "left" or side != 'right':
            print("Please only enter Left or Right.")
            chooseSide()
    
    def createShip(self):
        try:
            for ship in self.playerArsenal:
                if ship.isCreated() == False:
                    ShipRowStart = int(input("Enter Row For Start Posistion For %s: " % (ship.getName())))
                    ShipCollumnStart = int(input("Enter Collumn For Start Position For %s: " % (ship.getName())))
                    shipOrientation = input("Enter Orientation for %s (up down left or right): " % (ship.getName()))
                    if shipOrientation.lower() == "up":
                        ShipRowEnd = ShipRowStart + ship.getSize()
                        ShipCollumnEnd = ShipCollumnStart
                    elif shipOrientation.lower() == "down":
                        ShipRowEnd = ShipRowStart - ship.getSize()
                        ShipCollumnEnd = ShipCollumnStart
                    elif shipOrientation.lower() == "left":
                        ShipRowEnd = ShipRowStart
                        ShipCollumnEnd = ShipCollumnStart - ship.getSize()
                    elif shipOrientation.lower() == "right":
                        ShipRowEnd = ShipRowStart
                        ShipCollumnEnd = ShipCollumnStart + ship.getSize()
                    else:
                        print("Invalid Ship Location")    
                        createShip()

                    ship.setAll(ShipRowStart, ShipCollumnStart, ShipRowEnd, ShipCollumnEnd)   
                    # ship.printLocation()

                    # Check function here
                else:
                    continue
        except Exception:
            print("Invalid Ship Location")
            self.createShip()   

    def __init__(self):
        self.side = None     #Left or right side.
        self.playerArsenal  = []
        self.playerArsenal.append(ships.carrier(0,0,0,0))
        self.playerArsenal.append(ships.battleShip(0,0,0,0))
        self.playerArsenal.append(ships.cruiser(0,0,0,0))
        self.playerArsenal.append(ships.submarine(0,0,0,0))
        self.playerArsenal.append(ships.destroyer(0,0,0,0))
        self.createShip()

