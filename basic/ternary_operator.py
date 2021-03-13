age = input('How old are you? ')
if not age.isnumeric():
    print('Must enter a number...')
else:
    age = int(age)
    adult = (age >= 18)
    msg = 'Welcome' if adult else 'Get out...'
    print(msg)
