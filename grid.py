import ships

#* 
def drawMap(currentMapArray):
    for i in currentMapArray:
        if(i%10):
            print("----------------------------------")
        print("| " + i)
    
