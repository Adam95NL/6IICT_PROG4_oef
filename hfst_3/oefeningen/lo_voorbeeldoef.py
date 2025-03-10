""" Algemeen:
Schrijf bij iedere regel code commentaar 
De code mag geen foutmeldingen geven
    Opgelet! Code in commentaar wordt niet bekeken.
"""

""" 
lo_voorbeeldoefening.json bevat info over het schaakstuk "toren".
"""

""" STAP 1:
laad lo_voorbeeldoefening.json in Python. Zet deze dictionary in een variabele.

Lukt dit niet? Dan mag je de dictionary rechtstreeks hieronder plakken.
               Je krijgt dan wel geen punten voor dit onderdeel.
"""
import json


fp = open("hfst_3\oefeningen\lo_voorbeeldoefening.json", "r")
info = json.load(fp)
fp.close()

print(info)
""" STAP 2:
print volgende zaken over de toren:
    - De naam zelf (toren)
    - Hoeveel pionnen deze waard is (5)
    - 1 van de beweging die het kan maken (bvb. boven)

Je moet deze info uit de dictionary halen (dus niet manueel invullen).
"""
for key,value in info.items():
    print(key)
    print(value["waarde_pionnen"])
    print(value["beweging"][1])


""" STAP 3:
Voeg volgende zaken toe aan de dictionary (links staat de key, rechts de value):
    - engelse_naam: rook
    - andere_namen: ["Toring", "Torra", "Rukhkh", "Top"]

"""
info["toren"]["engelse_naam"] = "rook"
info["toren"]["andere_namen"] = ["Toring", "Torra", "Rukhkh", "Top"]
print(info)

    
""" STAP 4:
Schrijf de gewijzigde dictionary weg naar een NIEUW JSON-bestand.
Bijvoorbeeld lo_voorbeeldresultaat.json .
"""

fp = open("hfst_3\oefeningen\lo_voorbeeldoefeningstap4.json", "w")
json.dump(info, fp)
fp.close()