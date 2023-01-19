ans = set()

def div(n1, n2):
    dels1 = set()
    dels2 = set()

    for i in range(1, int(n1 ** 0.5) + 1):
        if i == 1:
            dels1.add(n1)
        else:
            if n1 % i == 0:
                dels1 |= {i, n1 // i}

    for i in range(1, int(n2 ** 0.5) + 1):
        if i == 1:
            dels2.add(n2)
        else:
            if n2 % i == 0:
                dels2 |= {i, n2 // i}


    return any(i in dels2 and i != 1 for i in dels1)


for a in range(1, 200):
    flag = 1
    for x in range(1, 500):
        flag *= ((div(x, 42)) <= (not(div(x, 7)))) or ((x + a) >= 25)
        if not flag:
            break
    if flag:
        ans.add(a)
print(min(ans))