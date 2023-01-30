# Maak een GUI met minstens drie aparte labels:
# inhoud van labels is: Hallo, Klas en 6IICT.

import tkinter as tk

venster = tk.Tk()

label = tk.Label(master=venster, text="Hallo, Tkinter!")
label.grid(row=0, column=0)

venster.mainloop()
