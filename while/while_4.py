x = int(input())
y = int(input())
k = 0

while x <= y:
    k += 1
    x = x + int(x * 0.1)
print(k)