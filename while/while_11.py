num = -1
k = -1
max = 0

while num != 0:
    num = int(input())
    if num > max:
        k += 1
        max = num
    else:
        max = num
print(k)

#prev = int(input())
#answer = 0

#while prev != 0:
    #next = int(input())
    #if next != 0 and prev < next:
        #answer += 1
    #prev = next
#print(answer)