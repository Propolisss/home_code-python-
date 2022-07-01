summ = 0
count = 0

def fun(n):
    global summ
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            summ = (n // i) + i
            return summ
    return 0

for i in range(220000, 1000000):
    if fun(i) % 10 == 4:
        count += 1
        print(i, summ)
    if count == 5:
        break