import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]  # Return 'X' or 'O' if there's a winner
        return None

    def is_draw(self):
        return ' ' not in self.board and self.check_winner() is None

def minimax(board, depth, is_maximizing):
    game = TicTacToe()
    game.board = board
    winner = game.check_winner()

    if winner == 'X':  # AI
        return 10 - depth
    elif winner == 'O':  # Player
        return depth - 10
    elif game.is_draw():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # AI move
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # Player move
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = float('-inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'  # AI move
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def random_move(board):
    available_moves = [i for i in range(9) if board[i] == ' ']
    return random.choice(available_moves) if available_moves else None

class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToe()
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.difficulty = "Hard"  # Default difficulty

        self.buttons = [tk.Button(root, text=' ', font=('Arial', 20), width=5, height=2,
                                   command=lambda i=i: self.player_move(i)) for i in range(9)]
        
        for i, button in enumerate(self.buttons):
            button.grid(row=i // 3, column=i % 3)

        self.start_menu()

    def start_menu(self):
        menu = tk.Toplevel(self.root)
        menu.title("Choose Start")

        tk.Label(menu, text="Who starts the game?", font=('Arial', 16)).pack(pady=10)

        tk.Button(menu, text="You Start", command=lambda: self.start_game(False, menu)).pack(pady=5)
        tk.Button(menu, text="AI Starts", command=lambda: self.start_game(True, menu)).pack(pady=5)

        tk.Label(menu, text="Select Difficulty:", font=('Arial', 16)).pack(pady=10)

        difficulty_frame = tk.Frame(menu)
        difficulty_frame.pack(pady=5)

        self.difficulty_var = tk.StringVar(value=self.difficulty)
        for option in ["Easy", "Medium", "Hard"]:
            tk.Radiobutton(difficulty_frame, text=option, variable=self.difficulty_var,
                           value=option, command=lambda: self.set_difficulty(self.difficulty_var.get())).pack(anchor=tk.W)

    def set_difficulty(self, option):
        self.difficulty = option

    def start_game(self, ai_starts, menu):
        menu.destroy()  # Close the start menu
        if ai_starts:
            ai_move = self.make_ai_move()
            if ai_move is not None:  # Ensure ai_move is valid
                self.buttons[ai_move].config(text='X')

    def player_move(self, index):
        if self.game.make_move(index, 'O'):
            self.buttons[index].config(text='O')
            if self.game.check_winner():
                self.end_game("You win!")
            elif self.game.is_draw():
                self.end_game("It's a draw!")
            else:
                self.root.after(100, self.make_ai_move)  # Delay AI move for better UX

    def make_ai_move(self):
        if self.game.is_draw() or self.game.check_winner():
            return  # No move if the game is over

        if self.difficulty == "Easy":
            ai_move = random_move(self.game.board)
        elif self.difficulty == "Medium":
            if random.random() < 0.5:
                ai_move = find_best_move(self.game.board)
            else:
                ai_move = random_move(self.game.board)
        else:  # Hard
            ai_move = find_best_move(self.game.board)

        if ai_move is not None:  # Ensure ai_move is valid
            self.game.make_move(ai_move, 'X')
            self.buttons[ai_move].config(text='X')
            if self.game.check_winner():
                self.end_game("AI wins!")
            elif self.game.is_draw():
                self.end_game("It's a draw!")

    def end_game(self, result):
        messagebox.showinfo("Game Over", result)
        self.reset_game()

    def reset_game(self):
        self.game = TicTacToe()
        for button in self.buttons:
            button.config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToeGUI(root)
    root.mainloop()
 