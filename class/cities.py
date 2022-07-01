c1 = input()
c2 = input()
c3 = input()
max = max(len(c1), len(c2), len(c3))
min = min(len(c1), len(c2), len(c3))

if max == len(c1):
    max = c1
if min == len(c1):
    min = c1
if max == len(c2):
    max = c2
if min == len(c2):
    min = c2
if max == len(c3):
    max = c3
if min == len(c3):
    min = c3
print(min)
print(max)