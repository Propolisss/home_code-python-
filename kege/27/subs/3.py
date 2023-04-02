file = open('27B_2902.txt')
n = int(file.readline())
count = 0
k = [0] * 11
counter = 0

for _ in range(n):
    x = int(file.readline())
    if x % 5 == 0:
        counter += 1
    if counter % 11 == 0:
        count += 1

    count += k[counter % 11]
    k[counter % 11] += 1
print(count)