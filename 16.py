from functools import lru_cache
import sys

sys.setrecursionlimit(100000)

@lru_cache
def f(x):
    if x >= 2025:
        return x
    return x + 3 + f(x+3)

print(f(23)- f(21))