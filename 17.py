with open('/Users/valery/ige_1/17_7596.txt', 'r') as f:
    text = f.readlines()
    text = [int(i.replace('\n', '')) for i in text]

mm = 10000000
for x in text:
    if len(str(x)) == 3:
        if str(x).endswith('5'):
            print(x)
            if mm > x:
                mm = x
c = 0
mmin = 10000000
for x ,y in zip(range(len(text)), range(1,len(text))):
    if (len(str(text[x])) == 3) or (len(str(text[y])) == 3):
        # print(text[x] , text[y])
        s = (text[x] + text[y])
        if s % mm == 0:
            c +=1
            if mmin > s:
                mmin = s

print(c, mmin)
