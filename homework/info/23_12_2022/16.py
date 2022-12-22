n1 = 1
prev = 1
n2 = 1
prev = 1

for i in range(2, 1000 + 1):
    prev = n1
    n1 = i * prev - 1

for i in range(2, 997 + 1):
    prev = n2
    n2 = i * prev - 1

print(n1 // n2)