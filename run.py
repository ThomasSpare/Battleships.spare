# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint
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
    print(colored(
        """
            ___  ____ ___ ___ _    ____ ____ _  _ _ ___  ____                            
            |__] |__|  |   |  |    |___ [__  |__| | |__] |__                             
            |__] |  |  |   |  |___ |___ ___] |  | | |    ___|                            
                            __     __                                                    
                            \_\_   \_\_  ________                                        
                            \  \   \  \/        \                                       
            ____________|¨¨¨¨¨¨¨¨¨¨¨¨¨^         ^¨¨¨\_______/¨¨¨¨\~~~==______          
            \                                                          /               
            ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ ¨¨¨¨¨¨¨¨¨¨¨¨ ¨¨¨¨¨¨¨¨¨¨¨¨ ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ \n
        """, "cyan"))
game = True
user_name = input("Captain, please write your name in the logbook to do battle: ")        
time.sleep(1)
print(colored("Board sizes: 6 X 6  or 10 X 10 (choose 6 or 10)","light_green"))
time.sleep(1)

while game:
    difficulty = input("Ay Captain " + user_name + ", now choose the size of your board (6 or 10): ")

    if difficulty == "6":
            boardsize = "6"
            ValueError
            "Choose a board by pressing 6 or 10 sire."
            game = False
        

    elif difficulty == "10":
        boardsize = "10"
        ValueError
        "Choose a board by pressing 6 or 10 sire."
        game = False
    else:
            print(colored("Captain "+ user_name +" we dont have time for this, choose 6 or 10, the enemy is near."))
            game = True
            

    print("Very Good Captain! We'll set up a "+ boardsize +" x "+ boardsize +" board for ya right away.")
    time.sleep(1)
    clear_console()
    print(colored(""" 
    To win this game you must defeat the cunning Captain John McWhir whos gone mad and turned against us.
    He is hiding together with his fleet somewhere out there. We must shoot down his fleet before he
    can bombard our ships. 
    ""","cyan"))
    time.sleep(2)
    print(colored("""
    Unfortunatly this weather doesn´t make it an easy task. The Typhoon that is roaring across the sea will
    make it even more difficult as ships that are hit can be concealed again and blown away to some other place.
    ""","cyan"))
    time.sleep(2)
    print(colored("""
    We must shoot down his ships as fast as possible or he will sneak up on us and wipe us out. 
    Now place your ships wisely on the board.
    ""","cyan"))
    RunGame()



class GameBoard:
    def __init__(self, board):
        self.board = board



def get_letter_to_numbers():
    letters_to_numbers = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10} 
    return letters_to_numbers

  
def print_board(self):
    print(" A B C D E F G H I J K")
    print(" +-+-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in self.board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1  


class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 9), random.randint(0, 9)
            while self.board[self.x_row][self.y_cloumn] == "░":
                    self.x_row, self.y_cloumn = random.randint(0, 9), random.randint(0, 9)
            self.board[self.x_row][self.y_column] ="░"
        return self.board


    def get_user_input  (self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in '123456789':
                print('Not an appropriate choice, please select a valid row')
                x_row = input("Enter the row of the ship: ")

            y_column = input("ENter the column letter of the ship: ").upper()
            while y_column not in "ABCDEFGHIJ":
                print('Not an appropriate choice, please select a vaslid column')
            return int(x_row) -1, GameBoard.get_letters_to_numbers()[y_column]
        except ValueError and Keyerror:
            print("Not a valid input")
            return self.get_user_input() 


def count_hit_ships(self):
    hit_ships = 0
    for row in self.board:
        for colummn in row:
            if column == "░":
                hit_ships += 1
    return hit_ships

    
def RunGame(): 
  computer_board = GameBoard([[" "] * 8 for i in range(8)])
  user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
  Battleship.create_ships(computer_board)
  #start 10 turns
  turns = 10
  while turns > 0:
    GameBoard.print_board(user_guess_board)
    #get user input
    user_x_row, user_y_column = Battleship.get_user_input(object)
    #check if duplicate guess
    while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "░":
      print("You guessed that one already")
      user_x_row, user_y_column = Battleship.get_user_input(object)
    #check for hit or miss
    if computer_board.board[user_x_row][user_y_column] == "░":
      print("You sunk 1 of my battleship!")
      user_guess_board.board[user_x_row][user_y_column] = "░"
    else:
      print("You missed my battleship!")
      user_guess_board.board[user_x_row][user_y_column] = "-"
    #check for win or lose
    if Battleship.count_hit_ships(user_guess_board) == 5:
      print("You hit all 5 battleships!")
      break
    else:
      turns -= 1
      print(f"You have {turns} turns remaining")
      if turns == 0:
        print("Sorry you ran out of turns")
        GameBoard.print_board(user_guess_board)
        break

if __name__ == '__main__':
  RunGame()