from game import Game
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def main():
    game = Game()
    console.print(Panel("Welcome to Tic Tac Toe!", style="bold green"))
    game.start_game()

    while True:
        try:
            console.print(f"[bold cyan]Player {game.current_player}[/bold cyan], it's your turn!")
            position = Prompt.ask("Enter your move (1-9)", default="1", choices=[str(i) for i in range(1, 10)])
            position = int(position) - 1

            game_over = game.make_move(position)
            if game_over:
                console.print(Panel(f"[bold magenta]Player {game.current_player} wins![/bold magenta]", style="bold green"))
                play_again = Prompt.ask("Do you want to play again? (y/n)", choices=["y", "n"])
                if play_again == 'y':
                    game.reset_game()
                else:
                    console.print("[bold yellow]Thanks for playing![/bold yellow]")
                    break
        except ValueError:
            console.print("[bold red]Invalid input! Please enter a valid number.[/bold red]")
        except KeyboardInterrupt:
            console.print("\n[bold red]Game interrupted. Goodbye![/bold red]")
            break

if __name__ == "__main__":
    main()