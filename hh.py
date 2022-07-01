def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


def simple(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def div(n):
    dels = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels.add(i)
            dels.add(n // i)
    return dels


def factorize(number):
    dels = list()
    i = 2
    while number != 1:
        if number % i == 0:
            number //= i
            dels.append(i)
            continue
        else:
            i += 1
    return dels


sim = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(sorted(factorize(1200)), len(factorize(1200)))
print(factorize(551350800), len(factorize(551350800)))
