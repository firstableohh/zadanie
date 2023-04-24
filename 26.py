with open('/Users/valery/ige_1/26_7602.txt', 'r') as f:
    k = int(f.readline())
    n = int(f.readline())

    pairs = []
    for i in range(n):
        m = f.readline()
        m = m.split(' ')
        pairs.append([int(m[0]), int(m[1])])

    pairs = sorted(pairs)


# k = 2
# n = 5
# pairs = [[30,60], [40,60], [50,1110], [61,1010], [1100, 1440]]

kk = [-1]*k
c = 0
for p in range(len(pairs)):
    for kek in range(k):
        if (pairs[p][0] +1) >= kk[kek] :
            c += 1
            kk[kek] = pairs[p][1]
            break

print(c, kek+1)