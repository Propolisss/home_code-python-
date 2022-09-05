def fac(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

print(fac(2023) // fac(2020))