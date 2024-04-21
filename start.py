'''
Grupa2 CodeGDA
Pomysł na program: Gra planszowa Tour De Gdańsk
Założenia:
    -plansza ciąg pól 1-100
    -celem jest doście do ostatniego pola, na zasadzie rzutu jedną kością 1-6, oraz pokonanie zadań
    -ranking
Fabuła: Wycieczka po Gdańsku. Na poszczególnych polach będą sie znajdowały zabytki Gdańska i przypisane do nich zadania
    (pomysły niżej)
Pomysły na pola zadaniowe:
    -zadanie matematyczne - wynik= rok danego zabytku na tym polu
    -więzienie (pechowe pole lub przy 3 błędnych odpowiedziach) 3 tury!
    -LUCKY THROW - skok o kolejną liczbę wylisowanych pól (idziesz do przodu o tyle samo oczek ile wylosowałeś przed
     wejściem na to pole)
    -po przekroczeniu odpowiedniego etapu ilość pól cofania się jest zmniejszona o połowę (zaokrąglane do góry)
    -papier/kamień/nozyce (pechowe pole)
    -zgadywanka True or False (pytania z wiedzy o Gdańsku) (tak lub nie))
    -zgadywanie liczb, za którym razem odgadniesz liczbę, to tyle pól przesówasz się w przód
    -zgadywanie liczb, za którym razem odgadniesz liczbę, to tyle pól przesówasz się w w tył
    -pole z grą w wisielca (wygyrwasz + 10 pól, przegrywasz -10)
    -Pytania w stylu, gdzie znajduje się dany zabytek (odpowiedź pełnym słowem)
    -
    -
    -
    -
    -
Programy przypisane do pól: do danego pola przypisany jest dany rodzaj zadania, zadania będą losowane ze zbioru lub
     przypisane na sztywno do pola
'''
#Typowanie graczy
x = 1
players = {"position": None, "number": x, "color": "green"}

green = "green"
yellow = "yellow"
blue = "blue"
red = "red"

def make_players(colors):
    players = []
    for color in colors:
        for i in range(1):
            players.append ({
                "position": None,
                "number": x,
                "color": color
            })

    return players

players = make_players([green, yellow, blue, red])
for player in players:
    print(player)  #"test"

#Sprwadzam Ivar
