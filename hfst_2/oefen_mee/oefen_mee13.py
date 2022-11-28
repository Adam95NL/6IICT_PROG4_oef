import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2\oefen_mee/oefen_mee13.json", "r")
coronalijst = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

for index,dagen in enumerate(coronalijst):
    if index == 0:
        print("er zijn 0 gevallen")
    else:
        print(f"{dagen['Date']} er zijn {dagen['Cases'] - f} nieuwe gevallen ")
    f = dagen["Cases"]
    coronalijst[index]["Niuewe gevellane"] = dagen['Cases'] - f

fp = open("hfst_2\oefen_mee/oefen_mee13.json", "w")
json.dump(coronalijst, fp)
fp.close()
