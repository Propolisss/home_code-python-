file = open('26_2615.txt')
n = int(file.readline())
sums = set()
nums = sorted(int(i) for i in file)
s = set(nums)
count = 0
summ = 0
for i in nums:
    sums |= set(j + i for j in sums) | {i}
    count += 1
    summ += i
    if len(set(range(1, summ + 1)) - sums) > 0:
        print(min(set(range(1, summ + 1)) - sums), count - 1)
        break
print('asdf')