# Battleship Game
---
![battleship_on_paper](https://github.com/ThomasSpare/Battleships.spare/blob/main/documentation/images/Battleship_game_board.png)
![marines_playing](https://github.com/ThomasSpare/Battleships.spare/blob/main/documentation/images/battleship_marines.jpg)
# 


# How to play
---

The user start the game by entering a username and choosing a board. At the moment only one board is available (5x5).
After this instructions follow telling the user how to win (I didn't win a single time when playing).

The storyline is that Captain Mcwhir who has gone mad and turned agianst us is hiding his fleet and the user must 
find his ships before the typhoon comes within 10 turns.
The user must hit 5 ships in the 10 turns given. The CPU place its ships randomly on the board. 


## Typhoon scenario
---
In the middle of designing the game I came up with the idea of using storms (typhoons) on the board while 
the game went on. The storms would travel from the top of the board down to the bottom. If a ship that already 
had a hit, either the COMP or users ship, was caught up in one of these storms the ship that was partly 
visible would disapear in the storm and be hidden again and moved to a different location. 

So the players would have to shoot the ship down before a typhoon came over it. If the hidden ship then would
recieve another hit the ship parts that was previously struck would be displayed again.

![added feature](https://github.com/ThomasSpare/Battleships.spare/blob/main/documentation/typhoon_scenario.png)

---

# Flowchart
---
![Flowchart](https://github.com/ThomasSpare/Battleships.spare/blob/main/documentation/Battleships_Flowchart.png)

## The flow chart above was my original idea for the game. The leaderboard function is not active in the game.



## After constructing the game the flowchart looked more like this:
![Flowchart](https://github.com/ThomasSpare/Battleships.spare/blob/main/documentation/images/Battleship_end_flow.png)



# Debugging
---

## Manual Testing

I tried entering every possible combination in the input fields and found that the game crashed
most often in the row / column input selection. So I used boolean operators in this part of the code to
nail down all the valid input values such as:
- To stop an integer input for a Column: type(yclm) != int:
- To stop a letter input (str) in a Row: type(xrow) == int:

---

**<li>Repeteadly Entering 'int' in row and 'int' in column<li>**
**This caused the game to crash in a while loop.**<br>
![int bug1](https://github.com/ThomasSpare/Battleships.spare/blob/main/documentation/Bugs/int_bug.jpg)
![int bug2](https://github.com/ThomasSpare/Battleships.spare/blob/main/documentation/Bugs/int2_bug.jpg)<br>
**Solution:**<br>
After some manual debugging I found a solution with a while loop that 
almost made it impossible to crash the game.

## Avoiding a scrolling gameboard
From the start the gameboard would after each move scroll down and create a new
gameboard. I found this rather annoying so to prevent this from happening I
made use of the function clear.console() after each user input, placing the
gameboard in a more fixed position.

## Crashes
If the user enters values in a normal fashion the game would not crash, regardless 
if it was the wrong input value type or not. Although during manual
testing if I repeatedly hit a number or letter really fast, 
the game would suddenly opt out.
  
## PEP8
Code structure check and errors in code were made using PEP8. Most errors due to the battleship logo
in the menu and consisted of 
- too many blank lines
- white spaces 
- space after/before operator

These errors didn´t at all make the program malfunction. Some errors was the result of not having
enough space to write the code with spaces due to the 80 Col limit for this project.





# Techologies and resources used
---

- Github
- Gitpod
- Heroku
- Python
- PEP8 Validator

# Python Libraries used in the game

- time
- random
- termcolor



# Future improvements
---
As the game is at present, rather rudimentary in featues, many
improvements could be built on this blueprint. 

For instance
- User can choose boardsize
- One user board / One CPU board
- Computer guess
- Advanced Computer guess
- Typhoon scenario  (se above image)
My typhoon scenario would introduce storms on the gameboard, moving over the board and
swallowing ships and moving them to another location.
- Different ship sizes




