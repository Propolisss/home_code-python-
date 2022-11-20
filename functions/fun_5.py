#def pos(n):
#    n = int(input())
#    if n == 0:
#       print(n)
#    else:
#        return pos(n - static), print(n)
#
#n = 0
#pos(n)

def pos():
    n = int(input())
    if n != 0:
        pos()
    print(n)
 
pos()