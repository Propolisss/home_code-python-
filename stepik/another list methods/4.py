n = int(input()[1:])
ss = []

for i in range(n):
    s = input().split('#')
    ss.append(s[0].rstrip())

print(*ss, sep='\n')