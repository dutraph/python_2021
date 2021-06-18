"""
* Split - divide a string #str
* Join - join a list #str
* Enumerate - enumerate list elements #iterables
"""

# Split
string = "O Brasil é o pais do futebol, o Brasil é penta..."
# lista = string.split(' ')
lista = string.split(',')
print(lista)

for valor in lista:
    print(valor.strip().title())
    # print(f'the word ({valor}), appeared {lista.count(valor)} time(s)')

# Join
string2 = 'O Brasil é penta.'
lista2 = string2.split(' ')
print(lista2)
join_string = '-'.join(lista2)
print(join_string)

# Enumerate
lista3 = list(range(1354, 1365))

for v1, v2 in enumerate(lista3):
    print(f'index = {v1}, value = {v2}')

lista6 = [
    # 0       1       2
    ['Edu', 'Joao', 'Luiz'],  # 0
    ['Maria', 'Aline', 'Joana'],  # 1
    ['Paulo', 'Max', 'Jack'],  # 2
]

print(lista6[0][1])  # Joao
print(lista6[2][1])  # Paulo

enumerada = enumerate(lista6)
# print(list(enumerada)[2])
for enum in enumerada:
    print(enum)

'''
indx          value   
[(0, ['Edu', 'Joao', 'Luiz']), 
 (1, ['Maria', 'Aline', 'Joana']), 
 (2, ['Paulo', 'Max', 'Jack'])]
'''

# Unpack list
lista4 = ['paulo', 'maria', 'joao', 'marcos', 1, 2, 3, 4, 5, 6, 7, 8]
n1, n2, n3, n4, *new_list = lista4 # with the '*var_name' we create a new list with the rest of remaining package values

print(n1)
print(n2)
print(n3)
print(n4)
print(new_list)

# if you dont care about a part of the list you can do like this
lista9 = ['astolfo', 'crisleid', 'joao', 'marcos', 1, 2, 3, 4, 5, 6, 7, 8]
n1, n2, *_ = lista9

print(n1)
print(n2)

