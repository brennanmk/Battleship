class ship:
   def __init__(self, xLoc, yLoc):
      self.xLoc = xLoc
      self.yLoc = yLoc

   def getYLoc(self):
      return self.size

   def getYLoc(self):
      return self.size

   def setYLoc(self, xLoc):
      self.xLoc = xLoc

   def setYLoc(self, yLoc):
      self.yLoc = yLoc


class carrier(ship):
   def __init__(self, xLoc, yLoc):
      self.size = 5
      ship.__init__(xLoc, yLoc)
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class battleShip(ship):
   def __init__(self, xLoc, yLoc):
      self.size = 4
      ship.__init__(xLoc, yLoc)
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class cruiser(ship):
   def __init__(self, xLoc, yLoc):
      self.size = 3
      ship.__init__(xLoc, yLoc)
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class submarine(ship):
   def __init__(self, xLoc, yLoc):
      self.size = 3
      ship.__init__(xLoc, yLoc)
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size


class destroyer(ship):
   def __init__(self, xLoc, yLoc):
      self.size = 2
      ship.__init__(xLoc, yLoc)
   
   def getSize(self):
      return self.size

   def setSize(self, size):
      self.size = size