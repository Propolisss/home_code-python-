def f(x):
    return ((x in p) <= (x not in q)) or (x in a)

a = set()
p = {1, 3, 5, 7, 9, 11}
q = {3, 6, 9, 12}

for i in range(1, 1_000):
    if not f(i):
        a.add(i)
print(sum(a))