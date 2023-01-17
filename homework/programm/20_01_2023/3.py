from itertools import *

s = list(map(''.join, product('0123456789', repeat=6)))

ans = []

for i in range(len(s)):
    s1 = s[i][:3]
    s2 = s[i][-3:]
    if sum(int(j) for j in s1) == sum(int(j) for j in s2):
        if all(s1.count(s1[j]) == 1 and s2.count(s2[j]) == 1 for j in range(3)):
            if any(j in s2 for j in s1):
                if s1 != s2:
                    ans.append(s1 + '-' + s2)
print(len(ans))
