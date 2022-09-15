# Maak onderstaande functies af.
# Testen kan MBV de oproepen onder iedere oefeningen.
# Tip: gebruik CTRL + / om meerdere lijnen in/uit commentaar te zetten.

# Deze websites geven meer info over de verschillende methodes van strings:
# https://www.w3schools.com/python/python_strings_methods.asp 
# https://www.programiz.com/python-programming/methods/string 

def aantal_karakters(zin):
    """ return het aantal letters in een zin """
    return len(zin)

print( aantal_karakters("Hallo") )
# print( aantal_karakters("2 plus 2 is 4") )
# print( aantal_karakters("de kat krabt de krullen van de traf af.") )

def titel(zin):
    """ return de zin waarbij ieder woord een hoofdletter heeft
    
        >>> print( titel("de kat krabt") ) --> De Kat Krabt
    """
    return zin.title()

print( titel("de kat krabt") )
# print( titel("krullen van de trap af") )
# print( titel("ditisslechts1woord") ) 

def kort_af(woord):
    """ return de eerste, middelste en laatste karakter van een woord 
    
        Indien het woord even is, return enkel het eerste en laatste karakter.
        >>> print( hoofdletter("krabt") ) --> kat

        Tip: je kan een woord beschouwen als een lijst van karakters.
             Gebruik de index!    
    """
    eerste_letter = woord[0]
    middelste_letter =  woord[(len(woord)-1)//2:(len(woord)+2)//2]
    laatste_letter = woord[-1]
    c = (eerste_letter+ middelste_letter+ laatste_letter)
    return c

print( kort_af("krabt") )
print( kort_af("belgie") )
print( kort_af("mosa-rt") )

def vervang(woord, kar):
    """ return het aangepaste woord 
    
        Vervang ieder karakter kar door een hoofdletter.
        >>> print( vervang("katten", "t") ) --> ka!!en
    """
    return woord.replace(kar, "!")

print( vervang("katten", "t") )
print( vervang("de koetsier poetst de postkoets met postkoetspoets", "oe") )
# print( vervang("Nog een paar tongbrekers", "i") )

def is_laag(zin):
    """ return True of False (boolean!)
    
        True: de zin bevat enkel kleine letters.
        False: de zin bevat ook grote letters.
        >>> print( vervang("Dit is fout!") ) --> False
    """
    
    x = zin.islower()
     
    return x

print( is_laag("Dit is fout!") )
# print( is_laag("een twee drie vIer") )
print( is_laag("een correcte zin") )

def is_getal(kar):
    """ return True of False (boolean!) 
    
        True: het karakter kar is een getal
        False: het karakter kar is geen getal.

        Indien True, voor de return, converteer str kar naar een int.
        Print het kwadraat van de waarde.
        >>> print( is_getal("5") ) --> 25
                                   --> True
    """
    if kar.isnummeric():
        kar = int(kar)
        kar = kar ** 2
    return kar
print( is_getal("5")  )
# print( is_getal("e")  )
# print( is_getal("44") )

def draai_om(zin):
    """ return de zin met alle karakters omgedraaid. 

        >>> print( draai_om("Palindroom") ) --> moordnilaP
    """
    return None

# print( draai_om("Palindroom")  )
# print( draai_om("de kat krabt")  )
# print( draai_om("racecar") )

def tel_klinkers(zin):
    """ return het aantal klinkers in een zin. 

        >>> print( tel_klinkers("De kat krabt") ) --> 3
    """
    return None

# print( tel_klinkers("De kat krabt") )
# print( tel_klinkers("de krullen van de trap af") )
# print( tel_klinkers("Belgie") )