import csv
class CsvWriter:
    def write_to_csv(self, player_data: list):
        with open('ranking.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Data", "Kolor i Nazwa", "Wynik"])
            writer.writerow(player_data)  # Dodajemy dane gracza

    def sort_csv_by_column(self)->list:
        try:
            with open('ranking.csv', 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = list(reader)

            if not data:  # Jeśli brak danych
                print("Plik jest pusty, brak danych do sortowania.")
                return

            sorted_data = sorted(data, key=lambda row: int(row["Wynik"]), reverse=True)

            with open('ranking.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=["Data", "Kolor i Nazwa", "Wynik"])
                writer.writeheader()
                writer.writerows(sorted_data)
        except Exception as e:
            print(f"Wystąpił błąd podczas sortowania: {e}")
