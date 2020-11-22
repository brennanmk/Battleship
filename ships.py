class ship:
   def __init__(self):
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

 

   def getYLoc(self):
      return self.size

   def getYLoc(self):
      return self.size

   def setYLoc(self, xLoc):
      self.xLoc = xLoc

   def setYLoc(self, yLoc):
      self.yLoc = yLoc


class carrier(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 5
      ship.__init__(self)
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class battleShip(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 4
      ship.__init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd)
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class cruiser(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 3
      ship.__init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd)
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class submarine(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 3
      ship.__init__(self, ShipRowStart, ShipCollumnStart, ShipRowEnd, ShipCollumnEnd)
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class destroyer(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 2
      ship.__init__(self, ShipRowStart, ShipCollumnStart, ShipRowEnd, ShipCollumnEnd)

   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size