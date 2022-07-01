list = [int(i) for i in input().split()]
count = 0

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            count += 1
print(count)