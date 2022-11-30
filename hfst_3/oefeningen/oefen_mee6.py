fruit_lijst = ["Appel", "Banaan", "Kers"]

try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except ValueError:
    print( "geef een getal" )  
except IndexError:
    print("je bent buiten de range gegaan")
except TypeError:
    print("geef een geheel getal")
except:
    print(f"\nerror")

print("Programma klaar")  
