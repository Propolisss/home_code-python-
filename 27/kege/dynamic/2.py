file = open('27A.txt')
n = int(file.readline())
nums = [int(i) for i in file]
k65 = 0
k13 = 0
k5 = 0
k = 0
count = 0

for i in nums:
    if i % 65 == 0: count += k
    elif i % 13 == 0: count += k5
    elif i % 5 == 0: count += k13
    else: count += k65

    if i % 65 == 0: k65 += 1
    if i % 13 == 0: k13 += 1
    if i % 5 == 0: k5 += 1
    k += 1
    
print(count)