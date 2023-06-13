from functools import *

@lru_cache(None)
def moves(h):
    a, b, c = h
    return (a + 3, b, c), (a + 13, b, c), (a + 23, b, c), (a, b + 3, c),\
        (a, b + 13, c), (a, b + 23, c), (a, b, c + 3), (a, b, c + 13), (a, b, c + 23)

@lru_cache(None)
def game(h):
    if sum(h) >= 73: return 'w'
    if any(game(i) == 'w' for i in moves(h)): return 'p1'
    if all(game(i) == 'p1' for i in moves(h)): return 'v1'
    if any(game(i) == 'v1' for i in moves(h)): return 'p2'
    if all(game(i) in ['p1', 'p2'] for i in moves(h)): return 'v2'

for i in range(1, 23 + 1):
    if game((2, i, 2 * i)) == 'v2':
        print(i)