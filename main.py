from utils import sleep_and_clear
from final_game import StartGame
from showing_players_ranking import ShowRanking
sleep_and_clear(0)     


class Game(StartGame):
    def __init__(self):
        super().__init__()
        self.ranking = ShowRanking()

    def menu(self):
        print("Witaj w grze Tour De Gdańsk! Zapraszamy do wspólnej zabawy i nauki\n")
        print("Menu główne\n - Start gry\n - Ranking\n - Wyjdź z gry\n")
        player_input = input("Wpisz S żeby rozpocząć grę, R żeby otworzyć ranking lub Q żeby opuścić grę: ")
        player_input.lower()
    def start(self):
        while True:    
            if player_input == "s":
                self.initial_game()
            elif player_input == "r":
                self.ranking.showing_ranking()
            elif player_input == "q":
                sleep_and_clear(0) 
                print("Koniec gry")
                return False
            else:
                print("Wpisałeś zły znak. Wpisz S, R lub Q")
                return True

start_game = Game()
start_game.start()