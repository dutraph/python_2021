# 1
def greetings(msg, name): return f'{msg} {name}'

# 2
def sum_num(n1, n2, n3): return n1 + n2 + n3

# 3
def aument_percent(num, p): return num + (num * (p / 100))

# 4
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'
    if num % 3 == 0:
        return 'fizz'
    if num % 5 == 0:
        return 'buzz'

    return num


print(greetings('Alo voce', 'Maria'))
print(sum_num(23, 65, 54))
print(aument_percent(50, 10))
print(fizz_buzz(9))

from random import randint
print("----------------------------------")
for i in range(100):
    aleatory = randint(0, 100)
    print(f'{aleatory} = {fizz_buzz(aleatory)}')
print("----------------------------------")
