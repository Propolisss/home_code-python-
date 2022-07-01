list = input().split()
count = 0

for i in range(1, len(list) - 1):
    if (int(list[i]) > int(list[i - 1])) and (int(list[i]) > int(list[i + 1])):
        count += 1
print(count)