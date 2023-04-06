from toolbox import clear_console
from termcolor import colored
import time
import random

# Object Oriented Programmed Battleship Game
# CODE credit
# This game was inspired by this battleship tutorial
# https://www.youtube.com/watch?v=tF1WRCrd_HQ


def menu():
    """
    New Game Menu where player enters a username
    and can choose boards. At the moment only one 5x5 board
    is playable. After valid input instructions follow.
    """


print(colored("""

        ___  ____ ___ ___ _    ____ ____ _  _ _ ___  ____                 
        |__] |__|  |   |  |    |___ [__  |__| | |__] |__                  
        |__] |  |  |   |  |___ |___ ___] |  | | |    ___|                 
                        __     __                                         
                        \_\_   \_\_  ________                             
                        \  \   \  \/        \                             
        ____________|¨¨¨¨¨¨¨¨¨¨¨¨¨^         ^¨¨¨\_______/¨¨¨¨\~~~==______ 
        \                                                          /      
        ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ¨¨¨¨¨¨¨¨¨¨¨¨ ¨¨¨¨¨¨¨¨¨¨¨¨ ¨¨¨¨¨¨¨¨¨¨¨¨¨¨ 
    """, "black", "on_red", attrs=["bold", "blink"]))


INTRO = True
user_name = input("Captain, write your name in the logbook to do battle: \n")
time.sleep(1)
print(colored("Board sizes avaiable: 5 X 5  (enter 5)", "light_green"))
time.sleep(1)

while INTRO:
    difficulty = input("Captain " + user_name + ", enter boardsize (5): ")
    while difficulty == "" or difficulty != "5":
        print("Choose a board by pressing 5 sire.")
        difficulty = input("Captain " + user_name + ", enter boardsize (5): ")
    else:
        INTRO = False
        break

    if difficulty == "5":
        boardsize = "5"
        INTRO = False
else:
    INTRO = True
    print("Very Good Captain! We'll set up a " + boardsize + " x " + boardsize 
    + " board for ya right away.")
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
    The Typhoon that is roaring across the sea will
    make it even more difficult so you only have 10 turns to 
    blast his five ships.
    \n""", "cyan"))
    time.sleep(2)
    print(colored("""
    The 5 ships are 1 square in size. A direct hit shows a (¤) 
    a missed shot shows a (-).
    \n""","cyan"))


class gameboard:
    """
    Creates the game board and change column letters to numbers
    to allow hit/miss checks
    """
    def __init__(self, board):
        self.board = board

    def get_let_to_num():
        let_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return let_to_num

    def print_board(self):
        print("\u0332".join("  A B C D E"))
        print("--^-^-^-^-^-")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class battleship:
    """
    Handle inputs, hits, misses and placements of ships on the gameboard  
    """
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        """
        Random function that place CPU ships on board
        """
        for i in range(5):
            self.xrow, self.yclm = random.randint(0, 4), random.randint(0, 4)
            while self.board[self.xrow][self.yclm] == "¤":
                self.xrow, self.yclm = random.randint(0, 4),random.randint(0,4)
            self.board[self.xrow][self.yclm] = "¤"
        return self.board

    def get_user_input(self):
        """
        Validate inputs from user. User cannot input letters for rows and
        vice versa. While loop to prompt user for correct input.
        """
        try:
            xrow = input("Enter a row (1-5): \n")
            if xrow not in '12345' or xrow == "" or type(xrow) != str:
                print('You cannot do that, select a row number (1-5)')
                xrow = input("Enter the row of the ship: \n")
            yclm = input("Enter a column letter (A-E): \n").upper()
            if yclm not in "ABCDE" or yclm == "" or type(yclm) == int:
                print('You can not do that, select a letter (A-E)')
                yclm = input("Enter a Column A-E: \n").upper()
                while yclm not in "ABCDE" or yclm == "" or type(yclm) == int:
                    clear_console()
                    yclm = input("Enter a Column A-E: \n").upper()
                    if type(yclm) == str and yclm in "ABCDE":
                        break
            return int(xrow) - 1, gameboard.get_let_to_num()[yclm]
        except (ValueError):
            print("Not a valid input")
            return self.get_user_input()
            return int(xrow) - 1, gameboard.get_let_to_num()[yclm]


    def count_hit_ships(self):
        """
        Calculate if user hits or miss
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "¤":
                    hit_ships += 1
        return hit_ships


def runGame():
    """
    Asks user to input rows and columns. Countdown turns from 10.
    Alerts user of hits or miss. After 10 turns game is over if not
    hit 5 ships and user get question to play new game. 
    """
    print(f"Welcome Captain {user_name}. Let's get into Battle!")
    time.sleep(1)
    print(colored(f"Mcwhir: Captain {user_name} I will show you pain!","red"))
    computer_board = gameboard([[" "] * 5 for i in range(5)])
    usrbrd = gameboard([[" "] * 5 for i in range(5)])
    battleship.create_ships(computer_board)

    turns = 10
    while turns > 0:
        gameboard.print_board(usrbrd)           # code below/ above shortened
        xrow, yclm = battleship.get_user_input(object)  # due to 80 Col limit
        while usrbrd.board[xrow][yclm] == "-" or usrbrd.board[xrow][yclm]=="¤":
            print("You guessed that one already")
            xrow, yclm = battleship.get_user_input(object)
        if computer_board.board[xrow][yclm] == "¤":
            clear_console()
            print(colored("""HIT ! You will pay for sinking 1 of my 
            battleships!\n""", "light_green"))
            usrbrd.board[xrow][yclm] = "¤"
        else:
            clear_console()
            print("Ha, You missed my battleship!")
            usrbrd.board[xrow][yclm] = "-"
        if battleship.count_hit_ships(usrbrd) == 5:
            clear_console()
            print("YOU WON - Damn You for destroying my fleet!")
            playagain = input("Play another game ? yes / no: \n")
            if playagain == "y":
                runGame()
            else:
                clear_console()
            break

        turns -= 1
        print(f"You have {turns} turns remaining")
        if turns == 0:
            print(colored("""GAME OVER: The typhoon is destroying our ship,
            Captain Mcwhir won this time.""", "red"))
            gameboard.print_board(usrbrd)
            playagain = input("Play another game ? yes / no: \n")
            if playagain == "y":
                runGame()
            else:
                clear_console()
            break


if __name__ == '__main__':
    runGame()