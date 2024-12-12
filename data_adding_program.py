import csv

# Lista danych
player = ["\U0001F535", "chomik", 12]
player1 = ['blue', 'kameleon', 14]
player2 = ['red', 'kaon', 116]
player3 = ['bl', 'kamele', 20]
player4 = ['blu', 'kamn', 39]

# Funkcja do zapisania danych do pliku CSV (na początek)
def write_to_csv():
    with open('ranking.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Kolor", "Nazwa", "Wartość"])  # Nagłówki
        writer.writerow(player)  # Dodajemy dane
        writer.writerow(player1)
        writer.writerow(player2)
        writer.writerow(player3)
        writer.writerow(player4)

# Funkcja sortująca dane w pliku CSV
def sort_csv_by_column():
    # Wczytaj dane z pliku CSV
    with open('ranking.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)  # Konwertuj na listę słowników
    
    # Posortuj dane według kolumny 'Wartość' (należy przekształcić na int)
    sorted_data = sorted(data, key=lambda row: int(row['Wartość']), reverse=True)  # Sortowanie malejąco
    
    # Zapisz posortowane dane z powrotem do pliku CSV
    with open('ranking.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()  # Zapisz nagłówki kolumn
        writer.writerows(sorted_data)  # Zapisz posortowane wiersze
write_to_csv()
sort_csv_by_column()
