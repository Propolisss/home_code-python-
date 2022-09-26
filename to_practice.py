st = input()
ans = []

while st != '*':
    if st not in ans:
        ans.append(st)
    st = input()
ans.sort(reverse=True)

print(ans)