file = open('26_2614.txt')
s, n = map(int, file.readline().split())
nums = sorted(int(i) for i in file)
unic = [i for i in nums if i > 3000]
enz = [i for i in nums if 2000 <= i <= 3000]
common = [i for i in nums if i < 2000]
summ = max(unic) + min(unic) + sum(enz)
count = 2 + len(enz)
last = 0

for i in range(len(common)):
    if summ + common[i] <= s:
        summ += common[i]
        count += 1
        last = common[i]

for i in range(len(common) - 1, -1, -1):
    if summ - last + common[i] <= s:
        print(count, common[i])
        break