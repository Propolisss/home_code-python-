cubes = []

for i in range(3, 1000, 2):
    cubes.append(i ** 3)

def dels(n):
    temp_dels = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if (i in cubes):
                temp_dels.add(i)
            if ((n // i) in cubes):
                temp_dels.add(n // i)
    return temp_dels

for i in range(228224, 531135 + 1):
    if len(dels(i)) >= 4:
        print(len(dels(i)), max(dels(i)))