import csv 

 

fp = open( "nieuwe_csv.csv", "w", newline="") 

 

csv_writer = csv.writer( fp , delimiter=";") 

csv_writer.writerow( ["FILM", "SCORE", "OKE"] ) 

csv_writer.writerow( ["Monty Python and the Holy Grail", 8] ) 

csv_writer.writerow( ["Monty Python's Life of Brian", 8.5] ) 

csv_writer.writerow( ["Monty Python's Meaning of Life", 7] ) 

 

fp.close() # Na sluiten is CSV niet meer bruikbaar 


fp = open( "nieuwe_csv.csv", "r" )
csv_reader = csv.reader( fp , delimiter=";")

for rij in csv_reader:
    print(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar


