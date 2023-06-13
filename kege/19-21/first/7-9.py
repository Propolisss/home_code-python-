from functools import *
@lru_cache(None)
def moves(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)

@lru_cache(None)
def game(h):
    a, b = h
    if a + b >= 59: return 'w'
    if any(game(i) == 'w' for i in moves(h)): return 'p1'
    if all(game(i) == 'p1' for i in moves(h)): return 'v1'
    if any(game(i) == 'v1' for i in moves(h)): return 'p2'
    if all(game(i) in ['p1', 'p2'] for i in moves(h)): return 'v2'

for i in range(2, 53):
    if game((5, i)) == 'v2':
        print(i)