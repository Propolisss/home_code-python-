# произведение цифр числа

def product_dig(n):
    prod = 1
    for i in str(n):
        if i.isdigit():
            prod *= int(i)
        else:
            return -1
    return prod


# нечетная перед четной

def is_correct(st):
    if st[0] in '02468':
        return False
    for i in range(1, len(st)):
        if st[i] in '02468' and st[i - 1] not in '13579':
            return False
    return True


# ровно 3 гласных

def is_3_alpha(st):
    gl = 'уеыаоэяиюeyuioa'
    count = 0

    for i in str(st):
        if i.lower() in gl:
            count += 1
        if count > 3:
            return False
    if count == 3:
        return True
    return False