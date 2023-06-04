def f(st):
    if len(st) == 20:
        return st[-1] != 'Г'
    summ = 0

    for i in 'ГОЛ':
        if st[-1] != i:
            if st[-1] == 'Г':
                summ += f(st + i) if i != st[-2] else 0
            else:
                summ += f(st + i)
    return summ
print(sum(f(let) for let in 'ОЛ'))