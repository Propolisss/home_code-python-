

def f(n):
    count = 1
    if n >= 1:
        count += 1
        count += f(n - 1)
        count += f(n - 3)
        count += 1
    return count
print(f(40))