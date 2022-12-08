

def f(n):
    if n == 0:
        return 0
    elif n > 0 and (n % 2 == 0):
        return f(n // 2)
    elif n & 1:
        return 1 + f(n - 1)
count = 0

for i in range(1, 1000 + 1):
    if f(i) == 3:
        count += 1
print(count)