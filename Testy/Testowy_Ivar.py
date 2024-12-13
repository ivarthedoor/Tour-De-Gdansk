from datetime import datetime

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



from datetime import datetime

# Aktualna data i czas z formatowaniem
aktualna_data = datetime.now()
sformatowana_data = aktualna_data.strftime("%Y-%m-%d %H:%M:%S")
print(sformatowana_data)  # Wyjście: "2024-12-13 14:30:45"



