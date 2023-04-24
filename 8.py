from itertools import product

c = 0
cc = []
for i in product('АВЛОР', repeat=4):
    i = ''.join(i)
    cc.append(i)
    c+= 1
    if i[0] == 'Л':
        print(c)
        break

print(len(cc))