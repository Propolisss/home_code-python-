with open('17 (3).txt') as file:
    nums = [int(i) for i in file]

def to_five(n):
    temp_st = ''
    temp_num = n

    while temp_num:
        temp_st += str(temp_num % 5)
        temp_num //= 5
    return temp_st[::-1]


def to_nine(n):
    temp_st = ''
    temp_num = n

    while temp_num:
        temp_st += str(temp_num % 9)
        temp_num //= 9
    return temp_st[::-1]

ans = []

for i in nums:
    if (to_five(i)[-1] == '3') and (to_nine(i)[-1] == '5') and (oct(i)[-1] != '7'):
        ans.append(i)
print(len(ans), max(ans))







