# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Vraag om de lievelingskleur van de gebruiker (rood, groen of blauw)
kleur = input("Wat is je favoriete kleur? ")

# Maak een lege GUI aan.
venster = tk.Tk()
if kleur == "groen":
    kleur = "green"
if kleur == "blauw":
    kleur = "blue"
if kleur == "rood":
    kleur = "red"


# TODO: vertaal input van gebruiker naar het Engels

# TODO: maak functie aan die het label in de ingegeven kleur laat zien.
def kleurlabel():
    label = tk.Label(master=venster, text=f"mijn favoriete kleur is {kleur}", fg = kleur)
    label.pack()


knop = tk.Button(master=venster, text="Klik op mij!", command= kleurlabel)
knop.pack()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()