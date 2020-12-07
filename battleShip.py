from player import player

def main():
   name = input("Enter Player Name: ")
   player1 = player("HANK THE BOT")
   bot = player(name)
   player1.createShip()
   bot.botPopulateBoard()
   

   while bot.getPlayerWon() == False and player1.getPlayerWon() == False:
      player1.printPlayerMap()
      bot.printPlayerMap()
      bot.hit() 
      if bot.getPlayerWon() == False:
         player1.botHit()

if __name__=="__main__":
   main()
