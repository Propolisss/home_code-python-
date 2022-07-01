n = int(input())
nums = [[0] * n for i in range(n)]
num = 1

for i in range(n):
    st = input()
    for j in range(len(st)):
        if int(st[j]) == 0:
            nums[i][j] = 10 ** 9
        else:
            nums[i][j] = int(st[j])

for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                continue
            else:
                nums[i][j] += nums[i][j - 1]
        elif j == 0:
            nums[i][j] += nums[i - 1][j]
        else:
            nums[i][j] += min(nums[i - 1][j], nums[i][j - 1])

if nums[n - 1][n - 1] > 10 ** 9:
    print('Impossible')
else:
    col = n - 1
    row = n - 1
    nums[n - 1][n - 1] = '#'

    while col > 0:
        while row > 0:
            if nums[col - 1][row] < nums[col][row - 1]:
                nums[col - 1][row] = '#'
                col -= 1
            else:
                nums[col][row - 1] = '#'
                row -= 1
            if col == 0:
                while row != 0:
                    nums[col][row - 1] = '#'
                    row -= 1
            if row == 0:
                while col != 0:
                    nums[col - 1][row] = '#'
                    col -= 1
    for i in range(n):
        st = ''
        for j in range(n):
            if nums[i][j] != '#':
                st += '-'
            else:
                st += '#'
        print(st)