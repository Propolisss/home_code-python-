for i in range(15):
    summ1 = f'82{int(str(i), 15)}19'
    summ2 = f'6{int(str(i), 15)}073'
    summ = int(summ1, 15) - int(summ2, 15)
    if summ % 11 == 0:
        print(summ // 11)
        break