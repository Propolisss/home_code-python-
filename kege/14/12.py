for x in range(2, 1_000):
    num1 = 3 * x ** 0 + 0 * x ** 1 + 1 * x ** 2
    num2 = 7 * (x + 2) ** 0 + 9 * (x + 2) ** 1
    if num1 == num2:
        print(x)