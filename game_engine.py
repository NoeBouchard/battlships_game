import components

def attack(coordinate, board, battleships):
    x = coordinate[0]
    y = coordinate[1]
    if board[y][x] == None:
        return False
    else:
        battleship_name = board[y][x]
        board[y][x] = None
        battleships[battleship_name]-=1
        if battleships[battleship_name]==0:
            print(f"you have sunk the {battleship_name}")
        return True



# ask for the user input for the attack, if oordinate is out of the board, prompt an error message

def cli_coordinates_input():
    user_input = input("Enter the coordinates x and y of a point for your attack (e.g., '1 2'): ")
    
    try:
        x, y = map(int, user_input.split())  # Split the input string and convert to integers

        if x<0 or x > 10 or y<0 or y> 10:
            raise ValueError
        return (x, y)
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space and in range of the board's length.")
        return cli_coordinates_input()  # ask the user again




def simple_game_loop():
    print("Hello, the battleship game will start now")
    board = components.initialise_board()  # Create an empty game board
    ships = components.create_battleships()  # Create ships with their positions
    initialized_board = components.place_battleships(board, ships)  # Place ships on the board
    game = True
    while game:
            if all(value == 0 for value in ships.values()):
                game = False
                print("you lost the game, all of your battlships have sunk !")
            else:
                attack_coordinate = cli_coordinates_input()
                result = attack(attack_coordinate, initialized_board, ships)
                if result == True:
                    print("Hit")
                else:
                    print("Miss")
        
if __name__ == '__main__':
    simple_game_loop()


