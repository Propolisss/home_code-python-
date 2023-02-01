from itertools import *
count = 0


for i in range(1, 1_000_000):
    n = oct(i)[2:]
    if len(n) == 5:
        if (n.count('6') == 1) and all(j not in n for j in ['16', '61', '36', '63','56', '65', '76', '67']):
            count += 1
print(count)