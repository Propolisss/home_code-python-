s = [i for i in open('24-164.txt')]
lens = []
dic = [[0] * len(s) for _ in range(256)]

maxx_len = float('-inf')
for i in range(len(s)):
    st = ''
    local_max = float('-inf')
    for j in range(len(s[i])):
        dic[ord(s[i][j])][i] += 1
        st = s[i][j]
        k = j + 1

        while k < len(s[i]):
            if st[-1] == s[i][k]:
                st += s[i][k]
                k += 1
            else:
                break

        maxx_len = max(maxx_len, len(st))
        local_max = max(local_max, len(st))
    lens.append(local_max)

row = lens.index(maxx_len)

maxx_let = float('-inf')
count_maxx_let = 0

for i in range(len(dic)):
    if dic[i][row] > count_maxx_let:
        count_maxx_let = dic[i][row]
        maxx_let = i

print(chr(maxx_let), sum(dic[maxx_let]), sep='')