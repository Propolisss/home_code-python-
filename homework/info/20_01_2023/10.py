file = open('10.txt')

s = []

for i in file:
    s.extend(i.split())

for i in range(len(s)):
    temp = ''

    for j in range(len(s[i])):
        if s[i][j].isalpha():
            temp += s[i][j]
    s[i] = temp

count = 0

for i in s:
    if any(i.lower() == word for word in ['конь', 'коня','коню','конем','конём','коне','кони','коней','коням','коней','конями','конях']):
        print(i.lower())
        count += 1
print(count)