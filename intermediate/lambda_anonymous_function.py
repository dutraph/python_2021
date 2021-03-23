# Regular function
def func(x, y):
    return x * y


var = func(2, 3)
print('Regular')
print(var)

# Lambda/Anonymous function
a = lambda x, y: x * y

print('Lambda')
print(a(2, 3))

# v = int(input("Enter a number: "))
# z = lambda test: 'elegible' if test >= 5 else 'not elegible'
# print(z(v))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 9],
]
# These methos below modify the original list
lista.sort(key=lambda item: item[1])
print(lista)

lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

# method without edit original list

print(sorted(lista, key=lambda i: i[1]))
