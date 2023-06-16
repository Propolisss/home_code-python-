file = open('26_838.txt')
n = int(file.readline())
disk1 = []
disk2 = []
nums = sorted(int(i) for i in file)

while len(nums) > 0:
    disk1.append(nums[-1])
    del nums[-1]
    if len(nums) == 0:
        break
    while len(nums) > 0 and sum(disk1) > sum(disk2):
        disk2.append(nums.pop(0))
print(len(disk1), len(disk2))