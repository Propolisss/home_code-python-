n = int(input())
s = []

for i in range(n):
    s.append(input())

search = input()

for i in range(n):
    if search.lower() in s[i].lower():
        print(s[i])