n = int(input())
s = []

for i in range(n):
    temp_st = input()
    if (temp_st not in s):
        s.append(temp_st)

print(*s, sep='\n')

