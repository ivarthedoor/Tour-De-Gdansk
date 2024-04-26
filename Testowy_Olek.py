from random import randint

# Funkcje
# Funkcje true_or_false 10 szt
# Odpowiedzi tak lub nie 

def question1():
    final_value = True
    print("Czy Zoo w Gdańsku jest największym zoo w Polsce?")
    answear = int(input("Podaj odpowiedź: "))
    if answear == "Tak" or "tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna")
        final_value = False
    return final_value 

def question2():
    final_value = True
    print("Czy miasto Gdańsk posiada tytuł Smart City?")
    answear = int(input("Podaj odpowedż: "))
    if answear == "tak" or "Tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def question3():
    final_value = True
    print("Czy Adam Kazimierz Czartoryski urodził się w Gdańsku?")
    answear = int(input("Podaj odpowuiedź: "))
    if answear == "tak" or "Tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def question4():
    final_value = True
    print("Czy niemieckojęzyczny fizyk i inżynier, holenderskiego pochodzenia, wynalazca termometru rtęciowego Daniel Gabriel Fahrenheit zmarł w Gdańśku?")
    answear = int(input("Podaj odpowiedź: "))
    if answear == "Nak" or "nie":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def question5():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def question6():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def question7():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def question8():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def question9():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def question10():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value



#########################################################



def true_or_false():
    number = randint(1, 10)
    if number == 1:
        return question1()
    elif number == 2:
        return question2()
    elif number == 3:
        return question3()
    elif number == 4:
        return question4()
    elif number == 5:
        return question5()
    elif number == 6:
        return question6()
    elif number == 7:
        return question7()
    elif number == 8:
        return question8()
    elif number == 9:
        return question9()
    else:
        return question10
