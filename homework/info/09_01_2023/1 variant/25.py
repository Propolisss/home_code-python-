def simple(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))



for i in range(33333, 55555 + 1):
    if simple(i) and sum(int(j) for j in str(i)) > 35:
        print(i, sum(int(j) for j in str(i)))