n = int(input())
s = []

for i in range(n):
    s.append(input())

k = int(input())
searches = []

for i in range(k):
    searches.append(input())

for i in range(n):
    if all(searches[j].lower() in s[i].lower() for j in range(k)):
        print(s[i])