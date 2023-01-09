""" Oefening 4 (  / 2)
Maak onderstaande opdrachten over dictionaries.

Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" Opdracht 1:
Zoek in onderstaande dictionary de club die het MEESTE kaarten heeft ontvangen.
Print deze club. Opgelet! Dit programma moet ook blijven werken als de dictionary wijzigt.

RESULTAAT: Nederland
"""
aantal_kaarten_wk = {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20} #aantal kaarten is een dictionary met key en values


sorted_values = sorted(aantal_kaarten_wk.values()) # sorteer de values
sorted_dict = {}#lege dictioanry

for i in sorted_values:#voor i in gesorteerde lijst
    for k in aantal_kaarten_wk.keys(): #voor k in aantalkaarten_wk.keys
        if aantal_kaarten_wk[k] == i: # als aantalkaarten wk [k] gelijk is aan i dan
            sorted_dict[k] = aantal_kaarten_wk[k] #stel de gesorteerde lijst gelijk aan de aantalkaarten
last_key = list(sorted_dict)[-1]# de laatste key is het laatste elment 
print(last_key)#print de laatste key

""" Opdracht 2:
Print de waarde bij de key "corners".
"""
wk = {"Duitsland": {"status": "uitgeschakeld", "matchen_gespeeld": 3, "statistieken": {"kaarten": 14, "corners": 9.8, "CS%": 10}}}# dictionary wk met elementen erin

print(wk["Duitsland"]["statistieken"]["corners"])#print de value in wk duitstalnd statistieken corners
""" Opdracht 3:
Vraag de gebruiker om een letter. Verwijder vervolgens alle keys waarin deze letter staat.
    Tip: gebruik if ... in ... om te controleren of een bepaalde letter in de key voorkomt.

Print de gewijzigde dictionary. 
Opgelet! Het programma mag geen onderscheid maken tussen kleine en grote letters.

VOORBEELD:
    Geef een letter op: L
    {"Spanje": 7}

    Geef een letter op: N
    {}

    Geef een letter op: z
    {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}

"""
aantal_kaarten_wk = {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}#dict met aantel kaarten per land
x = input("geeft letter op: ")# x is de ingegeven letter
for key, value in aantal_kaarten_wk.items(): #doorloop alle ket en value in de dict aantalkaarten
    if x in key.split():#als x in key.split dan
        key.pop(key,'')#pop de key en stop en niks ins
print(aantal_kaarten_wk)#print de aantal kaarten

