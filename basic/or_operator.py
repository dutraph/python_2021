name = input('Whats ur name: ')
if name:
    print(name)
else:
    print('must enter your name...')

# OR OPERATOR

print(name or 'must enter your name...')


a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Paulo'


variable = a or b or c or d or e or f or g #it will assume the first truthy value in this case the value of f
print(variable)