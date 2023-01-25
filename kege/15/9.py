from itertools import *

def f(x):
    return (x not in ans) <= ((x in p) or (x not in q))

s = list(map(''.join, product('01', repeat=8)))
q = []
p = []

for i in s:
    if i.startswith('11'):
        p.append(i)
    if i.endswith('0'):
        q.append(i)

ans = set()

for i in s:
    if not f(i):
        ans.add(i)
print(len(ans))