for i in range(2, 10_000):
    n = bin(i)[2:]
    s1 = sum(1 for j in range(len(n)) if n[j] == '1' and j & 1)
    s2 = sum(1 for j in range(len(n)) if n[j] == '0' and j % 2 == 0)
    if abs(s1 - s2) == 5:
        print(i)
        break