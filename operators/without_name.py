count = 0
x = 0

while x < 300:
    x += 1
    s = 12 * (x // 10)
    n = 1
    while s < 300:
      s = s + 25
      n = n * 2
    if n > 500:
        count += 1
print(count)