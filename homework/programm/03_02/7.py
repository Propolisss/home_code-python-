minn = 0
d = 0
count = 0

def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for j in range(268312, 336492 + 1):
    d = 0
    for k in range(2, int(j ** 0.5) + 1):
        if j % k == 0:
            if simple(k):
                if j // k != k:
                    d = j // k
                    if simple(d):
                        count += 1
                        if count == 1:
                            minn = j
print(count, minn)