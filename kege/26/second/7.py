file = open('26_2480.txt')
n = int(file.readline())
road = [0] * 2_000_001

for i in file:
    nums = [int(j) for j in i.split()]
    road[nums[0]] += 1
    road[nums[1]] -= 1

k = 0
prev = k
st = -1
count = 0
summ = 0
for i in range(1, len(road)):
    prev = k
    k += road[i]
    if k == 0 and st == -1:
        st = i
    if k > 0: summ += 1
    if k == 0 and prev > 0:
        st, end = -1, 0
        count += 1
print(count, summ)