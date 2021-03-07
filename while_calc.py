while True:
    print()
    n1 = input("Enter 1st number: ")
    n2 = input("Enter 2nd number: ")
    oper = input("Enter the operator: ")


    if not n1.isnumeric() or not n2.isnumeric():
        print("Enter a valid number...")
        continue
    
    n1 = int(n1)
    n2 = int(n2)


    if oper == '+':
        print(n1 + n2)

    elif oper == '-':
        print(n1 - n2)
    
    elif oper == '*':
        print(n1 * n2)
    
    elif oper == '/':
        div = n1 / n2
        print(f'{div:.2f}')
    
    else:
        print("Must enter a valid operator..")
        continue

    print(end='\n\n')
    exit = input("Exit? [y/n]: ")

    if exit == 'y':
        break