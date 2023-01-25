def f(x):
    return (not((x not in a) and (x in p))) or (x not in q)

a = set()
p = {3, 6, 9, 12}
q = {1, 2, 3, 4, 5, 6}

for i in range(1, 1_000):
    if not f(i):
        a.add(i)
print(len(a))