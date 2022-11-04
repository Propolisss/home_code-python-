st = open('24-j9.txt').readline()

count = 0

for i in range(len(st) // 2):
    if st[i] == st[-i - 1]:
        count += 1
print(count)