list = input().split()

for i in range(1, len(list), 2):
    list[i], list[i - 1] = list[i - 1], list[i]
print(' '.join(list))