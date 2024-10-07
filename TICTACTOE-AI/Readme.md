# Tic-Tac-Toe Game with GUI and AI

## Overview
This is a simple Tic-Tac-Toe game implemented in Python using the `Tkinter` library for the graphical user interface (GUI). The game allows you to play against an AI with different difficulty levels: **Easy**, **Medium**, and **Hard**. You can choose to start the game or let the AI go first.

## Features
1. **Player vs AI**: You (player) are "O" and the AI is "X".
2. **Difficulty Levels**:
   - **Easy**: AI makes random moves.
   - **Medium**: AI sometimes plays optimally and sometimes makes random moves.
   - **Hard**: AI always plays optimally using the minimax algorithm.
3. **Dynamic Game Start**: You can choose who starts first — you or the AI.
4. **Minimax Algorithm**: The Hard difficulty AI uses the minimax algorithm to ensure it plays the best possible move.
5. **Reset After Each Game**: The game board resets after each match, allowing you to play again.

## How to Run

### Prerequisites
- Python 3.x installed on your system.
- `Tkinter` comes pre-installed with Python on most systems. If it's missing, install it using the following command:

  ```bash
  sudo apt-get install python3-tk
  ```

### Running the Game
1. Download or clone this repository.
2. Navigate to the folder where the script is located.
3. Run the script using Python:
   ```bash
   python3 tictactoe.py
   ```

The game window will appear, and a start menu will let you choose who starts and the AI's difficulty level.

## Gameplay Instructions

### Start Menu
- After starting the game, a menu will pop up allowing you to:
  - Choose whether you or the AI will start.
  - Select the difficulty level of the AI (Easy, Medium, or Hard).

### In-Game
- The board is a 3x3 grid with 9 buttons representing each cell.
- You play as **O**, and the AI plays as **X**.
- Simply click on a button to make your move.
- The AI will make its move after you, depending on the chosen difficulty level.
- The game will end in one of the following ways:
  - You win.
  - The AI wins.
  - It's a draw.

### Post-Game
- After the game ends, a message box will pop up with the result (win, lose, or draw).
- The board will reset automatically, allowing you to play again.

## Code Breakdown

- **TicTacToe Class**: Contains the core game logic, including making moves, checking for a winner, and detecting draws.
- **minimax Function**: Implements the minimax algorithm for the AI's optimal decision-making on Hard difficulty.
- **TicTacToeGUI Class**: Manages the user interface and connects player actions with the game logic. It includes features like setting difficulty, determining who starts, and resetting the game.
- **start_menu Method**: Allows players to select who starts the game and the AI's difficulty.
- **make_ai_move Method**: Determines the AI's next move based on the chosen difficulty level.

## Future Enhancements
Some potential improvements to the game:
- Add multiplayer functionality.
- Include an option for custom board sizes (e.g., 4x4, 5x5).
- Implement better animations for moves and game results.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Contact
For any queries or suggestions, feel free to reach out to the developer.

Enjoy playing!

