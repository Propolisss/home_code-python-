p = set(range(2, 30 + 1, 2))
q = set(range(1, 31 + 1, 3))
a = set(range(1, 10_000))

def f(x):
    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))

for i in range(1, 10_000):
    if not(f(i)):
        a.remove(i)
print(len(a))