prog = 0
regr = 0
lista = list(range(1, 10))
for i in lista:
    print(prog, (regr + lista[-1] + 1))
    prog += 1
    regr -= 1

print('----------------------------------------------------------')
# Instructor solution
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)