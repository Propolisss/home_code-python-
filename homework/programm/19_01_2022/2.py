
count = 0

for i in range(5, 1_000_000, 5):
    n = oct(i)[2:]
    if len(n) == 6:
        if all(n.count(j) == 1 for j in n):
            if all(((int(n[j - 1]) % 2 == 0) != (int(n[j]) % 2 == 0)) for j in range(len(n))):
                count += 1
print(count)