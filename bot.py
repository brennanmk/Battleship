import random 

class bot: #Bot class written by Hank Pham & Brennan Miller-Klugman
   def __init__(self):
      self.storeHitRow = -1
      self.storeHitcolumn = -1
      self.surround = 0

   # store the hit coordinate  
   def setHit(self, row, column):
      self.storeHitRow = row
      self.storeHitcolumn = column

   # check if there is a hit or not
   def getHit(self):
      if self.storeHitRow == -1:
         return False
      else:
         return True

   # create ships and populate bot's board
   def generateBoard(self): #Written by Hank Pham
      RowA = 0
      RowB =0
      columnA = 0
      columnB = 0
      orentations = ["up", "down", "left", "right"]

      i = random.randint(1,5) # Randomly choosing between 5 regions
      
      # 3x4 top left region
      if i == 1:
         RowA = 0
         RowB = 2
         columnA = 0
         columnB = 3
         choice = [1,2] # only allow down and left orientations
         orientationValue = random.choice(choice)

      # 3x4 bottom left region
      elif i == 2:
         RowA = 7
         RowB = 9
         columnA = 0
         columnB = 3
         choice = [0,2] # only allow up and left orientations
         orientationValue = random.choice(choice)

      # 3x4 top right region
      elif i == 3:
         RowA = 0
         RowB = 2
         columnA = 6
         columnB = 9
         choice = [1,3] # only allow down and right orientations
         orientationValue = random.choice(choice)

      # 3x4 bottom right region
      elif i == 4:
         RowA = 7
         RowB = 9
         columnA = 6
         columnB = 9
         choice = [0, 3] # only allow up and left orientations
         orientationValue = random.choice(choice)

      # 6x6 middle region
      else:
         RowA = 2
         RowB = 7
         columnA = 2
         columnB = 7 
         orientationValue = random.randint(0,3) # allow all orientations

      # choose a random start point in the selected region
      row = random.randint(RowA, RowB)
      column = random.randint(columnA, columnB)

      # store the coordinate and orientation in the dictionary shipLoc
      shipLoc = {"row" : row, "column" : column, "orientation": orentations[orientationValue]}
      
      return shipLoc


   def generateHit(self): #Written by Brennan Miller-Klugman

      # if there is no hit
      if self.storeHitcolumn == -1:
         # randomly hit in a zig zag pattern
         row = random.randint(0,9)
         if row % 2 == 0:
            column = random.randrange(0,10,2)
         else:
            column = random.randrange(1,10,2)

      # if there is a hit, hit the surrounding
      elif self.surround != 4:
         if self.surround == 0:
            row = self.storeHitRow - 1
            column = self.storeHitcolumn
         elif self.surround == 1:
            row = self.storeHitRow + 1
            column = self.storeHitcolumn
         elif self.surround == 2:
            row = self.storeHitRow
            column = self.storeHitcolumn - 1
         else:
            row = self.storeHitRow
            column = self.storeHitcolumn + 1
         # change hit direction
         self.surround += 1

      # else reset store hit location, and hit randomly in a zig zag pattern
      else:
         self.surround = 0
         self.storeHitRow = -1
         self.storeHitcolumn = -1
         row = random.randint(0,9)
         if row % 2 == 0:
            column = random.randrange(0,10,2)
         else:
            column = random.randrange(1,10,2)

      hit = {"row" : row, "column" : column}
      return hit
