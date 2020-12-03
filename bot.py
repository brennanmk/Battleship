from random import randint

class bot: #parent ship function
   def __init__(self):
      self.test = 2

   def generateBoard(self, shipSize):
      orentations = []
      row = randint(0, 9)
      collumn = randint(0, 9)


      if(row+shipSize < 9 and row-shipSize > shipSize):
         if(collumn-shipSize < 0):
            orentations.append("right")
            orentations.append("up")
         elif(collumn+shipSize > 9):
            orentations.append("left")
            orentations.append("up")
      elif(row-shipSize > 0):
         if(collumn-shipSize < 0):
            orentations.append("right")
            orentations.append("down")
         elif(collumn+shipSize > 9):
            orentations.append("left")
            orentations.append("down")
      else:
         self.generateBoard

      orientationValue = randint(0,len(orentations))
      shipLoc = {"row" : row, "collumn" : collumn, "orientation": orentations[orientationValue]}
      print(shipLoc)
      return shipLoc

   def generateHit(self):
      row = randint(0, 9)
      collumn = randint(0, 9)
      hit = {"row" : row, "collumn" : collumn}
      return hit