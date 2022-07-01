x = int(input())
n = 1289
while (x+n)//1000 < 156725:
  x = x - 3
  n = n + 8
print( n//1000 )