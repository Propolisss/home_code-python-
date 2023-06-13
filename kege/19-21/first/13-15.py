from functools import *

@lru_cache(None)
def moves(h):
    a, b = h
    return (a + 1, b), (a + b, b), (a, b + 1), (a, b + a)

@lru_cache(None)
def game(h):
    if sum(h) >= 68: return 'w'
    if any(game(i) == 'w' for i in moves(h)): return 'p1'
    if all(game(i) == 'p1' for i in moves(h)): return 'v1'
    if any(game(i) == 'v1' for i in moves(h)): return 'p2'
    if all(game(i) in ['p1', 'p2'] for i in moves(h)): return 'v2'

for i in range(1, 59 + 1):
    if game((8, i)) == 'v2':
        print(i)