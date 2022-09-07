for i in range(17):
    summ1 = f'9759{int(str(i), 17)}'
    summ2 = f'3{int(str(i), 17)}108'
    summ = int(summ1, 17) + int(summ2, 17)
    if summ % 11 == 0:
        print(summ // 11)
        break