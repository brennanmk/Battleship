from player import player

def main():
   turnCount = 0
   bot1 = player("BOT2")
   bot2 = player("BOT1")
   bot1.botPopulateBoard()
   bot2.botPopulateBoard()
   

   while bot1.getPlayerWon() == False and bot2.getPlayerWon() == False:
      bot1.botHit() 
      if bot1.getPlayerWon() == False:
         bot2.botHit()
      bot1.printPlayerMap() 
      turnCount += 1
   print(turnCount)

if __name__=="__main__":
   main()
