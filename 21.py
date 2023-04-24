def f(x, m):
    if x >= 78: return m%2 == 0
    if m == 0: return 0

    h = [f(x+1, m-1), f(x+4, m-1), f(x*4, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)

for s in range(1,78):
    if f(s, 4) and not(f(s,2)):
        print(s)
