# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from toolbox import clear_console
from termcolor import colored
import time



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
time.sleep(3)
clear_console()

