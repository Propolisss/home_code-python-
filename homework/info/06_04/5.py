money = [
    [51, 21, 93, 48, 45, 100, 67, 39, 18, 29],
    [57, 43, 97, 51, 92, 10, 93, 32, 19, 58],
    [63, 16, 31, 16, 78, 88, 90, 72, 37, 67],
    [10, 57, 64, 25, 96, 50, 81, 65, 91, 69],
    [99, 43, 95, 7, 40, 76, 18, 34, 5, 65],
    [35, 19, 71, 77, 64, 38, 62, 56, 10, 2],
    [100, 57, 27, 26, 51, 33, 100, 11, 53, 1],
    [11, 79, 49, 46, 37, 69, 80, 31, 25, 39],
    [22, 71, 20, 23, 11, 12, 39, 16, 64, 34],
    [4, 25, 87, 84, 30, 48, 77, 13, 40, 33]
]
maxx = [
    [51, 21, 93, 48, 45, 100, 67, 39, 18, 29],
    [57, 43, 97, 51, 92, 10, 93, 32, 19, 58],
    [63, 16, 31, 16, 78, 88, 90, 72, 37, 67],
    [10, 57, 64, 25, 96, 50, 81, 65, 91, 69],
    [99, 43, 95, 7, 40, 76, 18, 34, 5, 65],
    [35, 19, 71, 77, 64, 38, 62, 56, 10, 2],
    [100, 57, 27, 26, 51, 33, 100, 11, 53, 1],
    [11, 79, 49, 46, 37, 69, 80, 31, 25, 39],
    [22, 71, 20, 23, 11, 12, 39, 16, 64, 34],
    [4, 25, 87, 84, 30, 48, 77, 13, 40, 33]
]
minn = [
    [51, 21, 93, 48, 45, 100, 67, 39, 18, 29],
    [57, 43, 97, 51, 92, 10, 93, 32, 19, 58],
    [63, 16, 31, 16, 78, 88, 90, 72, 37, 67],
    [10, 57, 64, 25, 96, 50, 81, 65, 91, 69],
    [99, 43, 95, 7, 40, 76, 18, 34, 5, 65],
    [35, 19, 71, 77, 64, 38, 62, 56, 10, 2],
    [100, 57, 27, 26, 51, 33, 100, 11, 53, 1],
    [11, 79, 49, 46, 37, 69, 80, 31, 25, 39],
    [22, 71, 20, 23, 11, 12, 39, 16, 64, 34],
    [4, 25, 87, 84, 30, 48, 77, 13, 40, 33]
]

#путь для максимума
for col in range(10):
    for row in range(10):
        if col == 0:
            if row == 0:
                continue
            else:
                maxx[col][row] += maxx[col][row - 1]
        elif row == 0:
            maxx[col][row] += maxx[col - 1][row]
        else:
            maxx[col][row] += max(maxx[col - 1][row], maxx[col][row - 1])

#путь для минимума
for col in range(10):
    for row in range(10):
        if col == 0:
            if row == 0:
                continue
            else:
                minn[col][row] += minn[col][row - 1]
        elif row == 0:
            minn[col][row] += minn[col - 1][row]
        else:
            minn[col][row] += min(minn[col - 1][row], minn[col][row - 1])
print(maxx[9][9], minn[9][9])