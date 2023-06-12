nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
ans = []
for a in range(55):
    n1 = nums.index('X') + nums.index('Y') * 55 + a * 55 ** 2 + nums.index('Z') * 55 ** 3
    n2 = nums.index('Y') + a * 55 + nums.index('X') * 55 ** 2 + 2 * 55 ** 3
    if (n1 - n2) % 29 == 0:
        print(a, abs(n1 - n2))
        ans.append([a, abs(n1 - n2)])
ans.sort()
print(ans[-1][1] - ans[0][1])