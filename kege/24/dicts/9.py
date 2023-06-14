count = 0

for i in open('24_859.txt'):
    if i.count('S') == i.count('X'):
        count += 1
print(count)