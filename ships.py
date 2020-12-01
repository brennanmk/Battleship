class ship: #parent ship function
    def __init__(self, shipName): #constructor takesin ship name as a parameter
        self.name = shipName

    def getName(self): #get function for ship name
        return self.name

    def setName(self, shipName): #set function for ship name
        self.name = shipName


class carrier(ship): #carrier is a class with the parent class ship
    def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip=False): #constructor for carrier class
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd
        self.size = 5
        self.created = creatingShip
        ship.__init__(self, "Carrier")

    def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd): #function to set the ships posistion
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd

    def printLocation(self): #function to display the ships location
        print("  %s is at location (%s,%s) to (%s, %s)." % (
            self.name, self.ShipCollumnStart, self.ShipRowStart, self.ShipCollumnEnd, self.ShipRowEnd))

    def getSize(self): #function to return the ship size
        return self.size

    def setSize(self, size): #function to change the ship size
        self.size = size

    def isCreated(self): #function to determine if the ship has been created
        return self.created

    def getStartColumn(self):
        return self.ShipCollumnStart

    def getStartRow(self):
        return self.ShipRowStart

    def getEndColumn(self):
        return self.ShipCollumnEnd

    def getEndRow(self):
        return self.ShipRowEnd


class battleShip(ship): #battleShip is a class with the parent class ship
    def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip=False): #constructor for battleShip class
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd
        self.size = 4
        self.created = creatingShip
        ship.__init__(self, "BattleShip")

    def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd): #function to set the ships posistion
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd

    def printLocation(self): #function to display the ships location
        print("  %s is at location (%s,%s) to (%s, %s)." % (
            self.name, self.ShipCollumnStart, self.ShipRowStart, self.ShipCollumnEnd, self.ShipRowEnd))

    def getSize(self): #function to display the ship size
        return self.size

    def setSize(self, size): #function to change the ship size
        self.size = size

    def isCreated(self): #function to determine if the ship has been created
        return self.created
    
    def getStartColumn(self):
        return self.ShipCollumnStart

    def getStartRow(self):
        return self.ShipRowStart

    def getEndColumn(self):
        return self.ShipCollumnEnd

    def getEndRow(self):
        return self.ShipRowEnd


class cruiser(ship): #cruiser is a class with the parent class ship
    def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip=False): #constructor for cruiser class
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd
        self.size = 3
        self.created = creatingShip
        ship.__init__(self, "Cruiser")

    def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd): #function to set the ships posistion
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd

    def printLocation(self): #function to dispaly the ship location
        print("  %s is at location (%s,%s) to (%s, %s)." % (
            self.name, self.ShipCollumnStart, self.ShipRowStart, self.ShipCollumnEnd, self.ShipRowEnd))

    def getSize(self): #function to return ship size
        return self.size

    def setSize(self, size): #function to change ship size
        self.size = size

    def isCreated(self): #function to return the created boolean
        return self.created

    def getStartColumn(self):
        return self.ShipCollumnStart

    def getStartRow(self):
        return self.ShipRowStart

    def getEndColumn(self):
        return self.ShipCollumnEnd

    def getEndRow(self):
        return self.ShipRowEnd


class submarine(ship): #submarine is a class with the parent class ship
    def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip=False): #constructor for the submarine class
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd
        self.size = 3
        self.created = creatingShip
        ship.__init__(self, "Submarine")

    def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd): #function to set the ships location
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd

    def printLocation(self): #function to display the ships location
        print("  %s is at location (%s,%s) to (%s, %s)." % (
            self.name, self.ShipCollumnStart, self.ShipRowStart, self.ShipCollumnEnd, self.ShipRowEnd))

    def getSize(self): #function to return the ships size
        return self.size

    def setSize(self, size): #function to change the ships size
        self.size = size

    def isCreated(self): #function to return the created boolean
        return self.created

    def getStartColumn(self):
        return self.ShipCollumnStart

    def getStartRow(self):
        return self.ShipRowStart

    def getEndColumn(self):
        return self.ShipCollumnEnd

    def getEndRow(self):
        return self.ShipRowEnd


class destroyer(ship): #destroyer is a class with the parent class ship
    def __init__(self, RowStart, CollumnStart, RowEnd, CollumnEnd, creatingShip=False): #constructor for the destroyed class
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd
        self.size = 2
        self.created = creatingShip
        ship.__init__(self, "Destroyer")

    def setShipPos(self, RowStart, CollumnStart, RowEnd, CollumnEnd): #function to set the ships location
        self.ShipRowStart = RowStart
        self.ShipCollumnStart = CollumnStart
        self.ShipRowEnd = RowEnd
        self.ShipCollumnEnd = CollumnEnd

    def printLocation(self): #function to display the ships location
        print("  %s is at location (%s,%s) to (%s, %s)." % (
            self.name, self.ShipCollumnStart, self.ShipRowStart, self.ShipCollumnEnd, self.ShipRowEnd))

    def getSize(self): #function to return ship size
        return self.size

    def setSize(self, size): #function to change ship size
        self.size = size

    def isCreated(self): #function to return created boolean value
        return self.created

    def getStartColumn(self):
        return self.ShipCollumnStart

    def getStartRow(self):
        return self.ShipRowStart

    def getEndColumn(self):
        return self.ShipCollumnEnd

    def getEndRow(self):
        return self.ShipRowEnd