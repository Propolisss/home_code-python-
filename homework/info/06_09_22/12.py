def is_simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def digits_sum(n):
    summ = 0
    for i in range(len(n)):
        summ += int(n[i])
    return summ

for i in range(100):
    st = '>' + '0' * 39 + '1' * i + '2' * 39
    while '>1' in st or '>2' in st or '>0' in st:
        if '>1' in st:
            st = st.replace('>1', '22>', 1)
        if '>2' in st:
            st = st.replace('>2', '2>', 1)
        if '>0' in st:
            st = st.replace('>0', '1>', 1)
    st = st.replace('>', '')
    if is_simple(digits_sum(st)):
        print(i)
        print(digits_sum(st))
        break