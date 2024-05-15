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
    print(player)