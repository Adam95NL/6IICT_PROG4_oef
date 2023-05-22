import random

class Hond:
    locaties = ["living", "tuin", "buren","keuken"]
    def __init__(self, naam, locatie):
        self.naam = naam
        self.locatie = locatie

    def ziet_hond(self, andere_hond):
        if self.locatie == andere_hond.locatie:
            print(f"{self.naam} ziet {andere_hond.naam} in de {self.locatie}.")

            gekozen = random.choice([self,andere_hond])
            gekozen.locatie = random.choice(self.locaties)
            print(f"{gekozen.naam} is bang en rent naar de {self.locatie}.")
        else:
            print(f"{self.naam} ziet geen hond in de/het {self.locatie}.")

hond_1 = Hond("Lulu","keuken")
hond_2 = Hond("Floris","keuken")
hond_3 = Hond("Ranger","tuin")

hond_1.ziet_hond(hond_2)
hond_1.ziet_hond(hond_3)
print(hond_1.locatie)
