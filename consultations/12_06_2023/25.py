from fnmatch import fnmatch

nech = '13579'
ch = '02468'

for i in range(2023, 10 ** 8 + 1, 2023):
    if fnmatch(str(i), f'11[{ch}]??[{nech}]11'):
        print(i, i // 2023)