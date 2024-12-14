from levels import GameLevels
from utils import sleep_and_clear

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
        print("Koniec")