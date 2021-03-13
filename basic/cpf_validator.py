# import re
#
# while True:
#     cpf = input('Enter your CPF number ex: 000.000.000-00: ')
#     cpf = re.sub('\\.', '', cpf)
#     cpf = re.sub('-', '', cpf)
#     sum_tot_9_dig = 0
#     sum_tot_10_dig = 0
#     new_cpf = cpf[:-2]
#
#     for e, i in enumerate(range(10, 1, -1)):
#         tot = int(i) * int(cpf[e])
#         sum_tot_9_dig += tot
#
#
#     def digit(soma):
#         find_digit = 11 - (soma % 11)
#         if find_digit > 9:
#             return 0
#         else:
#             return find_digit
#
#
#     new_cpf += str(digit(sum_tot_9_dig))
#
#     for e, i in enumerate(range(11, 1, -1)):
#         tot1 = int(i) * int(new_cpf[e])
#         sum_tot_10_dig += tot1
#
#     new_cpf += str(digit(sum_tot_10_dig))
#
#     if cpf == new_cpf:
#         print('Valid CPF')
#     else:
#         print('Invalid CPF, please Try again...')
#
#     exit_prog = input('Stop validation [y/n]: ')
#     if exit_prog == 'y':
#         print('Bye...')
#         break
#     else:
#         continue
#
# sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
# if cpf == novo_cpf and not sequencia:
#     print('Válido')
# else:
#     print('Inválido')

# Instructor solution

while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')
