import csv# importeer csv module

fp = open( "hfst_2\oefen_mee/volcanic-eruptions-EU.csv", "r" ) # open het bestand volanic eruptions en we gaan het bestand readen
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen

csv_reader = csv.DictReader( fp , delimiter=";") #variable csv_reader is gelijk aan csv reader het wordt afgescheiden met ;
# print(csv_reader[3]) # Voorbeeld
# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ld = [] # lege lijst eruptions_11  
for rij in csv_reader: # doorloop rij in csv_reader
    dictionary = {}
    dictionary["Year"] = abs(int(rij["Year"]))
    dictionary["Name"] = rij["Name"]
    eruptions_ld.append(dictionary)#voeg rij toe aan eruptions_ll
fp.close() # Na sluiten is CSV niet meer bruikbaar

for eruption in eruptions_ld:
    print(eruption)