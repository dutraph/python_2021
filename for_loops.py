string = 'python'

#enumerate
# for n, letra in enumerate(string):
#     print(n, letra)

"""
Output
(0, 'p')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')
"""

#range(start=0, stop<not included>, step=1) default
# for n  in range(10):
#     print(n)

print('')
new_str = ''
start = len(string) - 1
print(len(string))
for n  in range(start,-1, -1):
    new_str+=string[n]
    
print(new_str)


lista = ['a', 'banana', 'c', 'd', 10.2]

print(lista[-1])