file = open('26_813.txt')
s, n = map(int, file.readline().split())
nums = sorted([int(i) for i in file])
last = []
summ = 0
count = 0

while summ <= s:
    if count % 2 == 0:
        if summ + nums[0] <= s:
            summ += nums[-1]
            last.append(nums[-1])
            del nums[-1]
            count += 1
    else:
        if summ + nums[0] <= s:
            summ += nums[0]
            last.append(nums[0])
            nums.pop(0)
            count += 1
        else:
            break
print(count, last[-1])