import csv

class ShowRanking:
    def showing_ranking(self):
        with open('ranking.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        for i in data:
            print(i)