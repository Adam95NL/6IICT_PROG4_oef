import json #benodigde module json
""" Algemeen (gaat over oefening 1 en 2): (  / 2)
Schrijf bij iedere regel code commentaar (  / 1)
Zorg dat de code geen geeft foutmeldingen (  / 1)
    Opgelet! Code in commentaar wordt niet bekeken.
"""

""" OEFENING 1: (  / 5)
oefening1.json bevat info over Warren Buffett.
Dit is een zeer bekende investeerder.
"""

""" STAP 1: (  / 1)
laad oefening1.json in Python. Zet deze dictionary in een variabele.
Gebruik voor beide delen de JSON-module van Python.

Lukt dit niet? Dan mag je de dictionary rechtstreeks in de variabele plakken.
               Je krijgt dan wel geen punten voor dit onderdeel.
"""
fp = open("hfst_2\oefen_mee/oefening1.json", "r")#lokaliseer het het json bestand en we gaan in het bestand alleen readen
persoon = json.load(fp) # we laden de gegevens in het json bestand en we noemen de gegevens persoon
fp.close()  # Na sluiten is JSON niet meer bruikbaar


""" STAP 2: (  / 1)
print volgende zaken van Warren Buffett in een grote f-string:
    - voornaam
    - geboortedatum
    - bedrijf
    - 1 hobby (bvb. deze op index 3)

Je moet deze info uit de dictionary halen (dus niet manueel invullen).

De print kan er als volgt uit zien:
Warren is geboren op 03-08-1930. Hij is de eigenaar van Berkshire Hathaway. Hiernaast speelt hij ook ukelele.
"""
print(f'dit is {persoon["voornaam"]} hij is geboren op {persoon["geboortedatum"]} is eigenaar van het bedrijf {persoon["bedrijf"]} en zij hobby is {persoon["hobbys"][2]}') #print in de fstring de opgeroepen namen

""" STAP 3: (  / 2)
Gebruik code om het minimale en maximale vermogen in de laatste 5 jaar (2017-2021) te bepalen.
Ook als de cijfers van het vermogen zouden wijzigen, moet de code blijven werken.
    Tip: je kan de functies min() en max() toepassen op lijsten. Dit geeft de kleinste/grootste waarde terug.

Lukt dit niet? Dan mag je het minimale en maximale vermogen zelf bepalen.
               Je krijgt dan wel slechts een deel van de punten voor dit onderdeel

Voeg dit minimale en maximale vermogen toe als value aan de hoofddictionary. 
Gebruik hiervoor de keys verm_min en verm_max.
"""
lijst = [] #maak een lege lisjt
for key, value in persoon["vermogen_in_miljard"].items(): #doorloop alle key, values in persoon["vermogen_in_miljard"]
    print(value) #print alle values
    lijst.append(value)#voeg alle values toe aa een lege lijst
lijst.sort() #sorteer alle waardes van klein naar groot in de lijst
print(lijst) #print wat in de lijst staat
persoon["vermogen_min"] = lijst[0] #maak een nieuwe key en zet er de eerste waarde die in de lijst staat dit is dan de value
persoon["vermogen_max"] = lijst[-1]#maak een nieuwe key en zet er de laatste waarde die in de lijst staat dit is dan de value
print(persoon)#print de gegevens persoon 

""" STAP 4: (  / 1)
Schrijf de gewijzigde dictionary weg naar een NIEUW JSON-bestand.
Bijvoorbeeld oefening1_resultaat.json .
"""
fp = open("hfst_2/oefen_mee/oefening1_resultaat.json", "w") #maak een nieuwe json bestand genaamd oefening1_resultaat.json we gaan hierin schrijven 
json.dump(persoon, fp) #dump alles in persoon in het nieuwe json bestand
fp.close() #sluit het json bestand
