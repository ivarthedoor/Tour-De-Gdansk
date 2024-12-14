README - Tour De Gdańsk Game


Description:
Tour De Gdańsk is an interactive board game for 4 players, the goal of which is to travel through different districts in the city of Gdańsk. 
Players answer quiz questions to earn points and progress through each district. 
The game is divided into four districts, each with its own set of challenges and questions. The first player to reach the "Finish Line" wins the game.

Features:
Interactive gameplay: Players roll the dice to move around the board, answering quiz questions that appear when they land on specific spaces.

Dynamic question system: Questions are categorized by district and can be multiple choice (ABCD) or true/false questions.

Multiplayer: Supports four players with individual player positions and scores.
Game board: Simple but functional board system where players' progress is visually tracked.


Prerequisites:
Python 3.x
Required Python libraries:
csv (for loading player data and points)
json (for loading question data)
random (for rolling the dice)
os (for clearing the console)
time (for sleep and clearing operations)


Installation:
Clone the repository or download the files.
Make sure Python 3.x is installed on your system.
Go to the project directory and run the game by executing the main.py script.
bash
Copy the code
python final_game.py


Game flow:
1. Menu:
Player has to chose one of three options:
Start game, Ranking - show all scores, Quit the game.

2. Start the game:
Players enter their names at the beginning of the game.
The game takes place in four districts of Gdańsk:
-Stare Miasto
-Stare Przedmieście
-Oliwa
-Wrzeszcz

3. Roll the dice:
On each turn, players roll a dice (1-6), which determines how far they will move on the board.

4. Answering Questions:
Upon reaching specific locations, players are asked to answer a quiz question.
The question is randomly selected from a pool of district-specific "ABCD" or "True/False" questions loaded from the questions.json file.
Note:
When answering "abcd" questions, the answer must be very specific, e.g. "A" or "B"; "True/False" questions also require a very specific answer of "Tak" or "Nie".

5. Winning the Game:
The first player to reach position 30 ("Finish") ends the game.
Players earn points for correctly answering questions and advancing.
Payer who earn the most points wins the game.

6. Quitting the Game:
Players can quit the game at any time by pressing "q".


Game Structure:
1. final_game.py:
Contains the menu and main game initiation function that calls up levels and controls the flow of the game.

2. levels.py:
Defines the different levels (districts) and controls the game logic for each district.

3. board.py:
Contains the logic for generating the game board and displaying it after each turn.

4. movement_programms.py:
Handles dice rolls and player movement logic across the board.

5. questions.json, questions_reading.py:
Manages the quiz question system by fetching and presenting district-specific questions to players.

6. core.py:
Responsible for the core game mechanics, such as tracking player names, positions, and points.

7. utils.py:
Contains helper functions, including sleep_and_clear to pause and clear the screen between turns.

8. ranking.csv, data_adding_program.py:
Contains player data in csv format and supports saving and loading player data along with points.

9. showing_players_ranking.py:
Short function to read and print players ranking from ranking.csv


Thanks for playing Tour De Gdansk! We hope you enjoy the game and the fun quiz questions as you explore the city. Enjoy!