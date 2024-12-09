from main_functions import sleep_and_clear, BOARD_RANGE
from board import GameBoard
from movement_programms import Player_move
from questions_reading import questions_dispenser

# players_positions = [0, 0, 0, 0]
# task_assingment_positions = [i - 1 for i in BOARD_RANGE if i % 5 == 0] # Co piąte pole 
# players_points = [0, 0, 0, 0]
class GameCore:
    def __init__(self):
        self.players_positions = [0, 0, 0, 0]
        self.task_assingment_positions = [i - 1 for i in BOARD_RANGE if i % 5 == 0] # Co piąte pole 
        self.players_points = [0, 0, 0, 0]


    def position_reset(self): 
        """Resets pl pos"""
        self.players_positions[0] = 0
        self.players_positions[1] = 0
        self.players_positions[2] = 0
        self.players_positions[3] = 0

    def next_level_points(self, a: int, b: int, c: int, d: int):
        self.players_points[a] += 15
        self.players_points[b] += 5
        self.players_points[c] += 5
        self.players_points[d] += 5

    def questions_assingment(self, position: int, points_index: int, district: str)->int:  # Losowanie pytania co piąte pole 
        for i in self.task_assingment_positions:
            if position == i:
                if questions_dispenser(district):
                    sleep_and_clear(3)
                    self.players_points[points_index] += 10
                else:
                    sleep_and_clear(3)
                    if self.players_points[points_index] != 0:
                        self.players_points[points_index] -= 5
        return self.players_points[points_index]

    def make_players(self): # Generowanie graczy - ale jeszcze bez wyboru  ich ilosći 
        players = [x for x in enumerate(["Blue", "Red","Green", "Yellow"], start=1)]
        i = 0
        for i in range(len(players)):
            a, b = players[i]
            players_list = a, b
            players_board = players_list, self.players_points[i]
            print(f"{players_list[0]}.{players_list[1]}: {self.players_points[i]}")

class GameLevels(GameCore):
    def __init__(self):
        super().__init__()

    def game1(self): # Dzielnica 1
        while True:
            print("...Stare miasto...\n\n\n")
            self.make_players()
            print(f"START.{GameBoard.generate_board()}\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META")
            play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
            play = play.lower()
    # Poruszanie się graczem: 
            if play == "1":
                self.players_positions[0] = Player_move.move_player(self.players_positions[0])
                self.questions_assingment(self.players_positions[0], 0, "Stare miasto") # Jak jest na piątym polu to pojawia się pytanie 
                print("Time for Red (2)")
                sleep_and_clear(1)

            elif play == "2":
                self.players_positions[1] = Player_move.move_player(self.players_positions[1])
                self.questions_assingment(self.players_positions[1], 1, "Stare miasto")
                print("Time for Green (3)")
                sleep_and_clear(1)

            elif play == "3":
                self.players_positions[2] = Player_move.move_player(self.players_positions[2])
                self.questions_assingment(self.players_positions[2], 2, "Stare miasto")
                print("Time for Yellow (4)")
                sleep_and_clear(1)
            elif play == "4":
                self.players_positions[3] = Player_move.move_player(self.players_positions[3])
                self.questions_assingment(self.players_positions[3], 3, "Stare miasto")
                print("Time for Blue (1)")
                sleep_and_clear(1)
            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Invalid input! Please press 1, 2, 3, 4 or q.")

            if self.players_positions[0] == 29 or self.players_positions[1] == 29 or self.players_positions[2] == 29 or self.players_positions[3] == 29:
                print(GameBoard.generate_board())
                if self.players_positions[0] == 29:
                    self.position_reset()
                    self.next_level_points(0, 1, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif self.players_positions[1] == 29:
                    self.position_reset()
                    self.next_level_points(1, 0, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif self.players_positions[2] == 29:
                    self.position_reset()
                    self.next_level_points(2, 1, 0, 3)
                    sleep_and_clear(0.01)
                    return True
                elif self.players_positions[3] == 29:
                    self.position_reset()
                    self.next_level_points(3, 0, 1, 2)
                    sleep_and_clear(0.01)
                    return True

    def game2(self): # Dzielnica 2 
        while True:
            print("...Stare przedmieście...\n\n\n")
            self.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        {GameBoard.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META")
            play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
            play = play.lower()

            if play == "1":
                self.players_positions[0] = Player_move.move_player(self.players_positions[0])
                self.questions_assingment(self.players_positions[0], 0, "Stare Przedmieście")
                print("Time for Red (2)")
                sleep_and_clear(1)

            elif play == "2":
                self.players_positions[1] = Player_move.move_player(self.players_positions[1])
                self.questions_assingment(self.players_positions[1], 1, "Stare Przedmieście")
                print("Time for Green (3)")
                sleep_and_clear(1)

            elif play == "3":
                self.players_positions[2] = Player_move.move_player(self.players_positions[2])
                self.questions_assingment(self.players_positions[2], 2, "Stare Przedmieście")
                print("Time for Yellow (4)")
                sleep_and_clear(1)
            elif play == "4":
                self.players_positions[3] = Player_move.move_player(self.players_positions[3])
                self.questions_assingment(self.players_positions[3], 3, "Stare Przedmieście")
                print("Time for Blue (1)")
                sleep_and_clear(1)
            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Invalid input! Please press 1, 2, 3, 4 or q.")

            if self.players_positions[0] == 29 or self.players_positions[1] == 29 or self.players_positions[2] == 29 or self.players_positions[3] == 29:
                print(GameBoard.generate_board())
                if self.players_positions[0] == 29:
                    self.position_reset()
                    self.next_level_points(0, 1, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif self.players_positions[1] == 29:
                    self.position_reset()
                    self.next_level_points(1, 0, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif self.players_positions[2] == 29:
                    self.position_reset()
                    self.next_level_points(2, 1, 0, 3)
                    sleep_and_clear(0.01)
                    return True
                elif self.players_positions[3] == 29:
                    self.position_reset()
                    self.next_level_points(3, 0, 1, 2)
                    sleep_and_clear(0.01)
                    return True

    def game3(self): # Dzielnica 3
        while True:
            print("...Oliwa...\n\n\n")
            self.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        {GameBoard.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META")
            play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
            play = play.lower()

            if play == "1":
                self.players_positions[0] = Player_move.move_player(self.players_positions[0])
                self.questions_assingment(self.players_positions[0], 0, "Oliwa")
                print("Time for Red (2)")
                sleep_and_clear(1)

            elif play == "2":
                self.players_positions[1] = Player_move.move_player(self.players_positions[1])
                self.questions_assingment(self.players_positions[1], 1, "Oliwa")
                print("Time for Green (3)")
                sleep_and_clear(1)

            elif play == "3":
                self.players_positions[2] = Player_move.move_player(self.players_positions[2])
                self.questions_assingment(self.players_positions[2], 2, "Oliwa")
                print("Time for Yellow (4)")
                sleep_and_clear(1)
            elif play == "4":
                self.players_positions[3] = Player_move.move_player(self.players_positions[3])
                self.questions_assingment(self.players_positions[3], 3, "Oliwa")
                print("Time for Blue (1)")
                sleep_and_clear(1)
            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Invalid input! Please press 1, 2, 3, 4 or q.")

            if self.players_positions[0] == 29 or self.players_positions[1] == 29 or self.players_positions[2] == 29 or self.players_positions[3] == 29:
                print(GameBoard.generate_board())
                if self.players_positions[0] == 29:
                    self.position_reset()
                    self.next_level_points(0, 1, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif self.players_positions[1] == 29:
                    self.position_reset()
                    self.next_level_points(1, 0, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif self.players_positions[2] == 29:
                    self.position_reset()
                    self.next_level_points(2, 1, 0, 3)
                    sleep_and_clear(0.01)
                    return True
                elif self.players_positions[3] == 29:
                    self.position_reset()
                    self.next_level_points(3, 0, 1, 2)
                    sleep_and_clear(0.01)
                    return True

    def game4(self): # Dzielnica 4
        while True:
            print("...Wrzeszcz...\n\n\n")
            self.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        {GameBoard.generate_board()}.META")
            play = input("press 1 to move Blue, 2 to move Red, 3 to move Green, 4 to move Yellow or q to quit: ")
            play = play.lower()

            if play == "1":
                self.players_positions[0] = Player_move.move_player(self.players_positions[0])
                self.questions_assingment(self.players_positions[0], 0, "Wrzeszcz")
                print("Time for Red (2)")
                sleep_and_clear(1)

            elif play == "2":
                self.players_positions[1] = Player_move.move_player(self.players_positions[1])
                self.questions_assingment(self.players_positions[1], 1, "Wrzeszcz")
                print("Time for Green (3)")
                sleep_and_clear(1)

            elif play == "3":
                self.players_positions[2] = Player_move.move_player(self.players_positions[2])
                self.questions_assingment(self.players_positions[2], 2, "Wrzeszcz")
                print("Time for Yellow (4)")
                sleep_and_clear(1)
            elif play == "4":
                self.players_positions[3] = Player_move.move_player(self.players_positions[3])
                self.questions_assingment(self.players_positions[3], 3, "Wrzeszcz")
                print("Time for Blue (1)")
                sleep_and_clear(1)
            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Invalid input! Please press 1, 2, 3, 4 or q.")

            if any(pos == 29 for pos in self.players_positions):
                print(GameBoard.generate_board())
                winner_index = self.players_positions.index(29)
                self.position_reset()
                self.next_level_points(winner_index, *[i for i in range(4) if i != winner_index])
                sleep_and_clear(0.01)
                return True
            






            # if any(pos == 29 for pos in self.players_positions): # Przenoszenie wszystkich graczy do następnej dzielnicy w momencie kiedy jeden z graczy dotarł do końca pierwszej dzielnicy
            #     print(f"{GameBoard.generate_board()}\n\n")
            #     scores = {"\U0001F535": self.players_points[0], "\U0001F534": self.players_points[1], "\U0001F7E2": self.players_points[2], "\U0001F7E1": self.players_points[3]}
            #     print(scores)
            #     if self.players_positions[0] == 29:
            #         print("Player A wins!")
            #     elif self.players_positions[1] == 29:
            #         print("Player B wins!")
            #     elif self.players_positions[2] == 29:
            #         print("Player C wins!")
            #     elif self.players_positions[3] == 29:
            #         print("Player D wins!")
            #     sleep_and_clear(10)
            #     break