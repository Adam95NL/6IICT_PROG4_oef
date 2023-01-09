""" Oefening 1 (  / 2)
Maak onderstaande opdrachten over dictionaries.
Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" Opdracht 1:
Print voor IEDER element in onderstaande dictionary volgende tekst:
    <key> heb ik <value> uren per week

Voorbeeld:
    wisk heb ik 4 uren per week
    ...
    sph heb ik 2 uren per week
"""
vakken = {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2} # dit is de dictionary met de key en values
for key,value in vakken.items(): # doorloop de key en values in vakken.items
    print(f'het vak {key} heb ik {value} uur per week') #print in de fstring de opgeroepen namen

""" Opdracht 2:
Vraag de gebruiker naar een vak. Print het aantal uur dat dit vak voorkomt in de dictionary.
Als het ingegeven vak niet bestaat, print dan "vak bestaat niet".

VOORBEELD:
    Geef een vak op: wisk
    4

    Geef een vak op: huppel
    vak bestaat niet
"""
vakken = {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}# dit is de dictionary
vak = input("welk vak: ") # vak is de input die je zelf moet ingeven
if vak in vakken: # als vak in vakken is dan
    print(vakken[vak])#print het vak 
else:# als de voorwaarde niet van toepassing is 
    print("vak bestaat niet")# print dat de vak niet bestaat


""" Opdracht 3:
Schrijf een programma dat onderstaande 2 lijsten combineert in een dictionary.
print deze dictionary. Opgelet! Dit programma moet ook blijven werken als de lijsten wijzigen.
                                De lijsten zullen wel altijd evenveel elementen bevatten.

RESULTAAT: {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}
"""
namen = ["wisk", "prog", "cosn", "sph"]# de lijst namen met de vakken erin
uren = [4,4,2,2]# lijst met de uren
vakkensamen = {} # lege dit genaamd vakkensamen


for i in range(0,len(namen)):# doorloop alles tussen 0 en de lengte van de lijst
    vakkensamen[namen[i]] = uren[i] #stel de vakkensamen gelijk aan de uren i
print(vakkensamen)#print de vakkensamen


""" Opdracht 4:
Verander in onderstaande dictionary de key "error" naar "cosn". 
De volgorde van de dictionary hoeft niet hetzelfde te blijven. Print de dictionary. 

RESULTAAT: {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}
"""
vakken = {"wisk": 4, "prog": 4, "error": 2, "sph": 2}# dit is de dictionary met key en values

vakken["cosn"] = vakken.pop("error") # verander error met cosn dit poppen we

print(vakken)# print de dictionary vakken