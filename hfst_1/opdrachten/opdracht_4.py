""" Niveau 1 """
dict = {
    "belgie": {
        "provincie": {
            "naam": "limburg",
            "weetjes": {
                "oppervlakte":  2.422,
                "inwoners": 885.951,
                "gouverneur": "Jos Lantmeeters"
            }
        }
    }
}
print(dict["belgie"]["provincie"]["weetjes"]["gouverneur"])

"""niveau 2"""
dict["belgie"]["provincie"]["informatie"] = dict["belgie"]["provincie"].pop("weetjes")
print()

""" Niveau 3 """
extra_info = [  ["mannen", 49.77], 
                ["vrouwen", 50.23], 
                ["hoofdstad", "hasselt"] ]





for info in extra_info:
    dict["belgie"]["provincie"]["informatie"][info[0]] = info[1]
    print(info)

print(dict)