import random
import json


def  initialise_board(size=10):
    board = [[None]*size for _ in range(size)]
    return board



def create_battleships(filename='battleships.txt'):
    battleships = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            battleships[key] = int(value)
    return battleships


def place_battleships(board = None, ships = None, type = "simple"):

    if board == None:
        board = initialise_board()

    if ships == None:
        ships = create_battleships()

    if type == "simple":
        # initialize at the first row
        row = 0
        for ship_name, ship_size in ships.items():
            if row >= len(board):
                raise ValueError("Not enough rows on the board to place all ships.")
            if int(ship_size)> len(board[row]):
                raise ValueError(f"Ship {ship_name} is too large for the board's row size.")
            for col in range(int(ship_size)):
                board[row][col] = ship_name
            row+=1

    if type == "random":
        for ship_name, ship_size in ships.items():
            orientation = random.randint(1,2) # 1= horizontal placement, 2 = vertical placement
            while True:
                if orientation ==1:
# remove one to the number of columns and rows because the grid indexing starts at 0 and ends at length-1
                    x_coordinate = random.randint(0,len(board[0])-1) # horizontal coordinate (number of columns)
                    y_coordinate = random.randint(0, len(board)-1) # vertical coordinate (number of rows)
                    # if the boats is too long horizontally and gets out of the board restart
                    if x_coordinate+int(ship_size)>len(board[0]):
                        continue
                    # checks if the boat is overlapping another boat
                    if any(board[y_coordinate][x] is not None for x in range(x_coordinate, x_coordinate + int(ship_size))):
                        continue
                    # iterate from the x coordinate and add 1 each time so that the boat is placed horizontally
                    for x in range(x_coordinate, x_coordinate+int(ship_size)): 
                        board[y_coordinate][x] = ship_name
                    break
                if orientation ==2:
                    x_coordinate = random.randint(0,len(board)-1)
                    y_coordinate = random.randint(0, len(board[0])-1)
                    # if the boats is too long vertically and gets out of the board restart
                    if y_coordinate+int(ship_size)>len(board):
                        continue
                    if any(board[y][x_coordinate] is not None for y in range(y_coordinate, y_coordinate + int(ship_size))):
                        continue
                    for y in range(y_coordinate, y_coordinate+int(ship_size)):
                        board[y][x_coordinate] = ship_name
                    break
    
    if type == "custom":
        with open("placement.json", 'r') as file:
            dictionnary = json.load(file)
        for boat, placement in dictionnary.items():
            (x_coordinate) = int(placement[0])
            y_coordinate = int(placement[1])
            orientation = placement[2]
            ship_size = int(ships[boat])

            if orientation == "h":
                if x_coordinate + ship_size > len(board[0]):
                    raise ValueError("Boat cannot be placed here.")
                if any(board[y_coordinate][x] is not None for x in range(x_coordinate, x_coordinate + ship_size)):
                    raise ValueError("Boat cannot be placed here.")
            # Place the boat horizontally
                for x in range(x_coordinate, x_coordinate + ship_size):
                    board[y_coordinate][x] = boat
            
            if orientation == "v":
                if y_coordinate + ship_size > len(board):
                    raise ValueError("Boat cannot be placed here.")
                if any(board[y][x_coordinate] is not None for y in range(y_coordinate, y_coordinate + ship_size)):
                    raise ValueError("Boat cannot be placed here.")
            # place the boat vertically
                for y in range(y_coordinate, y_coordinate + ship_size):
                    board[y][x_coordinate] = boat
    return board 

    

