file = open('26_2149.txt')
n, m = map(int, file.readline().split())
nums = sorted([int(i) for i in file])
vid = sorted(i for i in nums if i >= 101)
pic = sorted(i for i in nums if i < 101)
summ_pic = 0
summ_vid = 0
count = 0

while summ_vid < (m / 2):
    summ_vid += vid.pop(0)
    count += 1

last = 0
for i in range(len(pic)):
    if summ_pic + pic[i] <= (m - summ_vid):
        summ_pic += pic[i]
        count += 1
        last = pic[i]
for i in range(len(pic) - 1, -1, -1):
    if summ_pic - last + pic[i] <= (m - summ_vid):
        summ_pic += pic[i] - last
        break



print(m - summ_vid - summ_pic, count)