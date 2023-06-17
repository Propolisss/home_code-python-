def f(start, count):
    if count == 7:
        return {start}
    else:
        return f(start + 1, count + 1) | f(start + 2, count + 1) | f(start * 2, count + 1)
print(len(f(1, 0)))