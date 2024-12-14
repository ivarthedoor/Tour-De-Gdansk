import json
from random import randint

with open ('questions.json', 'r', encoding='utf-8') as file:
    questions = json.load(file)
class GameQuestions:
    def questions_dispenser(self, district):
        specific_district_questons_list = []
        for i in questions:
            if i["district"] == district:
                specific_district_questons_list.append(i)

        if not specific_district_questons_list:
            print("Brak pytań dla podanego rejonu.")
            return

        rand_int = randint(0, len(specific_district_questons_list) - 1)
        selected_question = specific_district_questons_list[rand_int]

        if selected_question['type'] == "ABCD":
            print(f"Wylosowane pytanie: {selected_question['question']}")
            user_input_abcd = input(f"{str("\n".join(selected_question['options']))}\n")
            answer = str(selected_question['correct_answer'])
            if user_input_abcd.lower() == answer.lower():
                print("Odpowiedź prawidłowa!")
                return True
            else:
                print(f"Niestety, nie trafiłeś... \n \
                Prawidłowa odpowiedź to {selected_question['correct_answer']}")
                return False
        else:
            print(f"Wylosowane pytanie: {selected_question['question']}")
            user_input_tf = input(str("Odpowiedz tak lub nie: "))
            answer = str(selected_question['correct_answer'])
            if user_input_tf.lower() == answer.lower():
                print("Odpowiedź prawidłowa!")
                return True
            else:
                print(f"Niestety, nie trafiłeś... \n \
                Prawidłowa odpowiedź to {selected_question['correct_answer']}")
                return False