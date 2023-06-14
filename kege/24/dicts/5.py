st = open('24_2498.txt').readline()
count = 0

for i in range(len(st) - 2):
    if st[i : i + 3] == 'XIX':
        count += 1
print(count)