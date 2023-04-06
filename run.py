from toolbox import clear_console
from termcolor import colored
import time
import random

def menu():
    """
    Opening Game screen
    """
    clear_console()
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
    """, "white", 'on_blue'))


intro = True
user_name = input("Captain, write your name in the logbook to do battle: ")
time.sleep(1)
print(colored("Board sizes avaiable: 5 X 5  (enter 5)", "light_green"))
time.sleep(1)

while intro:
    difficulty = input("Captain " + user_name + ", enter boardsize (5): ")

    if difficulty == "5":
        boardsize = "5"
        ValueError
        "Choose a board by pressing 5 sire.\n"
        intro = False
    elif difficulty == "20":
        boardsize = "20"
        ValueError
        "Choose a board by pressing 5 sire.\n"
        intro = False
    else:
        print(colored("Captain " + user_name +
        "We only have a 5x5 board at the moment, press 5.\n"))
        intro = True
    print("Very Good Captain! We'll set up a "
    + boardsize + " x " + boardsize + " board for ya right away.\n")
    time.sleep(1)
    clear_console()
    print(colored("""
    To win this game you must defeat the cunning Captain John McWhir
    whos gone mad and turned against us.
    He is hiding together with his fleet somewhere out there.
    We must shoot down his fleet before he
    can escape.
    \n""","cyan"))
    time.sleep(2)
    print(colored("""
    Unfortunatly this weather doesn´t make it an easy task.
    The Typhoon that is roaring across the sea will
    make it even more difficult so you only have 10 turns to 
    blast his five ships.
    \n""","cyan"))
    time.sleep(2)
    print(colored("""
    The 5 ships are 1 square in size. A direct hit shows a (¤) 
    a missed shot shows a (-).
    \n""","cyan"))



class gameBoard:
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
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.xrow, self.yclm = random.randint(0, 4), random.randint(0, 4)
            while self.board[self.xrow][self.yclm] == "¤":
                self.xrow, self.yclm = random.randint(0, 4),random.randint(0,4)
            self.board[self.xrow][self.yclm] = "¤"
        return self.board

    def get_user_input(self):
        try:
            xrow = input("Enter the row of the ship: ")
            if xrow not in '12345' or xrow == "" or type(xrow) != str:
                print('You cannot do that, select a row number (1-5)\n')
                xrow = input("Enter the row of the ship: \n")
            yclm = input("Enter the column letter of the ship: ").upper()
            if yclm not in "ABCDE" or yclm == "" or type(yclm) == int:
                print('You can not do that, select a letter (A-E)\n')
                yclm = input("Enter a Column A-E: \n").upper()
                if yclm == "" or type(yclm) == int:
                    get_user_input()
            return int(xrow) - 1, gameBoard.get_let_to_num()[yclm]
        except (ValueError):
            print("Not a valid input\n")
            return self.get_user_input()
            return int(xrow) - 1, gameBoard.get_let_to_num()[yclm]


    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "¤":
                    hit_ships += 1
        return hit_ships






def runGame():
    print(f"Welcome Captain {user_name}. Let's get into Battle!")
    time.sleep(1)
    print(colored(f"Mcwhir: Captain {user_name} I will show you pain!","red"))
    computer_board = gameBoard([[" "] * 5 for i in range(5)])
    usrBrd = gameBoard([[" "] * 5 for i in range(5)])
    battleship.create_ships(computer_board)

    turns = 10
    while turns > 0:
        gameBoard.print_board(usrBrd)
        xrow, yclm = battleship.get_user_input(object)
        while usrBrd.board[xrow][yclm] == "-" or usrBrd.board[xrow][yclm]=="¤":
            print("You guessed that one already")
            xrow, yclm = battleship.get_user_input(object)
        if computer_board.board[xrow][yclm] == "¤":
            print(colored("HIT ! You will pay for sinking 1 of my "
            "battleships!\n","light_green"))
            usrBrd.board[xrow][yclm] = "¤"
        else:
            print("Ha, You missed my battleship!")
            usrBrd.board[xrow][yclm] = "-"
        if battleship.count_hit_ships(usrBrd) == 5:
            print("YOU WON - Damn You for destroying my fleet!\n")
            break

        turns -= 1
        print(f"You have {turns} turns remaining")
        if turns == 0:
            print("The typhoon is destroying our ship, Captain Mcwhir\n"
            "won this time\n")
            gameBoard.print_board(usrBrd)
            break

if __name__ == '__main__':
    runGame()