

def f(n):
    if n > 30:
        return n ** 2 + 5 * n + 4
    if n <= 30 and (n % 2 == 0):
        return f(n + 1) + 3 * f(n + 4)
    if n <= 30 and (n & 1):
        return 2 * f(n + 2) + f(n + 5)

count = 0
for i in range(1, 1000 + 1):
    if sum(int(j) for j in str(f(i))) == 27:
        count += 1
print(count)