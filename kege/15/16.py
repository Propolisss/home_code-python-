def f(x):
    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))

a = set(range(10_000))
p = set(range(2, 20 + 1, 2))
q = set(range(5, 50 + 1, 5))

for i in range(10_000):
    if not f(i):
        a.remove(i)
print(len(a))