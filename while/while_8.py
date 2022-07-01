num = int(input())
max = 0

while num != 0:
    if max < num:
        max = num
    num = int(input())
print(max)