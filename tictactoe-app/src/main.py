from game import Game

def main():
    game = Game()
    game.start_game()

    while True:
        try:
            position = int(input(f"Player {game.current_player}, enter your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            game_over = game.make_move(position)
            if game_over:
                play_again = input("Do you want to play again? (y/n): ").lower()
                if play_again == 'y':
                    game.reset_game()
                else:
                    print("Thanks for playing!")
                    break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main()