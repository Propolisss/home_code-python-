for i in range(2, 10_000):
    s1 = sum(int(j) for j in str(i) if int(j) % 2 == 0)
    s2 = sum(int(str(i)[j]) for j in range(len(str(i))) if (j + 1) % 2 == 0)
    if abs(s1 - s2) == 9:
        print(i)
        break