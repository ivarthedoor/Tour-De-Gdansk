ascii = """
------WYNIKI------
     _\U0001F535_
    |    |_\U0001F534_
    |    |    |_\U0001F7E2_
    |    |    |    |_\U0001F7E1_
    |    |    |    |    |
"""


# ["\U0001F535", "\U0001F534", "\U0001F7E2", "\U0001F7E1"]
# print(ascii)




lista = [x for x in enumerate(["Paweł", "Robert", "Damian", "Cyprian"], start=1)]
for i in range(len(lista)):
    a, b = lista[i]
    print(f"{a}.{b}")