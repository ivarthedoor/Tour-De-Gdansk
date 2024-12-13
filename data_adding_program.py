import csv



# Lista danych
# player = ["\U0001F535", "chomik", 12]
# player1 = ['blue', 'Ivar', 40]
# player2 = ['red', 'Przemo', 15]
# player3 = ['green', 'Olek', 20]
# player4 = ['yellow', 'Jan', 35]

# Funkcja do zapisania danych do pliku CSV (na początek)
class CsvWriter:
    def write_to_csv(self, player_data):
        with open('ranking.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Dodajemy nagłówki tylko raz, jeśli plik jest pusty
            if file.tell() == 0:
                writer.writerow(["Nazwa", "Wynik"])  # Nagłówki
            writer.writerow(player_data)  # Dodajemy dane gracza

    def sort_csv_by_column(self):
        try:
            with open('ranking.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)

            if not data:  # Jeśli brak danych
                print("Plik jest pusty, brak danych do sortowania.")
                return

            sorted_data = sorted(data, key=lambda row: int(row["Wynik"]), reverse=True)

            with open('ranking.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["Nazwa", "Wynik"])
                writer.writeheader()
                writer.writerows(sorted_data)
        except Exception as e:
            print(f"Wystąpił błąd podczas sortowania: {e}")





    # write_to_csv()
    # sort_csv_by_column()

