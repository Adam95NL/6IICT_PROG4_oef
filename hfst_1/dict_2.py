""" Opdracht 2:
Je krijgt een lijst van lijsten genaamd landen_steden.
1) Vorm deze om naar een dictionary van lijsten.
   De eerste lijst bevat alle keys. Deze moeten gekoppeld worden aan de overige lijsten.
   
   Te bekomen dictionary:
   {
    "USA":  ["Boston", "Pittsburgh", "Washington"],
    "UK":   ["London", "Edinburgh", "Belfast"],
    "Frankrijk": ["Parijs", "Lyon", "Avignon"],
    "Duitsland: ["Keulen", "Berlijn"]
   }

2) Vraag de gebruiker om een stad. 
   Gebruik de opgestelde dictionary om het land te printen waarin deze stad zich bevindt.
   >>> input: Lyon
       Frankrijk
"""
landen_steden = [
    ["USA", "UK", "Frankrijk", "Duitsland"],    # Landen
    ["Boston", "Pittsburgh", "Washington"],     # Steden USA
    ["London", "Edinburgh", "Belfast"],         # Steden UK
    ["Parijs", "Lyon", "Avignon"],              # Steden Frankrijk
    ["Keulen", "Berlijn"]                       # Steden Duitsland
]



dict_land = {}
for index, land in enumerate(landen_steden[0]):
    dict_land[land] = landen_steden[index+1]

print(dict_land)

stad = input("Geef een stad: ")
for land, steden in dict_land.items():
    if stad in steden:
        print(land)
    else:
        print("Stad niet in lijst.")
