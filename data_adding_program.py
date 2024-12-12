import csv
from core import GameCore
from utiles import PLAYERS_POINTS


# Lista danych
# player = ["\U0001F535", "chomik", 12]
player1 = ['blue', 'Ivar', 40]
player2 = ['red', 'Przemo', 15]
player3 = ['green', 'Olek', 20]
player4 = ['yellow', 'Jan', 35]

# Funkcja do zapisania danych do pliku CSV (na początek)
class CsvWriter(GameCore):
    def __init__(self):
        super().__init__()
        self.game_core = GameCore()

    def write_to_csv(self):
        with open('ranking.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Nazwa", "Wynik"])  # Nagłówki
            writer.writerow(self.game_core.player_data)  # Dodajemy dane

    # Funkcja sortująca dane w pliku CSV
    def sort_csv_by_column(self):
        # Wczytaj dane z pliku CSV
        with open('ranking.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)  # Konwertuj na listę słowników
        
        # Posortuj dane według kolumny 'Wartość' (należy przekształcić na int)
        sorted_data = sorted(data, key=lambda row: int(row["Wynik"]), reverse=True)  # Sortowanie malejąco
        
        # Zapisz posortowane dane z powrotem do pliku CSV
        with open('ranking.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()  # Zapisz nagłówki kolumn
            writer.writerows(sorted_data)  # Zapisz posortowane wiersze





    write_to_csv()
    sort_csv_by_column()

