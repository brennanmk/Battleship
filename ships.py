class ship:
   def __init__(self, shipName):
      self.name = shipName

class carrier(ship):
   def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip = False):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd
      self.size = 5
      self.created = creatingShip
      ship.__init__(self, "Carrier")
   

   def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd


   def printLocation(self):
      print("  %s is at location (%s,%s) to (%s, %s)." % (self.name, self.ShipRowStart, self.ShipCollumnStart, self.ShipRowEnd, self.ShipCollumnEnd))

   
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

   def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd

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
   
   def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd

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
   

   def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd

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

   def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd):
      self.ShipRowStart = RowStart
      self.ShipCollumnStart = CollumnStart
      self.ShipRowEnd = RowEnd
      self.ShipCollumnEnd = CollumnEnd


   def getSize(self):
      return self.size


   def setSize(self, size):
      self.size = size
