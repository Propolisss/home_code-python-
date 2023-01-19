dic = {'0' : 0}
nums = [i.replace(';', ' ').split() for i in open('22 (1).csv')]
al = [0, ]

while len(dic) < len(nums) + 1:
    for s in nums:
        if all(sub in dic for sub in s[2:]):
            dic[s[0]] = int(s[1]) + max(dic[sub] for sub in s[2:])
            al.append(dic[s[0]] - int(s[1]))
count = 0
time = [0] * 100
print(al)
for i in dic:
    for j in range(al[int(i)], dic[i]):
        time[j] += 1

maxx = max(time)
print(time.count(maxx))