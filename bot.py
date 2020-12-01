from random import randint

class bot: #parent ship function
   def __init__(self):
      random()

   def generateBoard(self):
      row = randint(0, 9)
      collumn = randint(0, 9)
      orientationValue = randint(0,3)
      orentations = ["up", "down", "left", "right"]
      shipLoc = {"row" : row, "collumn" : collumn, "orientation": orentations[orientationValue]}
      return shipLoc

   def generateHit(self):
      row = randint(0, 9)
      collumn = randint(0, 9)
      hit = {"row" : row, "collumn" : collumn}
      return hit