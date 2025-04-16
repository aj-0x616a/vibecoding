def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def validate_input(user_input):
    try:
        move = int(user_input)
        if move < 1 or move > 9:
            return False
        return True
    except ValueError:
        return False

def convert_input_to_coordinates(user_input):
    move = int(user_input) - 1
    return divmod(move, 3)