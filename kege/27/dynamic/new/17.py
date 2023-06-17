file = open('27A_2758.txt')
n = int(file.readline())
ch = [float('inf')] * 1071
nech = [float('inf')] * 1071
nums = [int(i) for i in file]
minn = float('inf')

for i in range(11 + 1):
    x = nums[i]
    ost = (1071 - x % 1071) % 1071
    if x % 2 == 0:
        minn = min(minn, x + ch[ost])
    else:
        minn = min(minn, x + nech[ost])

    if x % 2 == 0:
        ch[x % 1071] = min(ch[x % 1071], x)
    else:
        nech[x % 1071] = min(nech[x % 1071], x)

for i in range(11 + 1, n):
    ost = nums[i - (11 + 1)] % 1071
    if nums[i - (11 + 1)] % 2 == 0:
        ch[ost] = float('inf')
    else:
        nech[ost] = float('inf')

    x = nums[i]
    ost = (1071 - x % 1071) % 1071
    if x % 2 == 0:
        minn = min(minn, x + ch[ost])
    else:
        minn = min(minn, x + nech[ost])

    if x % 2 == 0:
        ch[x % 1071] = min(ch[x % 1071], x)
    else:
        nech[x % 1071] = min(nech[x % 1071], x)
print(minn)