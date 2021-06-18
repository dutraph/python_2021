print('Paulo', 'Silva', sep='-', end='#######')
print('Maria', 'Maciel', sep='-', end='')
cpf9 = input("Entre os 11 digitos do cpf sem espaço separações:  ")


b1 = cpf9[0:3]
b2 = cpf9[3:6]
b3 = cpf9[6:9]
b4 = cpf9[9:]
print(b1, b2, b3, sep='.', end='-')
print(b4)