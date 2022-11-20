


for i in range(1000):
    N = i
    num  = bin(N)
    num = num[2:]
    num += str(num.count('static') % 2)
    num += str(num.count('static') % 2)
    if int(num, 2) > 125:
        print(i)
        break