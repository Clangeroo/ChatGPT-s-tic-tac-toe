import tkinter as tk
from tkinter import messagebox

# Initialize the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create variables to hold player names
player_x_name = ""
player_o_name = ""
current_player = "X"
first_player = "X"
turn_label = None

# Function to set player names and start the game
def start_game():
    global player_x_name, player_o_name, turn_label
    player_x_name = player_x_entry.get()
    player_o_name = player_o_entry.get()
    if player_x_name == "" or player_o_name == "":
        messagebox.showerror("Error", "Please enter both player names.")
    else:
        name_frame.grid_forget()
        board_frame.grid(row=1, column=0, columnspan=3)
        restart_button.grid(row=3, column=0, columnspan=3)
        turn_label = tk.Label(window, text=f"{player_x_name}'s Turn (X)")
        turn_label.grid(row=0, column=0, columnspan=3)

# Create the game board state and buttons
board = [""] * 9
buttons = []

# Winning combinations
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6)              # diagonals
]

# Function to handle player moves
def handle_click(index):
    global current_player, first_player
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        # Check for a winner or a draw
        if check_winner():
            highlight_winning_combination()
            winner_name = player_x_name if current_player == "X" else player_o_name
            messagebox.showinfo("Game Over", f"{winner_name} wins!")
            disable_buttons()
            first_player = current_player
        elif "" not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            disable_buttons()
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"
            update_turn_label()

# Function to update the turn label
def update_turn_label():
    if turn_label:
        if current_player == "X":
            turn_label.config(text=f"{player_x_name}'s Turn (X)")
        else:
            turn_label.config(text=f"{player_o_name}'s Turn (O)")

# Function to check if there's a winner
def check_winner():
    for (i, j, k) in winning_combinations:
        if board[i] == board[j] == board[k] != "":
            return (i, j, k)
    return False

# Function to highlight the winning combination
def highlight_winning_combination():
    winning_combination = check_winner()
    if winning_combination:
        for index in winning_combination:
            buttons[index].config(bg="lightgreen")

# Function to disable all buttons after game ends
def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

# Function to reset the game board
def reset_board():
    global current_player
    current_player = first_player
    for i in range(9):
        board[i] = ""
        buttons[i].config(text="", state="normal", bg="SystemButtonFace")
    update_turn_label()

# Set up frames for layout
name_frame = tk.Frame(window)
board_frame = tk.Frame(window)

# Player name entry fields
player_x_label = tk.Label(name_frame, text="Player X Name:")
player_x_label.grid(row=0, column=0)
player_x_entry = tk.Entry(name_frame)
player_x_entry.grid(row=0, column=1)

player_o_label = tk.Label(name_frame, text="Player O Name:")
player_o_label.grid(row=1, column=0)
player_o_entry = tk.Entry(name_frame)
player_o_entry.grid(row=1, column=1)

start_button = tk.Button(name_frame, text="Start Game", command=start_game)
start_button.grid(row=2, column=0, columnspan=2)

name_frame.grid(row=0, column=0, columnspan=3)

# Set up the 3x3 grid of buttons
for i in range(9):
    button = tk.Button(board_frame, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: handle_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Add a restart button
restart_button = tk.Button(window, text="Restart", command=reset_board)

# Start the Tkinter main event loop
window.mainloop()
