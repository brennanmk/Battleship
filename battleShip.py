import ships as bs

ships = [{'Type': 'carrier', 'Size': 5, 'Created': False}, {'Type': 'battleShip', 'Size': 4, 'Created': False}, {'Type': 'cruiser', 'Size': 3, 'Created': False}, {'Type': 'submarine', 'Size': 3, 'Created': False}, {'Type': 'destroyer', 'Size': 2, 'Created': False}]

def createShips(player):
   try:
      for ship in ships: 
         if ship["Created"] == False:
            ShipRowStart = int(input("Enter Row For Start Posistion For %s: " % (ship["Type"])))
            ShipCollumnStart = int(input("Enter Collumn For Start Position For %s: " % (ship["Type"])))
            shipOrientation = input("Enter Orientation for %s (up down left or right): " % (ship["Type"]))
            if shipOrientation.lower() == "up":
               ShipRowEnd = ShipRowStart + ship["Size"]
               ShipCollumnEnd = ShipCollumnStart
            elif shipOrientation.lower() == "down":
               ShipRowEnd = ShipRowStart - ship["Size"]
               ShipCollumnEnd = ShipCollumnStart
            elif shipOrientation.lower() == "left":
               ShipRowEnd = ShipRowStart
               ShipCollumnEnd = ShipCollumnStart - ship["Size"]
            elif shipOrientation.lower() == "right":
               ShipRowEnd = ShipRowStart
               ShipCollumnEnd = ShipCollumnStart + ship["Size"]
            else:
               print("Invalid Ship Location")
               createShips(player)

            commandName = "player.%s(ShipRowStart, ShipCollumnStart, ShipRowEnd, ShipCollumnEnd)" % (ship["Type"]) 
            exec(commandName)
         else:
            continue
   except Exception:
      print("Invalid Ship Location")
      createShips(player)

def turn():
   printMap()
   xLoc = input("Enter Collumn Location: ")
   yLoc = input("Enter Row Location: ")

def main():
   player1 = bs.ship()
   player1.printMap()
   player1.Board = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
   player1.printMap()
   player1.battleShip(0,0,0,0)

   createShips(player1)

if __name__=="__main__":
   main()