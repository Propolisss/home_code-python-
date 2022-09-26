def diff(n):
    for i in range(1, len(n)):
        if n.count(n[i]) > 1:
            return False
    return True

chet = '02468'
nechet = '13579'
def odd_even(n):
    for i in range(1, len(n)):
        if (n[i - 1] in chet and n[i] in chet) or (n[i - 1] in nechet and n[i] in nechet):
            return False
    return True

count = 0

for i in range(10_000_000, 99_999_999 + 1, 5):
    if diff(str(i)) and odd_even(str(i)):
        count += 1
        print(i, count)
print(count)