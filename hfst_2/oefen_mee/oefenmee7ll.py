import csv
fp = open( "hfst_2\oefen_mee/volcanic-eruptions-EU.csv", "r" ) # open het bestand volanic eruptions en we gaan het bestand readen
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen
csv_reader = csv.reader( fp , delimiter=";") #variable csv_reader is gelijk aan csv reader het wordt afgescheiden met ;
# print(csv_reader[3]) # Voorbeeld
# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = [] # lege lijst eruptions_11  
for rij in csv_reader: # doorloop rij in csv_reader
    eruptions_ll.append(rij)#voeg rij toe aan eruptions_ll
    print(rij)
fp.close() # Na sluiten is CSV niet meer bruikbaar

eruptions_ll_verwerkt = []

for index, rij in enumerate(eruptions_ll):
    if index == 0:
        eruptions_ll_verwerkt.append([rij[1],rij[4]])
    else:
        eruptions_ll_verwerkt.append([abs(int(rij[1])),rij[4].lower()])#voeg rij toe aan eruptions_ll

fp = open( "kritieken_to_csv7ll.csv", "w", newline="")
csv_writer = csv.writer( fp , delimiter=";")

for rij in eruptions_ll_verwerkt:
    csv_writer.writerow(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar