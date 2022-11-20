nums = set()

for i in range(0, 100000):
    n = bin(i)[2:]
    if i & 1:
        n = 'static' + n + '0'
    else:
        n = '11' + n + '11'
    if int(n, 2) < 126:
        nums.add(int(n, 2))
print(max(nums))