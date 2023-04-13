for i in range(10, 10_000):
    maxx = float('-inf')
    minn = float('inf')
    for j in range(len(str(i)) - 1):
        maxx = max(maxx, int(str(i)[j:j + 2]))
        minn = min(minn, int(str(i)[j:j + 2]))
    if maxx - minn == 44:
        print(i)
        break