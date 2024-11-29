from flask import Flask, render_template, jsonify, request
import components
import json
import game_engine
import mp_game_engine

app = Flask(__name__)
SHIPS = components.create_battleships()
PLAYER_BOARD = components.initialise_board()
PLAYERS = {'player1': {"battleships": components.create_battleships().copy(), "board":components.initialise_board()}, 
'AI': {"board": components.initialise_board(), "battleships": components.create_battleships()}}
STORED_PLAYER1_ATTACKS = []
STORED_AI_ATTACKS = []


@app.route('/placement', methods=['GET','POST'])
def placement():
    global PLAYERS
    if request.method == 'GET':
        return render_template('placement.html', board_size=10, ships=SHIPS)
    if request.method == 'POST':
        placement_data = request.get_json()
        if not placement_data:
            return jsonify({'error': 'No data received'}), 400
        with open('placement.json', 'w') as file:
            json.dump(placement_data, file)
        try:
            PLAYERS['player1']["board"] = components.place_battleships(PLAYERS['player1']["board"], PLAYERS['player1']["battleships"], type="custom")
            PLAYERS['AI']["board"] = components.place_battleships(PLAYERS['AI']["board"], PLAYERS['AI']["battleships"], type="random")
            return jsonify({'message': 'Received'}), 200
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

@app.route('/')
def main():
    # Check if boards are set up for both player1 and AI
    if not PLAYERS['player1']["board"] or not PLAYERS['AI']["board"]:
        # Redirect to the placement page with an error message
        return render_template('error.html', message="Please configure your board on the <a href='/placement'>placement page</a>.")
    return render_template('main.html', player_board=PLAYERS['player1']["board"])


@app.route('/attack', methods=['GET'])
def attack():
    global PLAYERS, STORED_AI_ATTACKS, STORED_PLAYER1_ATTACKS
    player_board = PLAYERS['player1']["board"]
    player_ships = PLAYERS['player1']["battleships"]
    ai_board = PLAYERS['AI']["board"]
    ai_ships = PLAYERS['AI']["battleships"]
    if request.method == 'GET':
        x = request.args.get('x', type=int)
        y = request.args.get('y', type = int)
    if x is None or y is None:
        return jsonify({'error': 'Coordinates are missing'}), 400
    if (x,y) in STORED_PLAYER1_ATTACKS:
        return jsonify({'error': 'This coordinate has already been attacked.'}), 400

    STORED_PLAYER1_ATTACKS.append((x,y))
    player_hit = game_engine.attack((x, y), ai_board, ai_ships)

    print(f"Player attacked: x={x}, y={y}, hit={player_hit}")

   
    ai_x, ai_y = mp_game_engine.generate_attack(player_board, STORED_AI_ATTACKS)
    ai_hit = game_engine.attack((ai_x, ai_y), player_board, player_ships)
    print(f"AI attacked: x={ai_x}, y={ai_y}, hit={ai_hit}")

    player_ships_sunk = all(value == 0 for value in player_ships.values())
    ai_ships_sunk = all(value == 0 for value in PLAYERS['AI']["battleships"].values())

    if player_ships_sunk:
        return jsonify({
            'hit': player_hit,
            'AI_Turn': (ai_x, ai_y),
            'finished': "You lost! All your ships have been sunk."}), 200

    if ai_ships_sunk:
        return jsonify({
            'hit': player_hit,
            'AI_Turn': (ai_x, ai_y),
            'finished': "Congratulations! you won, you sunk all the AI's ships! "}), 200

# Continue the game
    return jsonify({'hit': player_hit,'AI_Turn': (ai_x, ai_y)}), 200



if __name__ == "__main__":
    app.run()
