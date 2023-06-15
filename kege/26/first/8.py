file = open('26_507.txt')
n = int(file.readline())
nums = sorted(int(i) for i in file)
maxx1 = max(nums) * 0.6
summ1 = sum(nums[int(n * 0.7) + 1:]) * 0.6 + sum(nums[:int(n * 0.7) + 1]) * 0.7
maxx2 = max(nums) * 0.65
summ2 = sum(nums[int(n * 0.5) + 1:]) * 0.65 + sum(nums[:int(n * 0.5) + 1]) * 0.6
if summ1 > summ2:
    print(abs(int(summ1 - summ2)), int(maxx1))
else:
    print(abs(int(summ2 - summ1)), int(maxx2))
#питон считает неправильно первое число, но в экселе мне лень делать