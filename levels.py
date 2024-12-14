from core import GameCore
from board import GameBoard
from movement_programms import move_player
from utils import sleep_and_clear

class GameLevels(GameCore):
    def __init__(self):
        super().__init__()
        self.board = GameBoard()

    def level_movement_mechanics(self, district: str):
        play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
        play = play.lower()
        
        if play == "1":
            self.board.players_positions[0] = move_player(self.board.players_positions[0])
            self.points_for_questions(self.board.players_positions[0], 0, district)
            print("Teraz kolej " + self.red + " (2)")
            return True, sleep_and_clear(3)

        elif play == "2":
            self.board.players_positions[1] = move_player(self.board.players_positions[1])
            self.points_for_questions(self.board.players_positions[1], 1, district)
            print("Teraz kolej " + self.green + " (3)")
            return True, sleep_and_clear(3)
            
        elif play == "3":
            self.board.players_positions[2] = move_player(self.board.players_positions[2])
            self.points_for_questions(self.board.players_positions[2], 2, district)
            print("Teraz kolej " + self.yellow + " (4)")
            return True, sleep_and_clear(3)

        elif play == "4":
            self.board.players_positions[3] = move_player(self.board.players_positions[3])
            self.points_for_questions(self.board.players_positions[3], 3, district)
            print("Teraz kolej " + self.blue + " (1)")
            return True, sleep_and_clear(3)

        elif play == "q":
            sleep_and_clear(3)
            return False
        else:
            print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
            return True, sleep_and_clear(3)

    def final_level_movement_mechanics(self, district: str):
        play = input("Wpisz 1 żeby ruszyć niebieskim pionkiem, 2 czerwonym, 3 zielonym i 4 żółtym, albo wpisz Q żeby opuścić grę: \n")
        play = play.lower()
        
        if play == "1":
            self.board.players_positions[0] = move_player(self.board.players_positions[0])
            self.points_for_questions(self.board.players_positions[0], 0, district)
            if self.board.players_positions[0] != 29:
                print("Następnie: " + self.red + " (2)")
            return True, sleep_and_clear(3)

        elif play == "2":
            self.board.players_positions[1] = move_player(self.board.players_positions[1])
            self.points_for_questions(self.board.players_positions[1], 1, district)
            if self.board.players_positions[1] != 29:
                print("Następnie: " + self.green + " (3)")
            return True, sleep_and_clear(3)
            
        elif play == "3":
            self.board.players_positions[2] = move_player(self.board.players_positions[2])
            self.points_for_questions(self.board.players_positions[2], 2, district)
            if self.board.players_positions[2] != 29:
                print("Następnie: " + self.yellow + " (4)")
            return True, sleep_and_clear(3)

        elif play == "4":
            self.board.players_positions[3] = move_player(self.board.players_positions[3])
            self.points_for_questions(self.board.players_positions[3], 3, district)
            if self.board.players_positions[3] != 29:
                print("Następnie: " + self.blue + " (1)")
            return True, sleep_and_clear(3)

        elif play == "q":
            sleep_and_clear(3)
            return False
        else:
            print("Niepoprawny znak ruchu! Proszę wpisz 1, 2, 3, 4 lub Q żeby opuścić grę.")
            return True, sleep_and_clear(3)

    def next_level_movement_mechanics(self)->bool:
        if any(pos == 29 for pos in self.board.players_positions):
            print(self.board.generate_board())
            if self.board.players_positions[0] == 29:
                self.position_reset()
                self.next_level_points(0, 1, 2, 3)
                sleep_and_clear(0.01)
                return True
            elif self.board.players_positions[1] == 29:
                self.position_reset()
                self.next_level_points(1, 0, 2, 3)
                sleep_and_clear(0.01)
                return True
            elif self.board.players_positions[2] == 29:
                self.position_reset()
                self.next_level_points(2, 1, 0, 3)
                sleep_and_clear(0.01)
                return True
            elif self.board.players_positions[3] == 29:
                self.position_reset()
                self.next_level_points(3, 0, 1, 2)
                sleep_and_clear(0.01)
                return True

    def level_1(self):
        print("             Witamy w grze 'Tour De Gdańsk'!\n \
        Rozpoczynacie wyjątkową podróż przez serce Gdańska - miasta pełnego historii, tajemnic i niezwykłych miejsc.\n \
        Cztery dzielnice czekają na odkrycie, a każda z nich skrywa zagadki i wyzwania, które sprawdzą Waszą wiedzę, spryt i szczęście.")
        sleep_and_clear(12)
        print("         Czy uda Wam się zdobyć przewagę i dotrzeć do mety jako pierwszy?\n \
        Przygotuj się na super przygodę - czas zwiedzić Gdańsk i zapisać się w historii tego miasta!")
        sleep_and_clear(10)
        print("         Rozpoczynacie Waszą podróż w sercu Gdańska - na Starym Mieście.\n \
        Spacerując wśród historycznych kamienic i uliczek, poczujecie ducha przeszłości.\n \
        Stąd wyruszycie, odkrywając zarówno urokliwe zakątki, jak i trudne pytania, które sprawdzą, jak dobrze znacie to miejsce.")
        sleep_and_clear(12)
        print("         Pamiętajcie, każda odpowiedź przybliża Was do zwycięstwa, ale bądźcie ostrożny - nie brakuje tu pułapek!\n \
        Powodzenia, podróżnicy!")
        sleep_and_clear(8)
        while True:
            print("...Stare Miasto...\n\n")
            self.make_players()
            print(f"\nSTART.{self.board.generate_board()}\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_movement_mechanics("Stare Miasto"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def level_2(self):
        print("         Gratulacje! Pierwszy poziom ukończony. Wszyscy gracze zostają przeniesieni do następnego poziomu.\n")
        print("         Wasza wędrówka prowadzi Was na Stare Przedmieście, dawną bramę Gdańska.\n \
        To tutaj zaczynały się historie kupców i rzemieślników, którzy budowali potęgę miasta.\n \
        Wśród malowniczych widoków i śladów przeszłości ukryte są kolejne wyzwania. ")
        sleep_and_clear(12)
        print("         Każdy krok może być decydujący - czy uda Wam się odnaleźć właściwą drogę?\n \
        Czas przekroczyć granice Starego Miasta i ruszyć ku nowym przygodom!")
        sleep_and_clear(8)
        while True:
            print("...Stare Przedmieście...\n\n")
            self.make_players()
            print(f"\nSTART.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_movement_mechanics("Stare Przedmieście"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def level_3(self):
        print("         Gratulacje! Drugi poziom ukończony. Wszyscy gracze zostają przeniesieni do następnego poziomu.\n")
        print("         Witajcie w Oliwie, miejscu pełnym zieleni i harmonii.\n \
        To dzielnica znana z pięknych parków i monumentalnej katedry, gdzie historia miesza się z ciszą i spokojem.\n \
        Ale nie dajcie się zwieść tej sielance - Oliwa skrywa wyzwania, które potrafią zaskoczyć nawet najtwardszych graczy.")
        sleep_and_clear(12)
        print("         Czy uda Wam się przejść przez te tereny, nie tracąc przewagi? Czas pokaże!\n \
        Niech Oliwa odsłoni przed Waszą swoje tajemnice.")
        sleep_and_clear(8)
        while True:
            print("...Oliwa...\n\n")
            self.make_players()
            print(f"\nSTART.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n  \
        {self.board.generate_board()} \n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.META\n")

            if not self.level_movement_mechanics("Oliwa"):
                return False
            if self.next_level_movement_mechanics():
                return True

    def level_4(self):
        print("         Gratulacje! Trzeci poziom ukończony. Wszyscy gracze zostają przeniesieni do następnego poziomu.\n")
        print("         Docieracie do Wrzeszcza - serca nowoczesnego Gdańska, gdzie historia spotyka współczesność.\n \
        To tutaj, w tętniącym życiem centrum, Wasze umiejętności zostaną wystawione na ostatnią próbę.\n \
        Zgiełk miasta nie pozwala się zatrzymać, a każdy krok może zadecydować o Waszym sukcesie.")
        sleep_and_clear(12)
        print("         Czy uda Wam się dotrzeć do mety? Wrzeszcz czeka na śmiałków, którzy odważą się zmierzyć z jego wyzwaniami!")
        sleep_and_clear(6)
        while True:
            print("...Wrzeszcz...\n\n")
            self.make_players()
            print(f"\nSTART.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.\n \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        ____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____.____. \n  \
        {self.board.generate_board()}.META\n")

            if not self.final_level_movement_mechanics("Wrzeszcz"):
                return False
            if self.next_level_movement_mechanics():
                return True
            
    def finish(self):
        self.make_players()
        self.end_game_and_save() 
        sleep_and_clear(0)
        winner = max(self.player_data, key=lambda player: player[2])
        print(f"         Gratulacje {winner[1]}, zostałeś zwycięzcą!\n \
        Wasza podróż przez Gdańsk dobiegła końca, a Ty triumfujesz jako zwycięzca tej niezwykłej przygody!\n \
        Poznałeś cztery dzielnice miasta, zmierzyłeś się z pytaniami\n \
        i wyzwaniami, a teraz Twoje imię zapisze się w historii 'Tour De Gdańsk'.")
        sleep_and_clear(12)
        print("         Gdańsk dziękuje Ci za odwiedziny - kto wie, może wkrótce wrócisz na nowe szlaki?\n \
        Do zobaczenia!")
        sleep_and_clear(6)
        
        for i in self.player_data:
            print(i)
        sleep_and_clear(5)
        return False