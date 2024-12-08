import random 

# ABCD
def abcd_question1():
    print("Konkatedralna Bazylika Mariacka zwana często „Koroną Gdańska” jest największą w Europie świątynią wybudowaną z cegły. \
          \nPotężne jej mury i wieże wznoszą się wysoko nad panoramą miasta oraz nad rozległą okolicą. \
          \n \
          \nW którym roku rozpoczęto budowę Bazyliki Mariackiej? \
          \na. 1285 \
          \nb. 1343 \
          \nc. 2003 \
          \nd. 867")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "B" or "b":
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
          \na. 1776 \
          \nb. 1822 \
          \nc. 1633 \
          \nd. 764 p.n.e.")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "C" or "c":
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
          \na. 1597 \
          \nb. 1800 \
          \nc. 1112 \
          \nd. 1438")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "A" or "a":
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
          \na. 1567 \
          \nb. 1481 \
          \nc. 1914 \
          \nd. 1474")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "B" or "b":
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
          \na. 1475 \
          \nb. 1575 \
          \nc. 1675 \
          \nd. 1775")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "B" or "b":
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
          \na. Kapucynów \
          \nb. Cystersów \
          \nc. Mnichów z Shaolin \
          \nd. Franciszkanów")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "B" or "b":
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
          \na.Niemieckie \
          \nb.Filipińskie \
          \nc.Rosyjskie \
          \nd.Pruskie")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "C" or "c":
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
          \na.Opal \
          \nb.Agat \
          \nc.Bursztyn \
          \nd.Krzemień")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "C" or "c":
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
          \na.Sobieszewską \
          \nb.Ołowianka2 \
          \nc.Spichrzów \
          \nd.Wolin")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "C" or "c":
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
          \na.Niemcy \
          \nb.Lichtenstein \
          \nc.Rosja \
          \nd.Szwecja")
    answer = str(input("Odpowiedz: a, b, c lub d"))
    if answer == "A" or "a":
        print("Odpowiedź jest poprawna!")
        return True
    else:
        print("Odpowiedź jest błędna!")
        return False

# Tak lub nie 


def tf_question1():
    final_value = True
    print("Czy Zoo w Gdańsku jest największym zoo w Polsce?")
    answear = str(input("odpowiedz: tak lub nie"))
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
    answear = str(input("odpowiedz: tak lub nie"))
    if answear == "tak" or "Tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question3():
    final_value = True
    print("Czy Adam Kazimierz Czartoryski urodził się w Gdańsku?")
    answear = str(input("odpowiedz: tak lub nie"))
    if answear == "tak" or "Tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question4():
    final_value = True
    print("Czy niemieckojęzyczny fizyk i inżynier, holenderskiego pochodzenia, wynalazca termometru rtęciowego Daniel Gabriel Fahrenheit zmarł w Gdańśku?")
    answear = str(input("odpowiedz: tak lub nie"))
    if answear == "Nie" or "nie":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question5():
    final_value = True
    print("Czy Gdańsk był kiedyś częścią Hanzy, czyli związku miast handlowych Europy Północnej?")
    answear = str(input("odpowiedz: tak lub nie"))
    if answear == "Tak" or "tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question6():
    final_value = True
    print("Czy Fontanna Neptuna w Gdańsku została zbudowana w XIX wieku?")
    answear = str(input("odpowiedz: tak lub nie"))
    if answear == "Nie" or "nie":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question7():
    final_value = True
    print("Czy w Gdańsku znajduje się najdłuższy w Europie kościół z cegły?")
    answear = str(input("odpowiedz: tak lub nie"))
    if answear == "Tak" or "tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question8():
    final_value = True
    print("Czy w Gdańsku powstała pierwsza na świecie poczta morska?")
    answear = str(input("odpowiedz: tak lub nie"))
    if answear == "Tak" or "tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question9():
    final_value = True
    print("Czy Westerplatte było miejscem rozpoczęcia II wojny światowej?")
    answear = str(input("odpowiedz: tak lub nie"))
    if answear == "Tak" or "tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value


def tf_question10():
    final_value = True
    print("Czy Gdańsk był jednym z miast, w których narodził się ruch Solidarność?")
    answear = str(input("odpowiedz: tak lub nie"))
    if answear == "Tak" or "tak":
        print("Odpowiedź jest poprawna!")
        final_value = True
    else:
        print("Odpowiedź jest błędna!")
    return final_value



# Wywoływanie różnych pytań (ABCD, tak/nie)
def abcd_questions():
    abcd_question_list = [abcd_question1, abcd_question2,abcd_question3, abcd_question4, abcd_question5, \
                          abcd_question6, abcd_question7, abcd_question8, abcd_question9, abcd_question10]
    abcd_random_question = random.choice(abcd_question_list)
    return abcd_random_question()

    
def true_or_false():
    tf_question_list = [tf_question1, tf_question2, tf_question3, tf_question4, tf_question5, \
                          tf_question6, tf_question7, tf_question8, tf_question9, tf_question10]
    tf_question = random.choice(tf_question_list)
    return tf_question()


