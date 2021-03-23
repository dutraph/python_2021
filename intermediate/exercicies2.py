# 1
def func1(): return 'func1 value'


def func2(func):
    return func()


print(func2(func1))


# 2

def greetings(name):
    return f'Hi {name}'


def greetings_advanced(name, greeting):
    return f'{greeting} {name}'


def main_func(func, *args, **kwargs):
    return func(*args, **kwargs)


print(main_func(greetings, 'Paulo'))
print(main_func(greetings_advanced, 'Paulo', greeting='Good Afternon'))

