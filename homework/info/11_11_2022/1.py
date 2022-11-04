for i in range(1234567891011121, 1234567891011121 + 1_000_000_000):
    st = str(i)[::-1]
    for j in range(1, len(st), 2):
        if (int(st[j]) * 2) >= 10:
            st = st[:j] + str(sum(int(k) for k in str(int(st[j]) * 2))) + st[j + 1:]
        else:
            st = st[:j] + str(int(st[j]) * 2) + st[j + 1:]
    summ = sum(int(k) for k in st)
    if summ % 10 == 0:
        print(str(i)[-8:], st[::-1], st)
        break