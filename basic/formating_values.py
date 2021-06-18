"""
:s - Text (strings)
:d - Integers (int)
:f - float
:.<n>f - decimal steps on float numbers
:<char>(> or < or ^)(qty)(type - s, d or f) 

> - Left
< - Right
^ - Center
"""

n1 = 111
n2 = 3
div = n1 / n2

print(f'{div:.2f}')

print(f'{round(div)}')

# complete n1 with 0s and the total os position is 10
print(f'{n1:0>10}') # left
print(f'{n1:0^10}') # center
print(f'{n1:0<10}') # right

username = 'dutra.phs'
numb = len(username)+1
print(numb == 10)
# username_to_email = f'{username:@<numb}'
print(f'{username}@gmail.com')