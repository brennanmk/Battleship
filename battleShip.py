from player import player

def main():
   bot1 = player()
   bot2 = player()

   bot1.botPopulateBoard()
   bot2.botPopulateBoard()
   bot1.botHit()  
   bot2.botHit()

if __name__=="__main__":
   main()
