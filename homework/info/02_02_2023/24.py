s = open('24.txt').readline().replace('D', 'C').replace('F', 'C').replace('O', 'A').replace('CA', '*')
maxx = float('-inf')

for i in range(len(s)):
    count = 0
    for j in range(i, len(s)):
        if s[j] == '*':
            count += 1
        else:
            break
    maxx = max(maxx, count)
print(maxx)