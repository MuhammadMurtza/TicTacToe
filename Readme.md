# Tic Tac Toe Game

This is a simple implementation of the Tic Tac Toe game in Python using the Pygame library.

## Installation

1. Make sure you have Python 3.9 installed on your system.
2. Clone this repository to your local machine using the following command:
```git clone <repository-url>```
3. Navigate to the project directory:
```cd TicTacToe```
4. (Optional) Create and activate a virtual environment to isolate the project dependencies:

    ``` python3 -m venv venv ```

    ``` source venv/bin/activate ```
5. Install the required dependencies using pip:

    ```pip install -r requirements.txt```


## How to Play

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the following command to start the game:
```python main.py```
3. The game window will open, and you can start playing.
4. Click on an empty cell to make a move. The game alternates between the human player (O) and the AI player (X).
5. The AI player's move will be automatically calculated based on the selected game mode (Easy, Medium, or Hard).
6. The game will continue until one player wins or the game ends in a draw.
7. To restart the game, you can press the **"R"** key. 
8. The game starts with default mode which is 'Easy' mode.
9. You can switch the game modes by pressing **'E'** for Easy, **'M'** for Medium and **'H'** for Hard.
10. You can restart the game anywhere in the middle of the game or when the game ends.
11. Likewise, you can switch the game modes when the game finishes or in the middle of the game.
12. The game modes will be displayed on the Window's caption. When you switch the game mode, The caption will change after you have done your move.

## Game Modes

The game offers three difficulty modes for the AI player:

- Easy Mode: The AI player makes random moves.
- Medium Mode: The AI player uses a combination of random moves and optimal move.
- Hard Mode: The AI player uses the Minimax algorithm to make optimal moves.

### Some Clarifications

1. There are different classes to handle different things.
2. Player class is responsible for handling AI moves and Player moves
3. Board class is responsible for handling console board. (Inner Functionality)
4. Renderer class is responsible for the GUI of the game and GUI Board.
5. Game class is responsible for defining the game rules, for instance, when the game is over.
6. Main is used to initialize the classes and start the game. 
7. I have used minimax algorithm for AI to choose the optimal move. 
8. In order to optimize the algorithm I have used Alpha-Beta pruning.
9. To further optimize the algorithm we can also use memoization to store the winning moves. In my opinion, it increases space complexity and for a game like tic tac toe where moves are not as numerous as chess, increasing space complexity is not optimal.
