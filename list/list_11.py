list = input().split()
k = int(input())

for i in range(k + 1, len(list)):
    list[i - 1] = list[i]
list.pop()
print(' '.join(list))


#  list = input().split()
#  k = int(input())
#  list.pop(k)
#  print(list)