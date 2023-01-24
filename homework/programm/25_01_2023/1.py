file = open('27-B.txt')
n = int(file.readline())
nums = [int(file.readline()) for _ in range(n)]
count = 0
stack = []

for i in range(len(nums)):
    stack = []
    for j in range(i, len(nums)):
        if len(stack) < 20:
            stack.append(nums[j])
        else:
            break
        if sum(stack) % 39 == 0:
            count += 1
print(count)