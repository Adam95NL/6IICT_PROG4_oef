class Hond:
    def __init__(self, naam, massa):
        self.naam = naam
        self.massa = massa
        
    def roep(self):
        print(f"{self.naam} ")
    def weegschaal(self):
        print(f"{self.naam} weegt {self.massa}")
        

hond = Hond("eddy",90)
hond.roep()
hond.weegschaal()
