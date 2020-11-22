import ships as bs

Board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

ships = [{'Type': 'carrier', 'Size': 5, 'Created': False}, {'Type': 'battleShip', 'Size': 4, 'Created': False}, {'Type': 'cruiser', 'Size': 3, 'Created': False}, {'Type': 'submarine', 'Size': 3, 'Created': False}, {'Type': 'destroyer', 'Size': 2, 'Created': False}]

def printMap():
   print("\n-------------------------------------")
   for row in Board:
      for collumns in row:
         if collumns == 1:
            print("%s X" % ("|"), end = " ")
         elif collumns == 2:
            print("%s !" % ("|"), end = " ")
         else:
            print("%s  " % ("|"), end = " ")
      print("\n-------------------------------------")

def hit():
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

def createShips(player):
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


def turn():
   printMap()
   xLoc = input("Enter Collumn Location: ")
   yLoc = input("Enter Row Location: ")

def main():
   player1 = bs
   player2 = bs
   printMap()
   player1.carrier(1,2,3,4)
   createShips(player1)

if __name__=="__main__":
   main()