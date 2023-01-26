num = (2 ** 345 + 8 ** 65 - 4 ** 130) * (8 ** 123 - 2 ** 89 + 4 ** 45)
num = oct(num)[2:]
print(sum(int(i) for i in num))