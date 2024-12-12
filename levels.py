from core import GameCore
from board import GameBoard
from time import sleep
from movement_programms import move_player
from utiles import sleep_and_clear, PLAYERS_POSITIONS

class GameLevels():
    def __init__(self):
        super().__init__()
        self.board = GameBoard()
        self.core = GameCore()

    def game1(self): # Dzielnica 1
        while True:
            print("...Stare miasto...\n\n")
            self.core.make_players()
            print(f"START.{self.board.generate_board()}\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")
            play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
            play = play.lower()
            # Poruszanie się graczem: 
            if play == "1":
                PLAYERS_POSITIONS[0] = move_player(PLAYERS_POSITIONS[0])
                self.core.questions_assingment(PLAYERS_POSITIONS[0], 0, "Stare miasto") # Jak jest na piątym polu to pojawia się pytanie 
                print("Teraz kolej " + self.core.red + " (2)")
                sleep_and_clear(2)

            elif play == "2":
                PLAYERS_POSITIONS[1] = move_player(PLAYERS_POSITIONS[1])
                self.core.questions_assingment(PLAYERS_POSITIONS[1], 1, "Stare miasto")
                print("Teraz kolej " + self.core.green + " (3)")
                sleep_and_clear(2)

            elif play == "3":
                PLAYERS_POSITIONS[2] = move_player(PLAYERS_POSITIONS[2])
                self.core.questions_assingment(PLAYERS_POSITIONS[2], 2, "Stare miasto")
                print("Teraz kolej " + self.core.yellow + " (4)")
                sleep_and_clear(2)

            elif play == "4":
                PLAYERS_POSITIONS[3] = move_player(PLAYERS_POSITIONS[3])
                self.core.questions_assingment(PLAYERS_POSITIONS[3], 3, "Stare miasto")
                print("Teraz kolej " + self.core.blue + " (1)")
                sleep_and_clear(2)

            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
                sleep(2)

            if PLAYERS_POSITIONS[0] == 29 or PLAYERS_POSITIONS[1] == 29 or PLAYERS_POSITIONS[2] == 29 or PLAYERS_POSITIONS[3] == 29:
                print(self.board.generate_board())
                if PLAYERS_POSITIONS[0] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(0, 1, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif PLAYERS_POSITIONS[1] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(1, 0, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif PLAYERS_POSITIONS[2] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(2, 1, 0, 3)
                    sleep_and_clear(0.01)
                    return True
                elif PLAYERS_POSITIONS[3] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(3, 0, 1, 2)
                    sleep_and_clear(0.01)
                    return True

    def game2(self): # Dzielnica 2 
        while True:
            print("...Stare przedmieście...\n\n")
            self.core.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")
            play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
            play = play.lower()

            if play == "1":
                PLAYERS_POSITIONS[0] = move_player(PLAYERS_POSITIONS[0])
                self.core.questions_assingment(PLAYERS_POSITIONS[0], 0, "Stare Przedmieście")
                print("Teraz kolej " + self.core.red + " (2)")
                sleep_and_clear(2)

            elif play == "2":
                PLAYERS_POSITIONS[1] = move_player(PLAYERS_POSITIONS[1])
                self.core.questions_assingment(PLAYERS_POSITIONS[1], 1, "Stare Przedmieście")
                print("Teraz kolej " + self.core.green + " (3)")
                sleep_and_clear(2)

            elif play == "3":
                PLAYERS_POSITIONS[2] = move_player(PLAYERS_POSITIONS[2])
                self.core.questions_assingment(PLAYERS_POSITIONS[2], 2, "Stare Przedmieście")
                print("Teraz kolej " + self.core.yellow + " (4)")
                sleep_and_clear(2)

            elif play == "4":
                PLAYERS_POSITIONS[3] = move_player(PLAYERS_POSITIONS[3])
                self.core.questions_assingment(PLAYERS_POSITIONS[3], 3, "Stare Przedmieście")
                print("Teraz kolej " + self.core.blue + " (1)")
                sleep_and_clear(2)

            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
                sleep(2)

            if PLAYERS_POSITIONS[0] == 29 or PLAYERS_POSITIONS[1] == 29 or PLAYERS_POSITIONS[2] == 29 or PLAYERS_POSITIONS[3] == 29:
                print(self.board.generate_board())
                if PLAYERS_POSITIONS[0] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(0, 1, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif PLAYERS_POSITIONS[1] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(1, 0, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif PLAYERS_POSITIONS[2] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(2, 1, 0, 3)
                    sleep_and_clear(0.01)
                    return True
                elif PLAYERS_POSITIONS[3] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(3, 0, 1, 2)
                    sleep_and_clear(0.01)
                    return True

    def game3(self): # Dzielnica 3
        while True:
            print("...Oliwa...\n\n")
            self.core.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")
            play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
            play = play.lower()

            if play == "1":
                PLAYERS_POSITIONS[0] = move_player(PLAYERS_POSITIONS[0])
                self.core.questions_assingment(PLAYERS_POSITIONS[0], 0, "Oliwa")
                print("Teraz kolej " + self.core.red + " (2)")                
                sleep_and_clear(2)

            elif play == "2":
                PLAYERS_POSITIONS[1] = move_player(PLAYERS_POSITIONS[1])
                self.core.questions_assingment(PLAYERS_POSITIONS[1], 1, "Oliwa")
                print("Teraz kolej " + self.core.green + " (3)")
                sleep_and_clear(2)

            elif play == "3":
                PLAYERS_POSITIONS[2] = move_player(PLAYERS_POSITIONS[2])
                self.core.questions_assingment(PLAYERS_POSITIONS[2], 2, "Oliwa")
                print("Teraz kolej " + self.core.yellow + " (4)")
                sleep_and_clear(2)

            elif play == "4":
                PLAYERS_POSITIONS[3] = move_player(PLAYERS_POSITIONS[3])
                self.core.questions_assingment(PLAYERS_POSITIONS[3], 3, "Oliwa")
                print("Teraz kolej " + self.core.blue + " (1)")
                sleep_and_clear(2)

            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
                sleep(2)

            if PLAYERS_POSITIONS[0] == 29 or PLAYERS_POSITIONS[1] == 29 or PLAYERS_POSITIONS[2] == 29 or PLAYERS_POSITIONS[3] == 29:
                print(self.board.generate_board())
                if PLAYERS_POSITIONS[0] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(0, 1, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif PLAYERS_POSITIONS[1] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(1, 0, 2, 3)
                    sleep_and_clear(0.01)
                    return True
                elif PLAYERS_POSITIONS[2] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(2, 1, 0, 3)
                    sleep_and_clear(0.01)
                    return True
                elif PLAYERS_POSITIONS[3] == 29:
                    self.core.position_reset()
                    self.core.next_level_points(3, 0, 1, 2)
                    sleep_and_clear(0.01)
                    return True

    def game4(self): # Dzielnica 4
        while True:
            print("...Wrzeszcz...\n\n")
            self.core.make_players()
            print(f"START.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        {self.board.generate_board()}.META\n")
            play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
            play = play.lower()

            if play == "1":
                PLAYERS_POSITIONS[0] = move_player(PLAYERS_POSITIONS[0])
                self.core.questions_assingment(PLAYERS_POSITIONS[0], 0, "Wrzeszcz")
                print("Teraz kolej " + self.core.red + " (2)")                
                sleep_and_clear(2)

            elif play == "2":
                PLAYERS_POSITIONS[1] = move_player(PLAYERS_POSITIONS[1])
                self.core.questions_assingment(PLAYERS_POSITIONS[1], 1, "Wrzeszcz")
                print("Teraz kolej " + self.core.green + " (3)")
                sleep_and_clear(2)

            elif play == "3":
                PLAYERS_POSITIONS[2] = move_player(PLAYERS_POSITIONS[2])
                self.core.questions_assingment(PLAYERS_POSITIONS[2], 2, "Wrzeszcz")
                print("Teraz kolej " + self.core.yellow + " (4)")
                sleep_and_clear(2)

            elif play == "4":
                PLAYERS_POSITIONS[3] = move_player(PLAYERS_POSITIONS[3])
                self.core.questions_assingment(PLAYERS_POSITIONS[3], 3, "Wrzeszcz")
                print("Teraz kolej " + self.core.blue + " (1)")
                sleep_and_clear(2)

            elif play == "q":
                sleep_and_clear(1)
                return False
            else:
                print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
                sleep(2)

            if any(pos == 29 for pos in PLAYERS_POSITIONS):
                print(self.board.generate_board())
                winner_index = PLAYERS_POSITIONS.index(29)
                self.core.position_reset()
                self.core.next_level_points(winner_index, *[i for i in range(4) if i != winner_index])
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