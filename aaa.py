def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def summ_digits(n):
    st = str(n)
    summ = 0
    for i in range(len(st)):
        summ += int(st[i])
    return summ
def fac(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def count_simple_dels(n):
    dels = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if simple(i):
                dels.add(i)
            if simple(n // i):
                dels.add(n // i)
    return len(dels)

print(int(5.9999999999999999))
