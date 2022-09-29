engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }
vertaal = []
keys_values_dict = list(engels_nederlands.items())
print(keys_values_dict)
x = input("Geef een zin in het Nederlands: ")
zin = x.split()

for woord in zin:
        for key.value in keys_values_dict:
                if 
        nieuwe_zin += f"{engels_nederlands.get(woord, woord)} "
print(nieuwe_zin)