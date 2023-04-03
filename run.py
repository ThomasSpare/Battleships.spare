# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from toolbox import clear_console
from termcolor import colored
from boardfunctions import buildboard



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

boardsize = int(str.boardsize)
print(boardsize)


def main(user_name, boardsize):
    """
#   Main run Game function
#    First engaged when user
#    has completed the input
#    validation above
#   """
    boardsize = int(boardsize)

buildboard(user_name, boardsize)

