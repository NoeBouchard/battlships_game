
import random
import components
import game_engine


board1 = components.initialise_board()  # Create a new board for player 1
board2 = components.initialise_board()  # Create a separate board for player 2
ships1 = components.create_battleships()
ships2 = components.create_battleships()
players = {}





def generate_attack(board, stored_coordinate):
    x = random.randint(0,len(board)-1)
    y = random.randint(0,len(board[0])-1)
    if (x,y) in stored_coordinate:
        return generate_attack(board, stored_coordinate)
    stored_coordinate.append((x, y))
    return (x, y)

def ai_opponent_game_loop():
    print("the Battleship game is about to start !")

    turn = 1 
    game = True
    stored_coordinate = []
    while game:
        if turn%2 == 1:
            player1_attack = game_engine.cli_coordinates_input()
            ai_board = players[name2]["board"]
            ships_ai = players[name2]["battleships"]
            result = game_engine.attack(player1_attack, ai_board, ships_ai)
        else:
            player1_board = players[name1]["board"]
            ships_player1 = players[name1]["battleships"]
            ai_attack = generate_attack(player1_board, stored_coordinate )
            result = game_engine.attack(ai_attack, player1_board, ships_player1)
        turn +=1
        if result == True:
            print("Hit")
        else:
            print("Miss")
        
        if all(value == 0 for value in players[name1]["battleships"].values()):
            winner = "player 2 wins"
            game = False
        elif all(value == 0 for value in players[name2]["battleships"].values()):
            winner = "player 1 wins"
            game = False
    print(winner)
    return


if __name__ == '__main__':
    name1 = input("enter player1 name")
    while True:
        name2 = input("enter player2 username, if you chose 'AI', you will play against an AI")
        if name1 == name2:
            print("you can't have the same username as player1")
            continue
        break


    players[name1] = {"board": components.place_battleships(board1, ships1, type = "custom"), "battleships":ships1}
    players[name2] = {"board": components.place_battleships(board2, ships2, type = "simple"), "battleships":ships2}
    
    ai_opponent_game_loop()


