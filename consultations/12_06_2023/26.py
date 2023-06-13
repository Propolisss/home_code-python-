file = open('26-94.txt')
n, k = map(int, file.readline().split())
floor1 = dict()
floor2 = dict()
maxx_floor = float('-inf')

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] == 1:
        if nums[1] in floor1:
            floor1[nums[1]].add(nums[2])
        else:
            floor1[nums[1]] = {nums[2]}
    else:
        if nums[1] in floor2:
            floor2[nums[1]].add(nums[2])
        else:
            floor2[nums[1]] = {nums[2]}
    maxx_floor = max(maxx_floor, nums[1])

count = 0
maxx_id = float('-inf')

for i in range(maxx_floor + 1):
    if i in floor1:
        if all(j not in floor1[i] for j in [1, 2, 3, 4]) or all(j not in floor1[i] for j in [3, 4, 5, 6]):
            count += 1
            maxx_id = max(maxx_id, i)
    if i in floor2:
        if all(j not in floor2[i] for j in [1, 2, 3, 4]) or all(j not in floor2[i] for j in [3, 4, 5, 6]):
            count += 1
            maxx_id = max(maxx_id, i)
print(maxx_id, count)