""" 
# Python Lists
slicing
append, insert, pop, del, clear, extend, +
min, max
range
"""

lista = ['a', 'banana', 'c', 'd', 10.2]

lista.append('morango')
print(lista)
print(lista[-1])

print(lista[1][2])

# a = input("digite para inverter: ")

# print(a[::-1])

# Sum lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
# Or 
l1.extend(l2)

print(l3)
print(l1)

# insert values 
l2.insert(0, 'banana')
print(l2)

# remove last element (default) or pass (index) you wanna remove
l2.pop(1)
print(l2)

# remove more than 1 index
#     0 1 2 3 4 5 6 7 8  index
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del (l4[2:5])
print(l4)

# Max value and Min value
print(max(l4))
print(min(l4))

# Create list with range built in
l5 = list(range(1, 11))
print(l5)

l6 = list(range(1, 101, 8))
print(l6)

sum1 = 0
for valor in l6:
    sum1 += valor

print(sum1)