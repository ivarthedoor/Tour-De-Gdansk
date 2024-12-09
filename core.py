from main_functions import sleep_and_clear, BOARD_RANGE
from board import GameBoard
from movement_programms import Player_move
from questions_reading import questions_dispenser

players_positions = [0, 0, 0, 0]
task_assingment_positions = [i - 1 for i in BOARD_RANGE if i % 5 == 0] # Co piąte pole 
players_points = [0, 0, 0, 0]
class GameCore:
    def __init__(self):
        self.players_positions = players_positions
        self.task_assingment_positions = task_assingment_positions
        self.players_points = players_points


    def position_reset(): 
        """Resets pl pos"""
        players_positions[0] = 0
        players_positions[1] = 0
        players_positions[2] = 0
        players_positions[3] = 0

    def next_level_points(a: int, b: int, c: int, d: int):
        players_points[a] += 15
        players_points[b] += 5
        players_points[c] += 5
        players_points[d] += 5

    def questions_assingment(position: int, points_index: int, district: str)->int:  # Losowanie pytania co piąte pole 
        for i in task_assingment_positions:
            if position == i:
                if questions_dispenser(district):
                    sleep_and_clear(3)
                    players_points[points_index] += 10
                else:
                    sleep_and_clear(3)
                    if players_points[points_index] != 0:
                        players_points[points_index] -= 5
        return players_points[points_index]

    def make_players(): # Generowanie graczy - ale jeszcze bez wyboru  ich ilosći 
        players = [x for x in enumerate(["Blue", "Red","Green", "Yellow"], start=1)]
        i = 0
        for i in range(len(players)):
            a, b = players[i]
            players_list = a, b
            players_board = players_list, players_points[i]
            print(f"{players_list[0]}.{players_list[1]}: {players_points[i]}")

class GameLevels:
    def __init__(self):
        pass

    def game1(): # Dzielnica 1
        while True:
            print("...Stare miasto...\n\n\n")
            GameCore.make_players()
            print(f"START.{GameBoard.generate_board()}\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META")
            play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
            play = play.lower()
    # Poruszanie się graczem: 
            if play == "1":
                players_positions[0] = Player_move.move_player(players_positions[0])
                GameCore.questions_assingment(players_positions[0], 0, "Stare miasto") # Jak jest na piątym polu to pojawia się pytanie 
                print("Time for Red (2)")
                sleep_and_clear(1)

            elif play == "2":
                players_positions[1] = Player_move.move_player(players_positions[1])
                GameCore.questions_assingment(players_positions[1], 1, "Stare miasto")
                print("Time for Green (3)")
                sleep_and_clear(1)

            elif play == "3":
                players_positions[2] = Player_move.move_player(players_positions[2])
                GameCore.questions_assingment(players_positions[2], 2, "Stare miasto")
                print("Time for Yellow (4)")
                sleep_and_clear(1)
            elif play == "4":
                players_positions[3] = Player_move.move_player(players_positions[3])
                GameCore.questions_assingment(players_positions[3], 3, "Stare miasto")
                print("Time for Blue (1)")
                sleep_and_clear(1)
            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Invalid input! Please press 1, 2, 3, 4 or q.")

            if players_positions[0] == 29 or players_positions[1] == 29 or players_positions[2] == 29 or players_positions[3] == 29:
                print(GameBoard.generate_board())
                if players_positions[0] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(0, 1, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif players_positions[1] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(1, 0, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif players_positions[2] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(2, 1, 0, 3)
                    sleep_and_clear(0.01)
                    return True
                elif players_positions[3] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(3, 0, 1, 2)
                    sleep_and_clear(0.01)
                    return True

    def game2(): # Dzielnica 2 
        while True:
            print("...Stare przedmieście...\n\n\n")
            GameCore.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        {GameBoard.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META")
            play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
            play = play.lower()

            if play == "1":
                players_positions[0] = Player_move.move_player(players_positions[0])
                GameCore.questions_assingment(players_positions[0], 0, "Stare Przedmieście")
                print("Time for Red (2)")
                sleep_and_clear(1)

            elif play == "2":
                players_positions[1] = Player_move.move_player(players_positions[1])
                GameCore.questions_assingment(players_positions[1], 1, "Stare Przedmieście")
                print("Time for Green (3)")
                sleep_and_clear(1)

            elif play == "3":
                players_positions[2] = Player_move.move_player(players_positions[2])
                GameCore.questions_assingment(players_positions[2], 2, "Stare Przedmieście")
                print("Time for Yellow (4)")
                sleep_and_clear(1)
            elif play == "4":
                players_positions[3] = Player_move.move_player(players_positions[3])
                GameCore.questions_assingment(players_positions[3], 3, "Stare Przedmieście")
                print("Time for Blue (1)")
                sleep_and_clear(1)
            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Invalid input! Please press 1, 2, 3, 4 or q.")

            if players_positions[0] == 29 or players_positions[1] == 29 or players_positions[2] == 29 or players_positions[3] == 29:
                print(GameBoard.generate_board())
                if players_positions[0] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(0, 1, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif players_positions[1] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(1, 0, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif players_positions[2] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(2, 1, 0, 3)
                    sleep_and_clear(0.01)
                    return True
                elif players_positions[3] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(3, 0, 1, 2)
                    sleep_and_clear(0.01)
                    return True

    def game3(): # Dzielnica 3
        while True:
            print("...Oliwa...\n\n\n")
            GameCore.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        {GameBoard.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META")
            play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
            play = play.lower()

            if play == "1":
                players_positions[0] = Player_move.move_player(players_positions[0])
                GameCore.questions_assingment(players_positions[0], 0, "Oliwa")
                print("Time for Red (2)")
                sleep_and_clear(1)

            elif play == "2":
                players_positions[1] = Player_move.move_player(players_positions[1])
                GameCore.questions_assingment(players_positions[1], 1, "Oliwa")
                print("Time for Green (3)")
                sleep_and_clear(1)

            elif play == "3":
                players_positions[2] = Player_move.move_player(players_positions[2])
                GameCore.questions_assingment(players_positions[2], 2, "Oliwa")
                print("Time for Yellow (4)")
                sleep_and_clear(1)
            elif play == "4":
                players_positions[3] = Player_move.move_player(players_positions[3])
                GameCore.questions_assingment(players_positions[3], 3, "Oliwa")
                print("Time for Blue (1)")
                sleep_and_clear(1)
            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Invalid input! Please press 1, 2, 3, 4 or q.")

            if players_positions[0] == 29 or players_positions[1] == 29 or players_positions[2] == 29 or players_positions[3] == 29:
                print(GameBoard.generate_board())
                if players_positions[0] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(0, 1, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif players_positions[1] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(1, 0, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif players_positions[2] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(2, 1, 0, 3)
                    sleep_and_clear(0.01)
                    return True
                elif players_positions[3] == 29:
                    GameCore.position_reset()
                    GameCore.next_level_points(3, 0, 1, 2)
                    sleep_and_clear(0.01)
                    return True

    def game4(): # Dzielnica 4
        while True:
            print("...Wrzeszcz...\n\n\n")
            GameCore.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        {GameBoard.generate_board()}.META")
            play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
            play = play.lower()

            if play == "1":
                players_positions[0] = Player_move.move_player(players_positions[0])
                GameCore.questions_assingment(players_positions[0], 0, "Wrzeszcz")
                print("Time for Red (2)")
                sleep_and_clear(1)

            elif play == "2":
                players_positions[1] = Player_move.move_player(players_positions[1])
                GameCore.questions_assingment(players_positions[1], 1, "Wrzeszcz")
                print("Time for Green (3)")
                sleep_and_clear(1)

            elif play == "3":
                players_positions[2] = Player_move.move_player(players_positions[2])
                GameCore.questions_assingment(players_positions[2], 2, "Wrzeszcz")
                print("Time for Yellow (4)")
                sleep_and_clear(1)
            elif play == "4":
                players_positions[3] = Player_move.move_player(players_positions[3])
                GameCore.questions_assingment(players_positions[3], 3, "Wrzeszcz")
                print("Time for Blue (1)")
                sleep_and_clear(1)
            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Invalid input! Please press 1, 2, 3, 4 or q.")

            if players_positions[0] == 29 or players_positions[1] == 29 or players_positions[2] == 29 or players_positions[3] == 29: # Przenoszenie wszystkich graczy do następnej dzielnicy w momencie kiedy jeden z graczy dotarł do końca pierwszej dzielnicy
                print(GameBoard.generate_board())
                scores = {"\U0001F535": players_points[0], "\U0001F534": players_points[1], "\U0001F7E2": players_points[2], "\U0001F7E1": players_points[3]}
                print(scores)
                if players_positions[0] == 29:
                    print("Player A wins!")
                elif players_positions[1] == 29:
                    print("Player B wins!")
                elif players_positions[2] == 29:
                    print("Player C wins!")
                elif players_positions[3] == 29:
                    print("Player D wins!")
                sleep_and_clear(10)
                break
            

