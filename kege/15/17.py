def f(x):
    return (x not in a) <= (((x in p) and (x in q)) <= (x in r))

a = set()
p = set(range(2, 20 + 1, 2))
q = set(range(3, 30 + 1, 3))
r = set(range(12, 60 + 1, 12))

for i in range(1, 1_000):
    if not f(i):
        a.add(i)

prod = 1
for i in a:
    prod *= i
print(prod)