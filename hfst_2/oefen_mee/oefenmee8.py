import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2\oefen_mee/oefenneem8.json", "r")
appel = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

print(appel["zondag"])