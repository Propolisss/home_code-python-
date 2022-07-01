list = input().split()
l = ''

for i in range(0, len(list), 2):
    l += str(list[i]) + ' '
print(l)