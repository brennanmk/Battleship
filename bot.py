import random 

class bot: #parent ship function
   def __init__(self):
      self.something = 0

   def generateBoard(self):
      RowA = 0
      RowB =0
      CollumnA = 0
      CollumnB = 0
      orentations = ["up", "down", "left", "right"]

      i = random.randint(1,5) # Randomly choosing between 5 region

      print(i)
      
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
      row = random.randint(0, 9)
      collumn = random.randint(0, 9)
      hit = {"row" : row, "collumn" : collumn}

      return hit