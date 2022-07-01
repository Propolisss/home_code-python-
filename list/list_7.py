list = [int(i) for i in input().split()]
n = int(input())
count = 0

for i in range(len(list)):
    count += 1
    if n > list[i]:
        print(count)
        break
else:
    print(len(list) + 1)