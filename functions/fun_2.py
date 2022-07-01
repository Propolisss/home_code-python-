

def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n < 0:
        return 1 / res
    else:
        return res


a = float(input())
n = int(input())
print(power(a, n))