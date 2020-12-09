class ship:  # parent ship function
    # constructor takesin ship name as a parameter
    def __init__(self, shipName, RowStart, columnStart, RowEnd, columnEnd, isSunk=False, creatingShip=False):
        self.name = shipName
        self.ShipRowStart = RowStart
        self.ShipcolumnStart = columnStart
        self.ShipRowEnd = RowEnd
        self.ShipcolumnEnd = columnEnd
        self.sunk = isSunk
        self.created = creatingShip

    def getSunk(self):
        return self.sunk

    def setSunk(self, isSunk):
        self.sunk = isSunk

    def getName(self):  # get function for ship name
        return self.name

    def setName(self, shipName):  # set function for ship name
        self.name = shipName

    # function to set the ships posistion
    def setShipPos(self, RowStart, columnStart, RowEnd, columnEnd):
        self.ShipRowStart = RowStart
        self.ShipcolumnStart = columnStart
        self.ShipRowEnd = RowEnd
        self.ShipcolumnEnd = columnEnd

    def printLocation(self):  # function to display the ships location
        print("  %s is at location (%s,%s) to (%s, %s)." % (
            self.name, self.ShipcolumnStart, self.ShipRowStart, self.ShipcolumnEnd, self.ShipRowEnd))

    def isCreated(self):  # function to determine if the ship has been created
        return self.created

    def setCreated(self):  # function to determine if the ship has been created
        self.created = not self.created

    def getStartColumn(self):
        return self.ShipcolumnStart

    def getStartRow(self):
        return self.ShipRowStart

    def getEndColumn(self):
        return self.ShipcolumnEnd

    def getEndRow(self):
        return self.ShipRowEnd


class carrier(ship):  # carrier is a class with the parent class ship
    def __init__(self, RowStart, columnStart, RowEnd, columnEnd):  # constructor for carrier class
        self.size = 5
        ship.__init__(self, "Carrier", RowStart,
                      columnStart, RowEnd, columnEnd)

    def getSize(self):  # function to return the ship size
        return self.size

    def setSize(self, size):  # function to change the ship size
        self.size = size


class battleShip(ship):  # battleShip is a class with the parent class ship
    # constructor for battleShip class
    def __init__(self, RowStart, columnStart, RowEnd, columnEnd):
        self.size = 4
        ship.__init__(self, "BattleShip", RowStart,
                      columnStart, RowEnd, columnEnd)

    def getSize(self):  # function to display the ship size
        return self.size

    def setSize(self, size):  # function to change the ship size
        self.size = size


class cruiser(ship):  # cruiser is a class with the parent class ship
    def __init__(self, RowStart, columnStart, RowEnd, columnEnd):  # constructor for cruiser class
        self.size = 3
        ship.__init__(self, "Cruiser", RowStart,
                      columnStart, RowEnd, columnEnd)

    def getSize(self):  # function to return ship size
        return self.size

    def setSize(self, size):  # function to change ship size
        self.size = size


class submarine(ship):  # submarine is a class with the parent class ship
    # constructor for the submarine class
    def __init__(self, RowStart, columnStart, RowEnd, columnEnd):
        self.size = 3
        ship.__init__(self, "Submarine", RowStart,
                      columnStart, RowEnd, columnEnd)

    def getSize(self):  # function to return the ships size
        return self.size

    def setSize(self, size):  # function to change the ships size
        self.size = size


class destroyer(ship):  # destroyer is a class with the parent class ship
    # constructor for the destroyed class
    def __init__(self, RowStart, columnStart, RowEnd, columnEnd):
        self.size = 2
        ship.__init__(self, "Destroyer", RowStart,
                      columnStart, RowEnd, columnEnd)

    def getSize(self):  # function to return ship size
        return self.size

    def setSize(self, size):  # function to change ship size
        self.size = size
