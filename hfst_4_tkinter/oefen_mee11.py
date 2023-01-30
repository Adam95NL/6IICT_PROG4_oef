# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()

woord = ""


veld = tk.Entry(master=venster, font=("Helvetica",14), border=10, borderwidth=5)
veld.pack()

# TODO: functie aanmaken gelinkt aan Button knop.
#       Doel van functie is toevoegen van Entry veld aan Label onder de knop.
def knop_klik():
    global woord
    woord = woord + veld.get()
    knop = tk.Label(master=venster, text= woord)
    knop.pack()

    
knop = tk.Button(master=venster, command= knop_klik, text="Voeg toe aan string:", width=50)
knop.pack()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()