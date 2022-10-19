import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2\oefen_mee/oefenmee9.json", "r")
quiz = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar
for key, onderwerp in quiz["quiz"].items():
    for key2, vraag in onderwerp.items():
        print(vraag["vraag"])
        print("kies uit", vraag["opties"])
        x = input()
        if x in vraag["antwoord"]:
            print("goed")
        else:
            print("fout")
