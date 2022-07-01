nums = [11, 13, 17, 19]
count = 0
minn = 0

def num(n):
    counter = 0
    for i in range(1, 19 + 1):
        if n % i == 0:
            if i in nums:
                counter += 1
    if counter == 2:
        return True

for i in range(11000, 22000 + 1):
    if num(i):
        if count == 0:
            minn = i
        count += 1
print(count, minn, sep = '')