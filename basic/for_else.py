lista = ['paulo', 'maria', 'pitagoras', 'platao']

for nome in lista:
    if nome.lower().startswith('p'):
        print(nome)
else:
    print('Nenhum nome com p')