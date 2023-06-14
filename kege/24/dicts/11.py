count = 0

for s in open('24_2502.txt'):
    for i in range(len(s) - 3):
        if s[i] + s[i + 2 : i + 4] == 'KGE':
            count += 1
            break
print(count)