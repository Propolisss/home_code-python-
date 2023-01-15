for x in range(2, 1000):
    num1 = 3 * (x + 4) ** 0 + 3 * (x + 4) ** 1
    num2 = 3 * 4 ** 0 + 3 * 4 ** 1
    if num1 - num2 == 33:
        print(x)