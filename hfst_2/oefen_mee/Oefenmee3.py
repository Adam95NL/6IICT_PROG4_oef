import csv# importeer csv module

fp = open( "hfst_2\oefen_mee/volcanic-eruptions-EU.csv", "r" ) # open het bestand volanic eruptions en we gaan het bestand readen
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";") #variable csv_reader is gelijk aan csv reader het wordt afgescheiden met ;
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = [] # lege lijst eruptions_11 
for rij in csv_reader: # doorloop rij in csv_reader
    eruptions_ll.append(rij)#voeg rij toe aan eruptions_ll

fp.close() # Na sluiten is CSV niet meer bruikbaar

for eruption in eruptions_ll:
    print(eruption)