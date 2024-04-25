from random import randint
#Funkcje
#Funkcje true_or_false 10szt

def true_or_false1():
    final_value = True
    print("W którym roku rozpoczęto budowę Bazyliki Mariackiej, znajdującej się na ulicy Podkramarskiej?")
    year = int(input("Odpowiedź: "))
    if year == 1343:
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!") #Jeżeli True gracz idzie dalej, jeżeli False gracz czeka kolejkę.
        final_value = False
    return final_value


def true_or_false2():
    final_value = True
    print("W 1549 przed Dworem Artusa istniała bliżej nieznana studnia, być może już z metalowymi dekoracjami.  \
           \nMowa o słynnej fontannie Neptuna. Czy wiesz w którym roku ukończono jej budowę?")
    year = int(input("Odpowiedź: "))
    if year == 1633:
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!") #Jeżeli True gracz idzie dalej, jeżeli False gracz czeka kolejkę.
        final_value = False
    return final_value


# def true_or_false4(year):

# def true_or_false5(year):

# def true_or_false6(year):

def true_or_false7():
    final_value = True
    print("Początkiem dzisiejszego parku był przyklasztorny ogród założony przez zakonników. \
          \nPrawdopodobnie był położony po wschodniej stronie starej siedziby opatów z XV wieku, \
          \ndalej do Zatoki Gdańskiej rozciągał się nadmorski las, który rozcinał Potok Oliwski. \
          \nPo wzniesieniu przez opata Franciszka Zaleskiego pod koniec pierwszej połowy XVII wieku nowej siedziby opatów, \
          \nogród został poszerzony w kierunku południowo-zachodnim, stykając się ze starszym ogrodem klasztornym. \
          \n \
          \n \
          \n \
          \nO jakim zakonie mowa? Kapucynów, czy Cystersów? \
          \nPodaj dokładną odpowiedź")
    answer = input("Odpowiedź: ")
    if answer == "Cystersów" or "cystersów" or "Cystersow" or "cystersow":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
        final_value = False
    return final_value

true_or_false7()

# def true_or_false8(answer):

# def true_or_false9(answer):

# def true_or_false10(answer):

# def true_or_false11(answer):






# def t_o_fy():
#     number = randint(1, 2)
#     if number == 1:
#         return true_or_false1()
#     else:
#         return true_or_false2()

# t_o_fy()
