from levels import GameLevels
from utils import sleep_and_clear
from showing_players_ranking import showing_ranking

def menu():
    while True: 
        sleep_and_clear(0) 
        print("Witaj w grze Tour De Gdańsk! Zapraszamy do wspólnej zabawy i nauki\n")
        print("Menu główne\n - Start gry\n - Ranking\n - Wyjdź z gry\n")
        player_input = input("Wpisz S żeby rozpocząć grę, R żeby otworzyć ranking lub Q żeby opuścić grę:\n").lower()
        if player_input == "r":
            sleep_and_clear(0)
            showing_ranking()
            input("Wpisz Q żeby wrócić do menu:\n").lower
            sleep_and_clear(0)
        elif player_input == "q":
            sleep_and_clear(0) 
            print("Koniec gry")
            exit()
        elif player_input == "s":
            sleep_and_clear(0)
            break
        else:
            print("Wpisałeś zły znak. Wpisz S, R lub Q")
            sleep_and_clear(3)
menu()
class StartGame(GameLevels):
    def __init__(self):
        super().__init__()

    def initial_game(self): 
        while True:
            if not self.level_1():
                break
            if not self.level_2():
                break
            if not self.level_3():
                break
            if not self.level_4():
                break
            if not self.finish():
                break
        print("Wychodzę do menu głownego")
        sleep_and_clear(2)
        menu()

start = StartGame()
start.initial_game()