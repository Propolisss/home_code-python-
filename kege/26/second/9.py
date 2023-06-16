file = open('26_2651.txt')
n = int(file.readline())
marks = dict()

for i in file:
    nums = [int(j) for j in i.split()]
    if nums[0] in marks:
        marks[nums[0]].add(nums[1])
    else:
        marks[nums[0]] = {nums[1]}

count = 0
local_count = 0
maxx = float('-inf')
for i in sorted(marks):
    local_count = 0
    count += (8 - len(marks[i]))
    local_count = (8 - len(marks[i]))
    if local_count >= maxx:
        maxx = local_count
        maxx_id = i
print(count, maxx_id)