sentence = 'o rato roeu a roupa do rei de roma'
sentence_size = len(sentence)
cont = 0
new_string = ''

user_choice = input("Qual letra deseja tornar maiuscula: ")

while cont < sentence_size:
    char = sentence[cont]
    if char == user_choice:
        new_string += user_choice.upper()
    else:
        new_string += char
    cont+=1

print(new_string)
# else: #while's else
#     print('cheguei no else')