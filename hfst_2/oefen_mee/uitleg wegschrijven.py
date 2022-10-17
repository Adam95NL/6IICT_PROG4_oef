import csv 
fp = open( "kritieken_to_csv.csv", "w", newline="") 
csv_writer = csv.writer( fp , delimiter=";") 
 

film_kritieken = [ 
["FILM", "SCORE"], 
["Monty Python and the Holy Grail", 8], 
["Monty Python's Life of Brian", 8.5], 
["Monty Python's Meaning of Life", 7] 

] 

 


 

for rij in film_kritieken: 

    csv_writer.writerow(rij) 

fp.close() # Na sluiten is CSV niet meer bruikbaar 