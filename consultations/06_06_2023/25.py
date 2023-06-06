from fnmatch import *
count = 0

for i in range(161, 17 * 10 ** 6 + 1, 161):
    if fnmatch(str(i), '*1?*?68*'):
        count += 1
        if count % 500 == 1:
            print(i, i // 161)