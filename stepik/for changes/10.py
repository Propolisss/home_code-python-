from fnmatch import *

z = 8 ** 888 + 15 * 15 ** 1515 - 2 ** 444
z = oct(z)[2:]

count = 0

for i in range(1, len(z)):
    if fnmatch(z[i - 1:i + 1], '7[123456]'):
        count += 1
print(count)