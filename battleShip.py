from player import player

def main(): #Written by Brennan Miller-Klugman
   name = input("Enter Player Name: ")    # Ask player to input a name(to be displayed upon winning)
   player1 = player("HANK THE BOT")       # Creating player instance for player1 and bot
   bot = player(name)               
   player1.createShip()                   # Populate player1's board using the createShip() function
   bot.botPopulateBoard()                 # Populate the bot's board
   

   while bot.getPlayerWon() == False and player1.getPlayerWon() == False: #loop to run until either the player or the bot has won the game
      player1.printPlayerMap() #prints player1's map at the begining of each turn to show what ships the bot has sunk/hit/missed
      bot.printEnemyMap() #function to show the bots board (hits/misses) without the ship locations to be used as referance by the player
      bot.hit() #function to attack the bots board
      if bot.getPlayerWon() == False: #check to make sure that the player did not win (otherwise it is possible for both the bot and the player to win on the same turn)
         player1.botHit() #allow the bot to attack the players board

if __name__=="__main__":
   main()
