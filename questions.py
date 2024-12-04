import random 
import main_functions

# ABCD
def abcd_question1():
    print("Konkatedralna Bazylika Mariacka zwana często „Koroną Gdańska” jest największą w Europie świątynią wybudowaną z cegły. \
          \nPotężne jej mury i wieże wznoszą się wysoko nad panoramą miasta oraz nad rozległą okolicą. \
          \n \
          \nW którym roku rozpoczęto budowę Bazyliki Mariackiej? \
          \n- a - 1285 \
          \n- b - 1343 \
          \n- c - 2003 \
          \n- d - 867")
    year = int(input("Odpowiedź: "))
    if year == 'b':
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!")
        return False

def abcd_question2():
    print("W 1549 przed Dworem Artusa istniała bliżej nieznana studnia, być może już z metalowymi dekoracjami.  \
           \nMowa o słynnej późniejszej fontannie Neptuna. \
          \n \
          \nCzy wiesz w którym roku ukończono jej budowę? \
          \n- a - 1776 \
          \n- b - 1822 \
          \n- c - 1633 \
          \n- d - 764 p.n.e.")
    year = int(input("Odpowiedź: "))
    if year == 'c':
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!")
        return False

def abcd_question3():
    print("Kuźnia Wodna to zabytek dawnej techniki, jedyny tego typu zachowany do dziś. \
          \nTo największa i najdłużej pracująca z młotowni oliwskich. \
          \nFunkcjonowała przez ok. 350 lat wykorzystując siłę spiętrzonych wód Potoku Oliwskiego. \
          \n \
          \nZ którego roku pochodzi pierwsza wzmianka na temat tejże kuźni? \
          \n- a - 1597 \
          \n- b - 1800 \
          \n- c - 1112 \
          \n- d - 1438")
    year = int(input("Odpowiedź: "))
    if year == 1597:
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!")
        return False

def abcd_question4():
    print("Dwór Artusa gmach usytuowany w centrum Gdańska, przy Długim Targu 44, dawniej miejsce spotkań kupców, \
          \nośrodek życia towarzyskiego, później giełda, obecnie oddział Muzeum Gdańska. \
          \nPełni rolę obiektu recepcyjnego miasta. \
          \n \
          \nW którym roku ukończono budowę pierwotnego Gdańskiego Dworu Artusa? \
          \n- a - 1567 \
          \n- b - 1481 \
          \n- c - 1914 \
          \n- d - 1474")
    year = int(input("Odpowiedź: "))
    if year == 1481:
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!") 
        return False

def abcd_question5():
    print("Brama Wyżynna, dawniej także „Brama Wysoka”. Renesansowa brama miejska w Gdańsku. \
          \nDo 1895 znajdowała się w ciągu szesnastowiecznych fortyfikacji, pomiędzy Bastionem św. Elżbiety i Bastionem Karowym \
          \noraz stanowiła główną bramę wjazdową do miasta, otwierającą ciąg tzw. Drogi Królewskiej. \
          \n \
          \nW którym roku ukończono budowę Bramy Wyżynnej? \
          \n- a - 1475 \
          \n- b - 1575 \
          \n- c - 1675 \
          \n- d - 1775")
    year = int(input("Odpowiedź: "))
    if year == 1575:
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!") 
        return False

def abcd_question6(): #oliwa
    print("Początkiem dzisiejszego parku był przyklasztorny ogród założony przez zakonników. \
          \nPrawdopodobnie był położony po wschodniej stronie starej siedziby opatów z XV wieku, \
          \ndalej do Zatoki Gdańskiej rozciągał się nadmorski las, który rozcinał Potok Oliwski. \
          \nPo wzniesieniu przez opata Franciszka Zaleskiego pod koniec pierwszej połowy XVII wieku nowej siedziby opatów, \
          \nogród został poszerzony w kierunku południowo-zachodnim, stykając się ze starszym ogrodem klasztornym. \
          \n \
          \nO jakim zakonie mowa? \
          \n- a - Kapucynów \
          \n- b - Cystersów? \
          \n- c - Mnichów z Shaolin \
          \n- d - Franciszkanów \
          \n \
          \nPodaj dokładną odpowiedź od 1 do 4")
    answer = int(input("Odpowiedź: "))
    if answer == 2:
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!")
        return False

def abcd_question7():
    print("9 maja 1734 roku Gdańszczanie pokonali w bitwie szturmujące Górę Gradową wojska. \
          \nTo było największe zwycięstwo gdańskiego oręża w osiemnastym stuleciu i ważny epizod wojny o sukcesję polską, \
          \nw której potężne miasto wiernie stało przy legalnie obranym królu Stanisławie Leszczyńskim. \
          \n \
          \nCzyje wojska atakowały Gdańsk? \
          \n- a - Niemieckie \
          \n2.Filipińskie \
          \n3.Rosyjskie \
          \n4.Pruskie \
          \n \
          \nPodaj dokładną odpowiedź od 1 do 4")
    answer = int(input("Odpowiedź: "))
    if answer == 3:
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!")
        return False

def abcd_question8():
    print("Najstarsze materiały świadczące o znajomości tego kamienia i jego obróbce w rejonie Gdańska \
          \npochodzą z okresu 8 - 4 tys. lat p.n.e. i wiążą się z przypisywaną mu magiczną siłą. \
          \nWyrabiano wówczas dla potrzeb kultowych amulety - postaci zwierząt, figurki bóstw i herosów. \
          \n \
          \nO jaki kamień chodzi? \
          \n1.Opal \
          \n2.Agat \
          \n3.Bursztyn \
          \n4.Krzemień \
          \n \
          \nPodaj dokładną odpowiedź od 1 do 4")
    answer = int(input("Odpowiedź: "))
    if answer == 3:
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!")
        return False

def abcd_question9():
    print("Wyspa jest położona pomiędzy Motławą a jej przekopem - Nową Motławą. \
          \nLeży w centrum Śródmieścia, od wschodu połączona z Długimi Ogrodami poprzez Most Stągiewny, \
          \nod południa ze Starym Przedmieściem, od zachodu poprzez Most Krowi i Most Zielony z Głównym Miastem. \
          \nOd północy wyspa sąsiaduje z wyspą Ołowianką. \
          \nDodatkowo południowa część wyspy, na której składowano niegdyś towary łatwopalne, \
          \nzostała odcięta od głównej części wyspy poprzez powstały sztucznie Kanał Smolny. \
          \n \
          \nO jaką wyspę chodzi? \
          \n1.Sobieszewską \
          \n2.Ołowianka2 \
          \n3.Spichrzów \
          \n4.Wolin \
          \n \
          \nPodaj dokładną odpowiedź od 1 do 4")
    answer = int(input("Odpowiedź: "))
    if answer == 3:
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!")
        return False

def abcd_question10():
    print("Miasto Gdańsk, Wolne Miasto Gdańsk, Danzig... \
          \nGdańsk zawsze był nietypowym miastem, rządził się swoimi prawami, przez pewien okres był zupełnie niepodległy żadnym krajom. \
          \nOprócz niepodległości i przynależności do Polski, przez długi okres swojej historii był częścią jednak do innego kraju. \
          \n \
          \nO jaki kraj chodzi? \
          \n1.Niemcy \
          \n2.Lichtenstein \
          \n3.Rosja \
          \n4.Szwecja \
          \n \
          \nPodaj dokładną odpowiedź od 1 do 4")
    answer = int(input("Odpowiedź: "))
    if answer == 1:
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!")
        return False

# Tak lub nie 


def tf_question1():
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

def tf_question2():
    final_value = True
    print("Czy miasto Gdańsk posiada tytuł Smart City?")
    answear = int(input("Podaj odpowedż: "))
    if answear == "tak" or "Tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question3():
    final_value = True
    print("Czy Adam Kazimierz Czartoryski urodził się w Gdańsku?")
    answear = int(input("Podaj odpowuiedź: "))
    if answear == "tak" or "Tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question4():
    final_value = True
    print("Czy niemieckojęzyczny fizyk i inżynier, holenderskiego pochodzenia, wynalazca termometru rtęciowego Daniel Gabriel Fahrenheit zmarł w Gdańśku?")
    answear = int(input("Podaj odpowiedź: "))
    if answear == "Nak" or "nie":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question5():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question6():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question7():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question8():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question9():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question10():
    final_value = True
    print("treść pytania")
    answear = int(input("odpowedż"))
    if answear == "":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value

# Matematyczne
def math_question1():
    print("To chyba jakiś wzór matematyczny")
    main_functions.sleep_and_clear(6)
    print("Gdy to obliczymy dowiemy się o roku budowy żurawia")
    print("72*(2*2)+12*(2**2)+((800/4)+44)")
    answear = int(input("to chyba  "))
    if answear == 1444:
        print("TAK jest!! udało się!!!")
    else:
        print("Kurcze coś jest nie tak!")



# Wywoływanie różnych pytań (ABCD, tak/nie, matematyczne)
def abcd_questions():
    abcd_question_list = [abcd_question1, abcd_question2,abcd_question3, abcd_question4, abcd_question5, \
                          abcd_question6, abcd_question7, abcd_question8, abcd_question9, abcd_question10]
    abcd_random_question = random.choice(abcd_question_list)
    return abcd_random_question()

    
# def true_or_false():
#     tf_question_list = [tf_question1, tf_question2, tf_question3, tf_question4, tf_question5, \
#                           tf_question6, tf_question7, tf_question8, tf_question9, tf_question10]
#     tf_question = random.choice(tf_question_list)
#     return tf_question()
    

# def math_questions():
#     math_question_list = [math_question1, math_question2, math_question3, math_question4, math_question5, \
#                           math_question6, math_question7, math_question8, math_question9, math_question10]
#     math_random_question = random.choice(math_question_list)
#     return math_random_question()


