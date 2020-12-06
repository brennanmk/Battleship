from player import player

def main():
   bot1 = player()
   bot2 = player()
   bot1.botPopulateBoard()
   bot2.botPopulateBoard()

   while bot1.getPlayerWon() == False and bot2.getPlayerWon() == False:
      bot1.botHit()  
      bot1.printEnemyMap()

if __name__=="__main__":
   main()
