from functools import *
from sys import *
setrecursionlimit(100000)

@lru_cache(None)
def moves(h):
    return h * 3, h + 1

@lru_cache(None)
def game(h):
    if h >= 2163: return 'w'
    if any(game(i) == 'w' for i in moves(h)): return 'p1'
    if all(game(i) == 'p1' for i in moves(h)): return 'v1'
    if any(game(i) == 'v1' for i in moves(h)): return 'p2'
    if all(game(i) in ['p1', 'p2'] for i in moves(h)): return 'v2'

for i in range(1, 2162 + 1):
    if game(i) == 'v2':
        print(i)