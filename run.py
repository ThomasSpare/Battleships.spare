
import random
import time
from termcolor import colored
from toolbox import clear_console



def menu():
    """
    New Game Menu where player enters a username
    and can choose boards. At the moment only one 5x5 board
    is playable. After valid input instructions follow.
    """
    print(colored("""CHASING CAPTAIN MCVHIR
    """, "black", "on_red", attrs=["bold", "blink"]))


TYPHON_TURN = 0
TURNS = 0

INTRO = True
user_name = input("Captain, write your name in the logbook to do battle: \n")
time.sleep(1)
print(colored("Board sizes avaiable: 5 X 5  (enter 5)", "light_green"))
time.sleep(1)
while INTRO:
    difficulty = input("Captain " + user_name + ", enter boardsize (5): ")
    while difficulty == "" or difficulty != "5":
        print("Choose a board by pressing 5 sire.")
        difficulty = input(
            "Captain " + user_name + ", enter boardsize (5): ")
    if difficulty == "5":
        boardsize = "5"
        INTRO = False
        print(
            "Very Good Captain! We'll set up a "
            + boardsize + " x " + boardsize + " board for ya right away.")
        time.sleep(1)
        clear_console()
    print(colored("""
    To win this game you must defeat the cunning Captain John McWhir
    whos gone mad and turned against us.
    He is hiding together with his fleet somewhere out there.
    We must shoot down his fleet before he
    can escape.
    \n""", "cyan"))
    time.sleep(2)
    print(colored("""
    Unfortunatly this weather doesn´t make it an easy task.
    The Typhon_turn that is roaring across the sea will
    make it even more difficult so you only have 10 TURNS to
    blast his five ships.
    \n""", "cyan"))
    time.sleep(2)
    print(colored("""
    The 5 ships are 1 square in size. A direct hit shows a (¤)
    a missed shot shows a (-).
    \n""", "cyan"))


class GameBoard:
    """
    Creates the game board and change column letters to numbers
    to allow hit/miss checks
    """
    def __init__(self, board):
        self.board = board

    def get_let_to_num(self):
        """
        Ordering correspondence with numbers to col
        """
        let_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return let_to_num

    def print_board(self):
        """
        Prints the board with columns ABCDE
        dots mark the inner corners
        """
        print("\u0332".join("  A B C D E"))
        print("--^-^-^-^-^-")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, ".".join(row)))
            row_number += 1

    def typhoon(self):
        """
        Random func
        """
        if TYPHON_TURN % 3 == 0:
            print("The typhoon is coming Captain" + {user_name})
            for row in board:
                if "░" in row:
                    hit_index = row.index("░")
                    new_index = (hit_index + 3) % 10
                    row[hit_index] = "░"
                    row[new_index] = "░"


USRBRD = GameBoard([[" "] * 5 for i in range(5)])


class BattleShip:
    """
    Handle inputs, hits, misses and placements of ships on the GameBoard
    """
    def __init__(self, board):
        self.board = board
        BS = global BattleShip(USRBRD.board)
        # Need to Create an instance of the BattleShip class to call it outside
        # of this function

    def create_ships(self):
        """
        Random function that place CPU ships on board
        """
        for i in range(5):
            self.xrow, self.yclm = random.randint(0, 4), random.randint(0, 4)
            while self.board[self.xrow][self.yclm] == "¤":
                self.xrow, self.yclm = random.randint(0, 4), random.randint(0, 4)
            self.board[self.xrow][self.yclm] = "¤"
        return self.board

    def count_hit_ships(self, ):
        """
        Calculate if user hits or miss
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "¤":
                    hit_ships += 1
        return hit_ships

    def get_user_input(self):
        """
        Validate inputs from user. User cannot input letters for rows and vice versa.
        While loop to prompt user for correct input.
        """
        try:
            xrow = input("Enter a row (1-5): \n")
            if xrow not in '12345' or xrow == "" or not xrow.isdigit():
                print('You cannot do that, select a row number (1-5)')
                xrow = input("Enter the row of the ship: \n")
            yclm = input("Enter a column letter (A-E): \n").upper()
            if yclm not in "ABCDE" or yclm == "" or not yclm.isalpha():
                print('You cannot do that, select a letter (A-E)')
                yclm = input("Enter a Column A-E: \n").upper()
                while yclm not in "ABCDE" or yclm == "" or not yclm.isalpha():
                    clear_console()
                    yclm = input("Enter a Column A-E: \n").upper()
                    if yclm.isalpha() and yclm in "ABCDE":
                        break
            return int(xrow) - 1, GameBoard.get_let_to_num(None)[yclm]
        except ValueError:
            print("Not a valid input")
            if USRBRD.board[xrow][yclm] == "¤":
                if TYPHON_TURN % 3 == 0:
                    # Check if it's a TYPHON_TURN affected location
                    new_xrow, new_yclm = random.randint(0, 4), random.randint(0, 4)
                    while USRBRD.board[new_xrow][new_yclm] != " ":
                        new_xrow, new_yclm = random.randint(0, 4), random.randint(0, 4)
                        USRBRD.board[new_xrow][new_yclm] = "¤"
                        # Move the hit ship to a new random location
                        # Hide the hit ship in the previous location
                        USRBRD.board[xrow][yclm] = " "
                        break
                    else:
                        USRBRD.board[xrow][yclm] = "¤"
                        # Mark the hit ship normally
                    return int(xrow) - 1, GameBoard.get_let_to_num(self)[yclm]
            return self.get_user_input() 


def run_game():
    """
    Asks user to input rows and columns. Countdown TURNS from 10.
    Alerts user of hits or miss. After 10 TURNS game is over if not
    hit 5 ships and user get question to play new game.
    """
    print(f"Welcome Captain {user_name}. Let's get into Battle!")
    time.sleep(1)
    print(colored(f"Mcwhir: Captain {user_name} I will show you pain!", "red"))
    computer_board = GameBoard([[" "] * 5 for i in range(5)])
    USRBRD = GameBoard([[" "] * 5 for i in range(5)])
    BattleShip.create_ships(computer_board)

    TURNS = 10
    max_TURNS = 0

    for TYPHON_TURN in range(1, max_TURNS + 3):
        if TURNS <= max_TURNS:
            print("The Typhoon is coming Captain!")
            USRBRD.typhoon()
            USRBRD.print_board()
        else:
            while TURNS > 0:
                USRBRD.print_board()
                xrow, yclm = BattleShip.get_user_input(object)
                while USRBRD.board[xrow][yclm] == "-" or USRBRD.board[xrow][yclm] == "¤":
                    print("You guessed that one already")
                    xrow, yclm = BattleShip.get_user_input(object)
                    TURNS += 1
                if computer_board.board[xrow][yclm] == "¤":
                    clear_console()
                    print(colored("""HIT ! You will pay for sinking 1 of my
                    BattleShips!\n""", "light_green"))
                    USRBRD.board[xrow][yclm] = "¤"
                else:
                    clear_console()
                    print("Ha, You missed my Battleship!")
                    USRBRD.board[xrow][yclm] = "-"
                if BS.count_hit_ships() == 5:
                    clear_console()
                    print("YOU WON - Damn You for destroying my fleet!")
                    playagain = input("Play another game ? yes / no: \n")
                    if playagain == "y":
                        run_game()
                else:
                    clear_console()
                break
            TYPHON_TURN += 1
            TURNS -= 1
            print(f"You have {TURNS} TURNS remaining")
            if TURNS == 0:
                print(colored(
                    "GAME OVER: The TYPHON_TURN is destroying our ship,"
                    "Captain Mcwhir won this time.", "red"))
                USRBRD.print_board()
                playagain = input("Play another game ? yes / no: \n")
                if playagain == "y":
                    run_game()
                else:
                    clear_console()


if __name__ == '__main__':
    run_game()
