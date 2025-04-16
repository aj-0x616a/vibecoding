class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Starting player

    def start_game(self):
        self.board = [' ' for _ in range(9)]  # Reset the board
        self.current_player = 'X'  # Reset to starting player
        print("Tic Tac Toe Game Started!")
        self.display_board()

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                print(f"Player {self.current_player} wins!")
                return True
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.display_board()
            return False
        else:
            print("Invalid move! Try again.")
            return False

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True
        return False

    def reset_game(self):
        self.start_game()

    def display_board(self):
        print("\n")
        for i in range(3):
            print(f"{self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]}")
            if i < 2:
                print("---------")
        print("\n")