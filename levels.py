from core import GameCore
from board import GameBoard
from movement_programms import Player_move
from main_functions import sleep_and_clear

class GameLevels(GameCore):
    def __init__(self):
        super().__init__()
        self.board = GameBoard()

    def game1(self): # Dzielnica 1
        while True:
            print("...Stare miasto...\n\n\n")
            self.make_players()
            print(f"START.{self.board.generate_board()}\n \
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
                print(self.board.generate_board())
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
        {self.board.generate_board()} \n \
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
                print(self.board.generate_board())
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
        {self.board.generate_board()} \n \
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
                print(self.board.generate_board())
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
        {self.board.generate_board()}.META")
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
                print(self.board.generate_board())
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