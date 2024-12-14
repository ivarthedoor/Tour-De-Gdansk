import csv

def showing_ranking():
    with open('ranking.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    for i in data:
        print(i)