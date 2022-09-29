# Open lied.txt in Python
lied = open("hfst_1/opdrachten/lied.txt", "r")
lied2 = open("hfst_1/opdrachten/lied_2.txt", "r")
# Vorm lied om naar lijst, vervang witregels '\n' door spaties ' ' 
lied = lied.read().replace('\n', ' ') 
lied2 = lied2.read().replace('\n', ' ') 
# Test inhoud van lied
print(lied)
dict = {

}
""" Begin eigen code hier """
for woord in lied.split():
    if woord in dict:
        dict[woord] = dict[woord] + 1
    else:
        dict[woord] = 1
    
    print(woord , woord.count(""))

"niveau 2"
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for leestekens in punc:
    if leestekens in lied2:
        lied2 = lied2.replace(leestekens)
print(lied2)
