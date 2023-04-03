


ROWS = boardsize
SHIP = "░"
HITSHIP = "█"



class boardTEN:   
    def __init__(self, SHIP, name = ""):
        self.board = [[SHIP] * COLUMNS for _ in range(ROWS)]
        self.name = name
        self.symbol = SHIP
        self.hits = 0



class boardSIX:
    def __init__(self, SHIP, name = ""):
        self.board = [[SHIP] * COLUMNS for _ in range(ROWS)]
        self.name = name
        self.symbol = SHIP
        self.hits = 0


def buildboard(str, boardsize):
    """
    Function for setting up users board
    at game start
    """
    if boardsize == 10
        self.boardTEN(10)
    
