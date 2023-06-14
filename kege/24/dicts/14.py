st = open('24_836.txt').readline()
count = 0

for i in range(len(st) - 4):
    if st[i : i + 5] == st[i : i + 5][::-1]:
        count += 1
print(count)