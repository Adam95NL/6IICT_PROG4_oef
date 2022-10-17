""" Opdracht:
Bekijk machten.csv. In dit bestand zijn drie kolommen gegeven:
    - basis: Getallen van 1 tot en met 10.
    - kwadraat: Het kwadraat van de linksgelegen basisgetallen.
    - derdemacht: De derdemacht van de linksgelegen basisgetallen.
    OPGELET: dit bestand gebruikt komma als scheidingsteken, geen punt-komma.

Momenteel zijn enkel de kolommen basis en kwadraat ingevuld.
De opdracht is als volgt:
    1) Open machten.csv in Python. Print iedere rij van de bekomen tabel. 
    2) Vul de kolom derdemacht aan in deze tabel. 
    3) Schrijf de verwerkte tabel weg naar een nieuw bestand. BVB. machten_verwerkt.csv.
OPGELET: Het verwerkte CSV-bestand moet komma's gebruiken als scheidingsteken. 

Puntenverdeling: (  / 5)
    1) Open en print machten.csv in Python (  / 1).
    2) Vul de kolom derdemacht aan in Python (  / 1).
    3) Schrijf de verwerkte tabel weg naar een nieuw bestand (  / 1).
    4) Schrijf bij iedere regel code commentaar die uitlegt wat je doet ( / 1).
    5) De ingeleverde code bevat geen foutmeldingen (  / 1).
      OPGELET: Voor onderdelen 1, 2 en 3 kijk ik enkel naar code die NIET in commentaar staat.
"""

import csv #importeer csv
fp = open( "hfst_1/machten.csv", "r" ) # open het bestand hfst_1/machten.csv en we gaan het bestand lezen
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen
csv_reader = csv.reader( fp , delimiter=",") #variable csv_reader is gelijk aan csv reader het wordt afgescheiden met ,

eruptions_ll = [] # lege lijst eruptions_11  
for rij in csv_reader: # doorloop rij in csv_reader
    eruptions_ll.append(rij)#voeg rij toe aan eruptions_ll
    print(rij)#print rij die zijn doorlopen
fp.close() # Na sluiten is CSV niet meer bruikbaar

eruptions_ll_verwerkt = []#lege lijst eruptions_ll_verwerkt

for index, rij in enumerate(eruptions_ll):#doorloop alle index en rijen en tel de eruptions_ll
    if index == 0:# als de index gelijk is aan 0 dan
        eruptions_ll_verwerkt.append([rij[0],rij[1],rij[2]])#append de rijen naar eruptions_ll_verwerkt 
        print(rij)#print de doorgelopen rij
    else:#als de bovenstaande waarde niet van toepassing is dan
        rij[2] = int(rij[0])**3 # de 2 de rij is de derde macht van de basisrij
        eruptions_ll_verwerkt.append([rij[0],rij[1],rij[2]])#voeg de rijen  toe aan eruptions_ll_verwerkt
        print(rij)#print de doorgelopen rijen
fp = open( "toets.csv", "w", newline="")# open een bestand genaamd toets.csv en we gaan erin writen de "" wordt gekenmerkt door een nieuwe lijn
csv_writer = csv.writer( fp , delimiter=",") # csv writer gaat schrijven in de variable fp en de scheidingtekens zijn de komma

for rij in eruptions_ll_verwerkt:#doorlop alle rijen in eruptions_ll_verwerkt
    csv_writer.writerow(rij)#csv writer schrijft per rij de deerlopen rijen

fp.close() # Na sluiten is CSV niet meer bruikbaar