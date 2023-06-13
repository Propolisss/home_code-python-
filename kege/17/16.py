nums = [int(i) for i in open('17_2309.txt')]
k11 = [i for i in nums if i % 11 == 0]
k17 = [i for i in nums if i % 17 == 0]

if len(k11) > len(k17):
    print(len(k11), min(k11))
else:
    print(len(k17), max(k17))