import csv

fp = open( "hfst_2\oefen_mee/volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.reader( fp , delimiter=";")

for rij in csv_reader:
    print(rij[1], rij[4])

fp.close() # Na sluiten is CSV niet meer bruikbaarµ