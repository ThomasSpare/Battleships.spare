
from toolbox import clear_console
from termcolor import colored
import time
import random

ship_sizes = [2, 3, 3, 4, 5]


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



Intro = True
user_name=input("Captain, write your name in the logbook to do battle: ")        
time.sleep(1)
print(colored("Board sizes: 5 X 5  or 20 X 20 (enter 5 or 20)", "light_green"))
time.sleep(1)

while Intro:
    difficulty = input("Captain " + user_name + ", enter boardsize (5 or 20): ")

    if difficulty == "5":
        boardsize = "5"
        ValueError
        "Choose a board by pressing 5 or 20 sire.\n"
        Intro = False
    elif difficulty == "20":
        boardsize = "20"
        ValueError
        "Choose a board by pressing 5 or 20 sire.\n"
        Intro = False
    else:
        print(colored("Captain "+ user_name +
        "we dont have time for this, choose 5 or 20, the enemy is near.\n"))
        Intro = True
    print("Very Good Captain! We'll set up a "
    + boardsize +" x "+ boardsize +" board for ya right away.\n")
    time.sleep(1)
    clear_console()
    print(colored(""" 
    To win this game you must defeat the cunning Captain John McWhir
    whos gone mad and turned against us.
    He is hiding together with his fleet somewhere out there. 
    We must shoot down his fleet before he
    can bombard our ships. 
    \n""","cyan"))
    time.sleep(2)
    print(colored("""
    Unfortunatly this weather doesn´t make it an easy task.
     The Typhoon that is roaring across the sea will
    make it even more difficult as ships that are hit can be concealed 
    again and blown away to some other place.
    \n""","cyan"))
    time.sleep(2)
    print(colored("""
    We must shoot down his ships as fast as possible or he will 
    sneak up on us and wipe us out. 
    Now place your ships wisely on the board.
    \n""","cyan"))


    
class GameBoard:
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




class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.Xrow, self.Yclm = random.randint(0, 4), random.randint(0, 4)
            while self.board[self.Xrow][self.Yclm] == "X":
                self.Xrow, self.Yclm = random.randint(0, 4), random.randint(0, 4)
            self.board[self.Xrow][self.Yclm] = "X"
        return self.board

    def get_user_input(self):
        try:
            Xrow = input("Enter the row of the ship: ")
            while Xrow not in '12345':
                print('You cannot do that, please select a valid row\n')
            Xrow = input("Enter the row of the ship: \n")
            Yclm = input("Enter the column letter of the ship: ").upper()
            while Yclm not in "ABCDE":
                print('You can not do that, please select another column\n')
            return int(Xrow) -1, GameBoard.get_let_to_num()[Yclm]
        except ValueError:
            print("Not a valid input\n")
            return self.get_user_input()


    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships






def RunGame():
    print(f"Welcome Captain {user_name}. Let's get into Battle!")
    time.sleep(1)
    print(colored(f"Mcwhir: Captain {user_name} I will show you pain!","red"))
    computer_board = GameBoard([[" "] * 5 for i in range(5)])
    UsrBrd = GameBoard([[" "] * 5 for i in range(5)])
    Battleship.create_ships(computer_board)

    turns = 10
    while turns > 0:
        GameBoard.print_board(UsrBrd)
        Xrow, Yclm = Battleship.get_user_input(object)
        while UsrBrd.board[Xrow][Yclm] =="-" or UsrBrd.board[Xrow][Yclm]== "X":
            print("You guessed that one already")
            Xrow, Yclm = Battleship.get_user_input(object)
        if computer_board.board[Xrow][Yclm] == "X":
            print("You will pay for sinking 1 of my battleships!\n")
            UsrBrd.board[Xrow][Yclm] = "X"
        else:
            print("Ha, You missed my battleship!")
            UsrBrd.board[Xrow][Yclm] = "-"
        if Battleship.count_hit_ships(UsrBrd) == 5:
            print("YOU WON - Damn You for destroying my fleet!\n")
            break
    
        turns -= 1
        print(f"You have {turns} turns remaining")
        if turns == 0:
            print("Captain Mcwhir won\n")
            GameBoard.print_board(UsrBrd)
            break

if __name__ == '__main__':
    RunGame()