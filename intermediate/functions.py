def greeting(msg='Hi', name='user'):
    msg = msg.replace('e', '3')
    name = name.replace('e', '3')
    return f'{msg} {name}'


print(greeting())  # Use the default parameters set
print(greeting(name='John'))  # only the default msg will be used
print(greeting('Hello', 'Paulo'))
print(greeting('Hey', 'Lisa'))
print(greeting('Howdy', 'Mark'))


# Akawrds things in python
def f(test):
    print(test)


def dumb():
    return f


var = dumb()  # now var == f
var('Hey you...')


# *args **kwargs

def func(*args):
    print(args)
    args = list(args)
    return args


lista = [1, 2, 3, 4, 5]
# print(func(1, 2, 3, 4, 5))
a = func(1, 3, 4, 5, 6, 7)
print(a)
a.append(8)
print(a)


def func2(*args):
    print(args)


lis1 = [1, 2, 3, 4, 5]
lis2 = [10, 20, 30, 40, 50]

func2(*lis1, *lis2)  # merge both lists in 1 tuple (1, 2, 3, 4, 5, 10, 20, 30, 40, 50)


def func3(*args, **kwargs):
    print(args)
    print(kwargs)
    # print(kwargs['name'], kwargs['surname'])

    name = kwargs.get('name')
    surname = kwargs.get('surname')
    age = kwargs.get('age')

    if age is not None:
        print(f'Age = {age}')
        print(f'Name = {name}')
        print(f'Surname = {surname}')
    else:
        print('Age does not exist')


lis1 = [1, 2, 3, 4, 5]
lis2 = [10, 20, 30, 40, 50]

func3(*lis1, *lis2, name='Paulo', surname='Dutra', age=30)
# (1, 2, 3, 4, 5, 10, 20, 30, 40, 50) ARGS
# {'name': 'Paulo', 'surname': 'Dutra'} KWARGS
