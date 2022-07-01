num = -1
max = 0
i = -1

while num != 0:
    num = int(input())
    i += 1
    if num > max:
        max = num
        maxi = i
print(maxi)