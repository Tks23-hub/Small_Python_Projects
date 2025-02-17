import os

class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter Your Name (Letters Only): ").strip()
            if name.isalpha():
                self.name = name
                break
            print("Invalid name. Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (a single letter): ").strip()
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Please choose a single letter.")

class Menu:
    def display_main_menu(self):
        print("Welcome Players")
        print("1. Start Game")
        print("2. Quit Game")
        choice = input("Enter your choice (1 or 2): ")
        return choice

    def display_endgame_menu(self, result):
        print(f"\n{result}")
        menu_text = """
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2): """
        choice = input(menu_text)
        return choice

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]  # Board initialized with numbers

    def display_board(self):
        print("\033[H\033[J", end="")  # Clears the terminal screen (cross-platform ANSI escape code)
        print("\n  Tic-Tac-Toe Board\n")
        for i in range(0, 9, 3):
            print(f"  {self.board[i]}  |  {self.board[i+1]}  |  {self.board[i+2]}")
            if i < 6:
                print("-----+-----+-----")

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid_move(self, choice):
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]

class Game:
    def __init__(self):
        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for index, player in enumerate(self.players, start=1):
            print(f"\nPlayer {index}, enter your details:")
            player.choose_name()
            player.choose_symbol()
            print("=" * 20)

    def play_game(self):
        while True:
            self.play_turn()

            if self.check_win():
                winner = self.players[1 - self.current_player_index]
                result = f"\n🎉 {winner.name} wins! 🎉"
            elif self.check_draw():
                result = "\nIt's a draw!"
            else:
                continue  # Continue to the next turn

            choice = self.menu.display_endgame_menu(result)
            if choice == "1":
                self.restart_game()
            else:
                self.quit_game()
                break

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"\n{player.name}'s turn ({player.symbol})")

        while True:
            try:
                cell_choice = int(input("Choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a valid number between 1 and 9.")

        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        print("Thanks for playing! 🎮")

print("\nGame is starting...")
if __name__ == "__main__":
    game = Game()
    game.start_game()
