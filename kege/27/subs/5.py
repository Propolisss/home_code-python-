file = open('27A_2903.txt')
n = int(file.readline())
minn = float('inf')
k = [0] * n
summ = 0
counter = 0

for _ in range(n):
    x = int(file.readline())
    summ += x

    if x % 3 == 0:
        counter += 1
    if counter == 10:
        minn = min(minn, summ)
    if counter >= 10:
        minn = min(minn, summ - k[counter - 10])
    k[counter] = max(k[counter], summ)
print(minn)