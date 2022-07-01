count = 0
counter = 0
minn = 0

for i in range(10001, 50000 + 1):
    counter = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            counter += 2
        if counter > 17:
            if count == 0:
                minn = i
            count += 1
            break
print(count, minn, sep = '')