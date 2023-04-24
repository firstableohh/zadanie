def f(x):
    x2 = bin(x)[2:]
    if x % 3 == 0: x2 += x2[-3:]
    if x% 3 != 0: x2 += bin((x%3)*3)[2:]

    return int(x2,2)

for i in range(1000,0,-1):
    if f(i) < 100:
        print(i)
        break
