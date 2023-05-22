class Hond:
    def naam(self,naam):
        self.naam = naam
        print(f"{self.naam} ")
    
    def massa(zichzelf, massa):
        zichzelf.massa = massa
        print(f"{zichzelf.naam} weegt {zichzelf.massa} kilo")

hond = Hond()
hond.naam("eddy")
hond.massa(70)
