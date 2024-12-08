import json
from random import randint

with open ('questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)


def questions_dispenser():
    tf_q = []
    for i in questions:
        if i["district"] == "Stare miasto":
            tf_q.append(i)

    rand_int = randint(0, len(tf_q))

    selected_question = questions[rand_int]
    if selected_question['type'] == 'tf':
        print("Wylosowane pytanie:")
        print(selected_question["question"])
    # print(selected_question["description"])
        print("Odpowiedz tak lub nie")
    else:
        print("Wylosowane pytanie:")
        print(selected_question["question"])
        print(selected_question["options"])!!!!!!!!!!!!!!!!!!!!!!!!!!

"""Trzeba dopisać inputa dla juzera i porównać go 

"""


