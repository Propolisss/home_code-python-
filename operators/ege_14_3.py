z = (5**300 *   15**100) - (25**50 + 125**100)
summ = 0
last = 0

while z > 0:
    last = z % 5
    if last != 4:
        summ += last
    z //= 5
print(summ)