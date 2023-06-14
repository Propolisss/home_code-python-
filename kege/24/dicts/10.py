count = 0

for s in open('24_587.txt'):
    if (s.count('B') * 100) >= (105 * s.count('A')):
        count += 1
print(count)