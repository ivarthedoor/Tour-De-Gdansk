from random import randint
#Funkcje
#Funkcje question 10szt

def question1():
    final_value = True
    print("Konkatedralna Bazylika Mariacka zwana często „Koroną Gdańska” jest największą w Europie świątynią wybudowaną z cegły. \
          \nPotężne jej mury i wieże wznoszą się wysoko nad panoramą miasta oraz nad rozległą okolicą. \
          \n \
          \nW którym roku rozpoczęto budowę Bazyliki Mariackiej? \
          \n-1285 \
          \n-1343 \
          \n-2003 \
          \n-867")
    year = int(input("Odpowiedź: "))
    if year == 1343:
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
        final_value = False
    return final_value #Jeżeli True gracz idzie dalej, jeżeli False gracz czeka kolejkę.

def question2():
    final_value = True
    print("W 1549 przed Dworem Artusa istniała bliżej nieznana studnia, być może już z metalowymi dekoracjami.  \
           \nMowa o słynnej późniejszej fontannie Neptuna. \
          \n \
          \nCzy wiesz w którym roku ukończono jej budowę? \
          \n-1776 \
          \n-1822 \
          \n-1633 \
          \n-764 p.n.e.")
    year = int(input("Odpowiedź: "))
    if year == 1633:
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
        final_value = False
    return final_value

def question3():
    final_value = True
    print("Kuźnia Wodna to zabytek dawnej techniki, jedyny tego typu zachowany do dziś. \
          \nTo największa i najdłużej pracująca z młotowni oliwskich. \
          \nFunkcjonowała przez ok. 350 lat wykorzystując siłę spiętrzonych wód Potoku Oliwskiego. \
          \n \
          \nZ którego roku pochodzi pierwsza wzmianka na temat tejże kuźni? \
          \n-1597 \
          \n-1800 \
          \n-1112 \
          \n-1438")
    year = int(input("Odpowiedź: "))
    if year == 1597:
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
        final_value = False
    return final_value

def question4():
    final_value = True
    print("Dwór Artusa gmach usytuowany w centrum Gdańska, przy Długim Targu 44, dawniej miejsce spotkań kupców, \
          \nośrodek życia towarzyskiego, później giełda, obecnie oddział Muzeum Gdańska. \
          \nPełni rolę obiektu recepcyjnego miasta. \
          \n \
          \nW którym roku ukończono budowę pierwotnego Gdańskiego Dworu Artusa? \
          \n-1567 \
          \n-1481 \
          \n-1914 \
          \n-1474")
    year = int(input("Odpowiedź: "))
    if year == 1481:
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!") 
        final_value = False
    return final_value

def question5():
    final_value = True
    print("Brama Wyżynna, dawniej także „Brama Wysoka”. Renesansowa brama miejska w Gdańsku. \
          \nDo 1895 znajdowała się w ciągu szesnastowiecznych fortyfikacji, pomiędzy Bastionem św. Elżbiety i Bastionem Karowym \
          \noraz stanowiła główną bramę wjazdową do miasta, otwierającą ciąg tzw. Drogi Królewskiej. \
          \n \
          \nW którym roku ukończono budowę Bramy Wyżynnej? \
          \n-1475 \
          \n-1575 \
          \n-1675 \
          \n-1775")
    year = int(input("Odpowiedź: "))
    if year == 1575:
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!") 
        final_value = False
    return final_value

def question6():
    final_value = True
    print("Początkiem dzisiejszego parku był przyklasztorny ogród założony przez zakonników. \
          \nPrawdopodobnie był położony po wschodniej stronie starej siedziby opatów z XV wieku, \
          \ndalej do Zatoki Gdańskiej rozciągał się nadmorski las, który rozcinał Potok Oliwski. \
          \nPo wzniesieniu przez opata Franciszka Zaleskiego pod koniec pierwszej połowy XVII wieku nowej siedziby opatów, \
          \nogród został poszerzony w kierunku południowo-zachodnim, stykając się ze starszym ogrodem klasztornym. \
          \n \
          \nO jakim zakonie mowa? \
          \n-Kapucynów \
          \n-Cystersów? \
          \n-Mnichów z Shaolin \
          \n-Franciszkanów \
          \n \
          \nPodaj dokładną odpowiedź")
    answer = input("Odpowiedź: ")
    if answer == "Cystersów" or "cystersów" or "Cystersow" or "cystersow":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
        final_value = False
    return final_value

def question7():
    final_value = True
    print("9 maja 1734 roku Gdańszczanie pokonali w bitwie szturmujące Górę Gradową wojska. \
          \nTo było największe zwycięstwo gdańskiego oręża w osiemnastym stuleciu i ważny epizod wojny o sukcesję polską, \
          \nw której potężne miasto wiernie stało przy legalnie obranym królu Stanisławie Leszczyńskim. \
          \n \
          \nCzyje wojska atakowały Gdańsk? \
          \n-Niemieckie \
          \n-Filipińskie \
          \n-Rosyjskie \
          \n-Pruskie \
          \n \
          \nPodaj dokładną odpowiedź")
    answer = input("Odpowiedź: ")
    if answer == "Rosyjskie" or "rosyjskie":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
        final_value = False
    return final_value

def question8():
    final_value = True
    print("Najstarsze materiały świadczące o znajomości tego kamienia i jego obróbce w rejonie Gdańska \
          \npochodzą z okresu 8 - 4 tys. lat p.n.e. i wiążą się z przypisywaną mu magiczną siłą. \
          \nWyrabiano wówczas dla potrzeb kultowych amulety - postaci zwierząt, figurki bóstw i herosów. \
          \n \
          \nO jaki kamień chodzi? \
          \n-Opal \
          \n-Agat \
          \n-Bursztyn \
          \n-Krzemień \
          \n \
          \nPodaj dokładną odpowiedź")
    answer = input("Odpowiedź: ")
    if answer == "Bursztyn" or "bursztyn":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
        final_value = False
    return final_value

def question9():
    final_value = True
    print("Wyspa jest położona pomiędzy Motławą a jej przekopem - Nową Motławą. \
          \nLeży w centrum Śródmieścia, od wschodu połączona z Długimi Ogrodami poprzez Most Stągiewny, \
          \nod południa ze Starym Przedmieściem, od zachodu poprzez Most Krowi i Most Zielony z Głównym Miastem. \
          \nOd północy wyspa sąsiaduje z wyspą Ołowianką. \
          \nDodatkowo południowa część wyspy, na której składowano niegdyś towary łatwopalne, \
          \nzostała odcięta od głównej części wyspy poprzez powstały sztucznie Kanał Smolny. \
          \n \
          \nO jaką wyspę chodzi? \
          \n-Sobieszewską \
          \n-Ołowianka2 \
          \n-Spichrzów \
          \n-Wolin \
          \n \
          \nPodaj dokładną odpowiedź")
    answer = input("Odpowiedź: ")
    if answer == "Spichrzów" or "spichrzów" or "Spichrzow" or "spichrzow":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
        final_value = False
    return final_value

def question10():
    final_value = True
    print("Miasto Gdańsk, Wolne Miasto Gdańsk, Danzig... \
          \nGdańsk zawsze był nietypowym miastem, rządził się swoimi prawami, przez pewien okres był zupełnie niepodległy żadnym krajom. \
          \nOprócz niepodległości i przynależności do Polski, przez długi okres swojej historii był częścią jednak do innego kraju. \
          \n \
          \nO jaki kraj chodzi? \
          \n-Niemcy \
          \n-Lichtenstein \
          \n-Rosja \
          \n-Szwecja \
          \n \
          \nPodaj dokładną odpowiedź")
    answer = input("Odpowiedź: ")
    if answer == "Niemcy" or "niemcy":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
        final_value = False
    return final_value








def questions():
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
