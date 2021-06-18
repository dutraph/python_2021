import itertools
import io

f = open("separated", "r")
lines = [line for line in f.readlines()]
l = []
for i in range(0, len(lines)):
    l.append(lines[i].rstrip('\n').split(','))

ab = []
for i in range(0, len(l)):
    ab.extend(l[i])

string = []
for x in ab:
    if not x.isdigit():
        string.append(x)

string.sort()

lowercase = []

string = [string.lower() for string in string]

string = list(dict.fromkeys(string))
string.sort()
print(string)

for i in range(3):
    with io.open("file_" + str(i), 'w', encoding='utf-8') as j:
        j.write("-----\n")
        j.write(str(i) + "\n")
        j.write(string[i].upper() + "\n")
        j.write("-----\n")
j.close()

f.close()
