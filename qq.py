def simple(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def factorize(x):  ## define all simple dels of x
    a = []
    r = 2
    while x > 1 and r <= x:
        if x % r == 0:
            x //= r
            a.append(r)
        else:
            r += 1
    return a

simpledels = []  ## mas of simple numbers from 2 to 1000
for i in range(2, 1000):
    if simple(i):
        simpledels.append(i)

number_of_dels = 1600
mas = factorize(number_of_dels)
mas.sort()
mas.reverse()
mas_of_dels = []

for i in range(len(mas)):
    mas_of_dels.append(simpledels[i] ** (mas[i] - 1))
boolean = True
number = 1

while boolean == True:
    boolean = False
    for i in range(len(mas) - 1):
        current_position = mas_of_dels[-1] * mas_of_dels[i]
        possible_possition = simpledels[i] ** (mas[-1] * mas[i] - 1) - mas_of_dels[i]
        # print(current_position,possible_possition,mas_of_dels,mas)
        if current_position > possible_possition:
            mas_of_dels.pop(-1)
            mas[i] *= mas[-1]
            mas_of_dels[i] = simpledels[i] ** (mas[i] - 1)
            mas.pop(-1)
            boolean = True
            break

for i in range(len(mas_of_dels)):
    number *= mas_of_dels[i]

print(mas_of_dels)
print(number, int(mas_of_dels[-1] ** (1 / (mas[-1] - 1))))
