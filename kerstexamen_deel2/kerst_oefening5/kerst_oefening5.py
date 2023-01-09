import json
import csv
""" Oefening 5 (  / 4)
Het JSON-bestand kerst_oefening5.json bevat een agenda.
Het zou echter handiger zijn als deze agenda in een CSV-bestand stond.

Lees kerst_oefening5.json in, in een Python variabele.
Schrijf deze vervolgens weg naar een bestand kerst_oefening5.csv.
kerst_voorbeeld5.csv toont hoe dit CSV-bestand er uit moet zien.

ALLES wat je naar dit CSV-bestand schrijft, moet uit het JSON-bestand komen. Manueel zaken ingeven mag dus niet.
Dit zodat het converteren blijft werken, ook wanneer je een andere JSON-agenda zou gebruiken.
Je mag ervanuit gaan dat iedere dag HETZELFDE aantal activiteiten heeft.
"""

fp = open("kerstexamen_deel2\kerst_oefening5/kerst_oefening5.json", "r")# open het bestand en we gaan readen
agenda = json.load(fp) #agende is gelijk aan de gegevens in het json bestand
fp.close()# sluit de gegevens in het bestan

print(agenda)#print de agenda
fp = open( "oef5.csv", "w", newline="")# open een bestand genaamd oef5.csv en we gaan erin writen de "" wordt gekenmerkt door een nieuwe lijn
csv_writer = csv.writer( fp , delimiter=",") # csv writer gaat schrijven in de variable fp en de scheidingtekens zijn de komma



dagen = []#lege lijst fagen
lijst = []#lege lijst lijst
for key, value in agenda.items():#doorloop de key en value in agenda.items
    print(key)#print de key
    dagen.append(key)#append de key aan dagen
    lijst.append(lijst)#append de lijst aan lijst
print(lijst)#print de lisjt

csv_writer.writerow(dagen)#csv writer schrijft per rij de deerlopen rijen
x = 1# x is gelijk aan 1
for index, rij in agenda.items():#doorloop alle index en rijen en tel de agenda
        print(rij)#print rij
        csv_writer.writerow(rij[x])#csv writer schrijft per rij de deerlopen rijen
        x = x+1# x is gelijk aan x +1

        



fp.close()#close de fp