file = open('26.txt')
n, all_summ = map(int, file.readline().split())
need = []
no_need = []

for i in file:
    temp_arr = [int(j) for j in i.split()]
    need.append(temp_arr) if temp_arr[1] == 1 else no_need.append(temp_arr)
need.sort()
no_need.sort()
summ = sum(int(i[0]) + 10 for i in need)
count = len(need)
maxx = float('-inf')

for i in range(len(no_need)):
    if (summ + no_need[i][0] + 10) <= all_summ:
        summ += no_need[i][0] + 10
        count += 1
        last = no_need[i][0] + 10

for i in range(len(no_need) - 1, -1, -1):
    if (summ - last + no_need[i][0] + 10) <= all_summ:
        maxx = no_need[i][0]
        break
print(count, maxx)