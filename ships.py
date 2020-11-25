

class ship:
   def __init__(self, shipName):
      self.name = shipName
      self.Board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

   def printMap(self):
      print("\n-------------------------------------")
      for row in self.Board:
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

   def getName(self):
      return self.name

   def getSize(self):
      return self.size



class carrier(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip = False):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 5
      self.created = creatingShip
      ship.__init__(self, "Carrier")
   
   def setAll(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd

   def printLocation(self):
      print("  %s is at location (%s,%s) to (%s, %s)." %(getName(), self.ShipRowStart, self.ShipCollumnStart, self.ShipRowEnd, self.ShipCollumnEnd))

   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size
   
   def isCreated(self):
      return self.created


class battleShip(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip = False):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 4
      self.created = creatingShip
      ship.__init__(self, "BattleShip")
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size

   def isCreated(self):
      return self.created

class cruiser(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip = False):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 3
      self.created = creatingShip
      ship.__init__(self, "Cruiser")
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class submarine(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip = False):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 3
      self.created = creatingShip
      ship.__init__(self, "Submarine")
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class destroyer(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip = False):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 2
      self.created = creatingShip
      ship.__init__(self, "Destroyer")

   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size