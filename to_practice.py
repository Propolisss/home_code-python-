

def f(n):
    if n < 2:
        return n
    if (n >= 2) and (n % 2 == 0):
        return f(n // 2) + 1
    if (n >= 2) and (n & 1):
        return f(n * 3 + 1) + 1

count = 0
for i in range(1, 100 + 1):
    try:
        if f(i) > 100:
            count += 1

print(count)