import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2\oefen_mee/oefen_mee12.json", "r")
agenda = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar



x = input()
print(agenda[x])
s = input("wil je deze acitiviteit wijzigen? ")
if s == "ja":
    b = input("wat wil je doen dan ")
    agenda[x] = b
x = input()
print(agenda[x])