from player import player

def main():
   player1 = player()
   player2 = player()

   print("Player 1 Ship Creation: \n")
   player1.createShip()
   player1.printPlayerMap()
   
   print("\n\nPlayer 2 Ship Creation: \n")
   player2.createShip()
   player2.printPlayerMap()

   while not player1.getPlayerWon() and not player2.getPlayerWon():
      print("\nPlayer 1's Turn: \n")
      player2.printEnemyMap()
      player2.hit()
      player2.isSunk()

      print("\n\nPlayer 2's Turn: \n")
      player1.printEnemyMap()
      player1.hit()
      player1.isSunk()

   if player1.getPlayerWon():
      print("\n\nPlayer 1 Won!")
   else:
      print("\n\nPlayer 2 Won!")


if __name__=="__main__":
   main()
