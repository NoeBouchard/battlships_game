Battleship Game
A web-based implementation of the classic Battleship game, featuring a player-versus-AI gameplay experience. This project allows players to place their battleships on a grid, attack the AI's grid, and try to sink all the AI's ships before their own fleet is destroyed.

Features
Custom Battleship Placement: Players can manually position their ships on a 10x10 grid.
Random AI Placement: The AI places its ships randomly.
Turn-Based Gameplay: Players take turns attacking the AI's grid, while the AI counterattacks.
Real-Time Updates: Displays hits, misses, and sunk ships in real-time.
Game State Tracking: Ensures that repeated moves or invalid inputs are handled gracefully.
Dynamic Logging: Logs both player and AI moves for better gameplay transparency.
Technologies Used
Python: For backend logic and game engine.
Flask: As the web framework for serving the game interface and handling requests.
HTML/CSS/JavaScript: For the frontend user interface, grid interaction, and real-time updates.
JSON: For handling and storing ship placement data.
Git: For version control and project collaboration.
How to Set Up the Project
Prerequisites
Install Python 3.x
Install pip (Python package manager)
Installation Steps
Clone this repository:


git clone https://github.com/yourusername/battleship-game.git
cd battleship-game
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:


pip install -r requirements.txt
Run the Flask application:

python main.py
Open the game in your web browser at http://127.0.0.1:5000.

Gameplay Instructions
Setup Phase:

Navigate to the /placement page.
Place your ships on the grid using the UI. Press the "Send" button to confirm placement.
AI ships are placed randomly.
Game Phase:

Navigate to / to begin the game.
Click on a cell in the AI's grid to attack.
Logs will display the result of your move and the AI's counterattack.
Victory or Defeat:

The game ends when either all of your ships or all of the AI's ships are sunk.
A victory or defeat message will be displayed.
Project Structure


battleship-game/
├── components.py       # Game components (initialization, placement, etc.)
├── game_engine.py      # Game logic for attacks and validation
├── mp_game_engine.py   # Multiplayer/AI opponent logic
├── main.py             # Main Flask application
├── templates/          # HTML templates for the frontend
│   ├── main.html       # Main gameplay interface
│   ├── placement.html  # Ship placement interface
│   └── error.html      # Error page template
├── static/             # Static assets (CSS, JS, etc.)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation (this file)
Example Gameplay
Custom Placement Page

Main Gameplay Interface

Future Improvements
Multiplayer Support: Add an option for two players to compete online.
AI Difficulty Levels: Introduce configurable difficulty levels for the AI.
Save/Load Game: Allow players to save and resume games.
Dynamic Grid Sizes: Support grids of different dimensions.
Contributing
Feel free to submit pull requests or report issues. Contributions are always welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more details.