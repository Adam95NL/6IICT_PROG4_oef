""" Niveau 1 """
try:
    num_lijst = [ 100, 101, 0, "103", 104 ]
    index = int( input( "Geef een index: " ) )
except ValueError:
    print( "geef een getal" ) 
except TypeError:
    print("geef een geheel getal")
except IndexError:
    print("je bent buiten de range gegaan")
except:
    print("error")
""" Niveau 2 (haal uit commentaar) """
# print( f"100 / {num_lijst[index]} = {100/num_lijst[index]}" ) 

""" Niveau 3 (haal uit commentaar) """
# print( "Geldig getal als index opgegeven." )
