

def f(n):
    if n <= 18:
        return n + 3
    if n > 18 and (n % 3 == 0):
        return (n // 3) * f(n // 3) + n - 12
    if n > 18 and (n % 3 != 0):
        return f(n - 1) + n ** 2 + 5

count = 0
for i in range(1, 1000 + 1):
    if all(int(j) % 2 == 0 for j in str(f(i))):
        count += 1
print(count)