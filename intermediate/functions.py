def greeting(msg='Hi', name='user'):
    msg = msg.replace('e', '3')
    name = name.replace('e', '3')
    return f'{msg} {name}'


print(greeting())  # Use the default parameters set
print(greeting(name='John'))  # only the default msg will be used
print(greeting('Hello', 'Paulo'))
print(greeting('Hey', 'Lisa'))
print(greeting('Howdy', 'Mark'))
