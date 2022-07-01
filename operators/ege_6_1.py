n = 1
s = 0
summ = 200
count = 0

while 0 < n <= 46:
    n = 1
    summ += 1
    s = summ
    while s > 200:
        s = s - 15
        n = n + 3
    if n == 46:
        count += 1
print(count)