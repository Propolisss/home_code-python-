s = open('24_634.txt')
count = 0

for i in s:
    if any(f'Z{let}RO' in i for let in set(i)):
        count += 1
print(count)