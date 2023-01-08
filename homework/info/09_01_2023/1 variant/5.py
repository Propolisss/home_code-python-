def f(n, base):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % base}{temp_st}'
        temp_n //= base
    return temp_st

ans = []

for i in range(1, 10_000):
    n = f(i, 9)

    for k in range(5):

        maxx = float('-inf')
        maxx_let = ''

        if n.count('5') == n.count('7'):
            n += n[-1]
        else:
            for j in n:
                if n.count(j) > maxx:
                    maxx = n.count(j)
                    maxx_let = j
                elif n.count(j) == maxx:
                    if int(j) > int(maxx_let):
                        maxx = n.count(j)
                        maxx_let = j
            n += maxx_let
    res = hex(int(n, 9))[2:]
    if 'bac' in res:
        ans.append(i)
print(max(ans))