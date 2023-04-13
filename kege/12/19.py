a = 'КАРА'
i = len(a) - 1
k = 1
b = 'Т'

while i > 0:
    c = a[i]
    b += c
    i = i - k
print(b)