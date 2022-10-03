# n = input()
#
# if (int(n[0]) + int(n[-1]) == int(n[1]) - int(n[2])):
#     print('ДА')
# else:
#     print('НЕТ')

n = int(input())

if ((n // 1000) + (n % 10)) == ((n // 100 % 10) - ((n % 100) // 10)):
    print('ДА')
else:
    print('НЕТ')