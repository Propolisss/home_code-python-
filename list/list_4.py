list = input().split()

for i in range(1, len(list)):
    if (int(list[i]) >= 0 and int(list[i - 1]) >= 0) or (int(list[i]) < 0 and int(list[i - 1]) < 0):
        print(list[i - 1], list[i], sep = ' ')
        break