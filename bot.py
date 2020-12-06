import random 

class bot: #parent ship function
   def __init__(self):
      self.lastHitRow = -1
      self.lastHitCollumn = -1
      self.hitDirection = "down"

   def setLastHit(self, collumn, row, isSunk):
      self.lastHitRow = row
      self.lastHitCollumn = collumn

      if isSunk == True:
         self.lastHitRow = -1
         self.lastHitCollumn = -1


   def setNextHitDirection(self):
      orentations = ["up", "down", "left", "right"]
      for index, orientation in enumerate(orentations):
         if orientation == self.hitDirection:
            if index == 3:
               self.hitDirection = orentations[0]
               break
            else:
               self.hitDirection = orentations[index + 1]
               break

   def generateBoard(self):
      RowA = 0
      RowB =0
      CollumnA = 0
      CollumnB = 0
      orentations = ["up", "down", "left", "right"]

      i = random.randint(1,5) # Randomly choosing between 5 region
      
      # 3x4 top left region
      if i == 1:
         RowA = 0
         RowB = 2
         CollumnA = 0
         CollumnB = 3
         choice = [1,2]
         orientationValue = random.choice(choice)

      # 3x4 bottom left region
      elif i == 2:
         RowA = 7
         RowB = 9
         CollumnA = 0
         CollumnB = 3
         choice = [0,2]
         orientationValue = random.choice(choice)

      # 3x4 top right region
      elif i == 3:
         RowA = 0
         RowB = 2
         CollumnA = 6
         CollumnB = 9
         choice = [1,3]
         orientationValue = random.choice(choice)

      # 3x4 bottom right region
      elif i == 4:
         RowA = 7
         RowB = 9
         CollumnA = 6
         CollumnB = 9
         choice = [0, 3]
         orientationValue = random.choice(choice)

      # 6x6 middle region
      else:
         RowA = 2
         RowB = 7
         CollumnA = 2
         CollumnB = 7
         orientationValue = random.randint(0,3)

      row = random.randint(RowA, RowB)
      collumn = random.randint(CollumnA, CollumnB)

      shipLoc = {"row" : row, "collumn" : collumn, "orientation": orentations[orientationValue]}
      

      return shipLoc

   def generateHit(self):
      if self.lastHitRow != -1 and self.lastHitCollumn != -1: 
         if self.hitDirection == "down":
            row = self.lastHitRow + 1
            collumn = self.lastHitCollumn
         elif self.hitDirection == "up":
            row = self.lastHitRow - 1
            collumn = self.lastHitCollumn
         elif self.hitDirection == "left":
            row = self.lastHitRow
            collumn = self.lastHitCollumn - 1
         elif self.hitDirection == "right":
            row = self.lastHitRow
            collumn = self.lastHitCollumn + 1
      else: 
         row = random.randint(0,9)
         if row % 2 == 0:
            collumn = random.randrange(0,10,2)
         else:
            collumn = random.randrange(1,10,2)

      hit = {"row" : row, "collumn" : collumn}

      return hit
