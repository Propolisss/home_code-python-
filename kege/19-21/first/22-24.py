from functools import *
from sys import *
setrecursionlimit(1_000_000)

@lru_cache(None)
def moves(h):
    mov = []
    a, b = h
    if a > 0: mov.append((a - 1, b))
    if b > 0: mov.append((a, b - 1))
    if a > 1: mov.append(((a + 1) // 2, b))
    if b > 1: mov.append((a, (b + 1) // 2))
    return mov

@lru_cache(None)
def game(h):
    if sum(h) <= 20: return 'w'
    if any(game(i) == 'w' for i in moves(h)): return 'p1'
    if all(game(i) == 'p1' for i in moves(h)): return 'v1'
    if any(game(i) == 'v1' for i in moves(h)): return 'p2'
    if all(game(i) in ['p1', 'p2'] for i in moves(h)): return 'v2'

for i in range(11, 100):
    if game((10, i)) == 'p2':
        print(i)