# """ Niveau 1"""
# dict_1={1: 10, 2: 20}
# dict_2={3: 30, 4: 40}
# dict_3={5: 50, 6: 60}
# # Resultaat: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dict_1.update(dict_2)
# dict_1.update(dict_3)
# print(dict_1)

# """ Niveau 2 """
# dict = {'a': 'Red', 'b': 'Green', 'c': None}
# # Resultaat: {'a': 'Red', 'b': 'Green'}
# for key, value in dict.copy().items():
#     if value is None:
#         del dict[key]
# print(dict)

""" Niveau 3 """
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
# Resultaat: {'a': 400, 'b': 400, 'd': 400, 'c': 300})
dicttot = {}
for key_1, waarde_1 in dict_1.items():
    print(waarde_1)


for key_2, waarde_2 in dict_2.items():
    dict_1[key_1] = sum(waarde_2)
    

    
print(dict_1)
