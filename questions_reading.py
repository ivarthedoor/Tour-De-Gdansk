import json

with open ('questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)

for i in questions:
    if i['type'] == 'tf':
        print(i)