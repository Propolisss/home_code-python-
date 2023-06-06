file = open('26.txt')
n, m = map(int, file.readline().split())
nums = [int(i) for i in file]
nums.sort(reverse=True)
cases = []
count = 0
flags = [0] * n

for i in range(n):
    if not flags[i]:
        summ = 0
        for j in range(i, n):
            if not flags[j]:
                if summ + nums[j] <= m:
                    summ += nums[j]
                    flags[j] = 1
        count += 1
        cases.append(summ)

print(count, cases[-2])