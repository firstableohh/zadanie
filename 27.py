# a
with open('/Users/valery/ige_1/27A_7603.txt', 'r') as f:
    n = int(f.readline())
    k = int(f.readline())
    pairs = []
    for i in range(n):
        m = f.readline()
        pairs.append(int(m))

print('A:')
mmax = 0
m = 0
for i in range(k, n):
    mmax = max(mmax, pairs[i]-k)
    m = max(m, m + mmax)

print(m)

# b
print('B:')
with open('/Users/valery/ige_1/27B_7603.txt', 'r') as f:
    n = int(f.readline())
    k = int(f.readline())
    pairs = []
    for i in range(n):
        m = f.readline()
        pairs.append(int(m))


mmax = 0
m = 0
for i in range(k, n):
    mmax = max(mmax, pairs[i]-k)
    m = max(m, m + mmax)

print(m)