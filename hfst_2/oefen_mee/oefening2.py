""" OEFENING 2: (  /3)
Onderstaande code gebruikt een API om twee willekeurig getallen te genereren.
Vervolgens wordt het eerste door het tweede getal gedeeld.

Je hebt de requests module nodig voor deze opgave.
"""

""" STAP 1: (  / 2)
Deze code is niet veilig. Er kunnen (minstens) twee zaken misgaan.
    - Delen door 0 (ZeroDivisionError)
    - Geen verbinding met de API (requests.exceptions.ConnectionError)

Vorm de code om naar een try-except structuur, rekening houdend met deze Errors.
Laat de gebruiker in beide gevallen duidelijk weten wat er misliep (gebruikt dus 2 specifieke Exceptions).
    Tip: je kan de requests.exception.ConnectionError simuleren door je internet af te zetten.

Vang alle andere Errors op met een algemene boodschap (VB: "Er ging iets mis...")
"""

""" STAP 2: (  / 1)
Als zich GEEN Errors voordoen, print dan volgende boodschap:
"Programma kwam geen fouten tegen."
"""
import requests, json # Benodigde modules.
try:#probeer de onderstaande code 
    API = "http://www.randomnumberapi.com/api/v1.0/random?min=0&max=3&count=2" # Genereer twee getallen tussen 0 en 5.
    getallen = json.loads(requests.get(API, timeout=3).text) # Haal de twee getallen op als tekst, converteer naar lijst.
    getal_1, getal_2 = getallen[0], getallen[1]   # Zet twee getallen in aparte variabelen.
    print(f"De deling van {getal_1} en {getal_2} is {getal_1/getal_2}") # Print de deling.
except ZeroDivisionError:# je deling door 0 optreed voer de volgende code uit
    print("het is niet mogelijk om iets de delen door 0")#print de tekst
except requests.exceptions.ConnectionError:#als er geen internet verbinding is voer de volgende code uit
    print("Er is geen verbinding met het internet")#print de tekst
except:#als er een andere fout optreed voer de volgende code uit
    print("er ging iets mis")#print dat er iets mis is gegaan