secret = 'avocado'
tries = []
chances = 3

while True:
    if chances <= 0:
        print("You lose")
        break

    letter = input('Type a letter: ')

    if len(letter) > 1:
        print('type 1 letter...')
        continue

    tries.append(letter)

    if letter in secret:
        print(f'awesome letter {letter} exists...')
    else:
        print(f'you missed it... {letter} doesnt exists...')
        tries.pop()

    secret_temp = ''
    for secret_letter in secret:
        if secret_letter in tries:
            secret_temp += secret_letter
        else:
            secret_temp += '*'

    if secret_temp == secret:
        print(f'you win... {secret_temp} is the word.')
        break
    else:
        print(secret_temp)

    if letter not in secret:
        chances -= 1

    print(f'you still get {chances} chances...')
    print()
