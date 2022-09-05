nums = set()
count = 0

for i in range(100000):
    temp_bin_num = oct(i)[2:]
    if len(temp_bin_num) == 5:
        nums.add(temp_bin_num)

for i in nums:
    if i.count('6') == 1:
        index_of_six = i.find('6')
        if index_of_six == 0:
            if int(i[index_of_six + 1]) % 2 == 0:
                count += 1
        elif index_of_six == len(i) - 1:
            if int(i[index_of_six - 1]) % 2 == 0:
                count += 1
        else:
            if int(i[index_of_six + 1]) % 2 == 0 and int(i[index_of_six - 1]) % 2 == 0:
                count += 1
print(count)