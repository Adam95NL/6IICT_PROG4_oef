import csv
""" Oefening 2 (  / 4)
Bekijk kerst_oefening2.csv. Het bevat de scores die juryleden (rij 1) hebben gegeven in een wedstrijd.
Er waren in totaal 5 deelnemers die beoordeeld zijn (rij 2-6).

In de volgende stappen zal je dit bestand inlezen, verwerken en wegschrijven.
Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" STAP 1:
Lees kerst_oefening2.csv in, in een variabele van Python. 
"""
fp = open( "kerstexamen_deel1\kerst_oefening2/kerst_oefening2.csv", "r" )#open het csv bestand met lees modus
csv_reader = csv.reader( fp , delimiter=",")#gebruik de functie csv.reader om het bestand te lezen
eruptions_ll = [] # lege lijst eruptions_11

for rij in csv_reader: # doorloop rij in csv_reader
    eruptions_ll.append(rij)#voeg rij toe aan eruptions_ll
fp.close() # Na sluiten is CSV niet meer bruikbaar
""" STAP 2:
print voor IEDERE deelnemer zijn scores af. 

VOORBEELD (jou print hoeft niet exact hetzelfde te zijn):
    Deelnemer 1 kreeg volgende scores: 9, 8, 9, 10
    ...
    Deelnemer 5 kreeg volgende scores: 7, 4, 6, 7
"""
eruptions_ll_verwerkt = [] # lege lijst eruptions_11_verwerkt
for index, rij in enumerate(eruptions_ll):#doorloop alle index en rijen en tel de eruptions_ll
    if index == 0:# als de index gelijk is aan 0 dan
        eruptions_ll_verwerkt.append([rij[0],rij[1],rij[2], rij[3]])#append de rijen naar eruptions_ll_verwerkt 
    else:#als de bovenstaande waarde niet van toepassing is dan
        eruptions_ll_verwerkt.append([rij[0],rij[1],rij[2], rij[3]])#append de rijen naar eruptions_ll_verwerkt 
        print(f"deelnemer {index} kreeg  {rij}")#print de tekst met de variable die tussen accolades staat
        

""" STAP 3: 
Bereken voor iedere deelnemer de gemiddelde score. 
    Tip: Ieder element in een CSV-bestand is een string. Zet deze eerst om, vooraleer iets te berekenen.

Lukt dit niet?
    Je zult de gemiddelde score nodig hebben voor stap 4. 
    Bereken de gemiddelde score van iedere persoon manueel en voeg deze zelf toe aan de code (bvb. in een lijst).
    Doe je dit, dan krijg je geen punten op STAP 3.
"""
eruptions_ll2 = [] #lege lijst 
gemiddeldecijfers = [] #lege lijst
for index, rij in enumerate(eruptions_ll):#doorloop alle index en rijen en tel de eruptions_ll
    if index == 0:# als de index gelijk is aan 0 dan
        eruptions_ll2.append([rij[0],rij[1],rij[2],rij[3]])#append de rijen naar eruptions_ll2 
    else:#als de bovenstaande waarde niet van toepassing is dan
        getal_1 = int(rij[0]) # getal_1 is een integer op rij 0
        getal_2 = int(rij[1]) # getal_2 is een integer op rij 1
        getal_3 = int(rij[2]) # getal_3 is een integer op rij 2
        getal_4 = int(rij[3]) # getal_4 is een integer op rij 3
        gem = (getal_1 + getal_2 + getal_3 +getal_4) /4 #gemiddelde zijn alle getaln bij elkaar gedeeld door 4
        gemiddeldecijfers.append(gem) #print de gemmidelde naar de lijst gemiddeldecijfers
print(gemiddeldecijfers)#print de lijst gemiddeldecijfers

""" STAP 4:
Maak een nieuw bestand kerst_oefening2_verwerkt.csv aan. Dit bestand bevat alle kolommen van kerst_oefening2.csv.
Voeg er nog een nieuwe kolom aan toe. Deze bevat de gemiddelde score van iedere deelnemer (bepaald in STAP 3).

Een voorbeeld van het resultaat is te vinden in kerst_voorbeeld2.csv
"""


