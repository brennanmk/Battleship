class ship:
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd

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
      ship.__init__(self.ShipRowStart, self.ShipCollumnStart, self.ShipRowEnd, self.ShipCollumnEnd)
   
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
      ship.__init__(RowStart, CollumnStart, RowEnd, CollumnEnd)
   
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
      ship.__init__(RowStart, CollumnStart, RowEnd, CollumnEnd)
   
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
      ship.__init__(ShipRowStart, ShipCollumnStart, ShipRowEnd, ShipCollumnEnd)
   
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
      ship.__init__(ShipRowStart, ShipCollumnStart, ShipRowEnd, ShipCollumnEnd)

   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size