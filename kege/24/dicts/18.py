st = open('24_2504.txt').readline().strip()
dic = {let : 0 for let in sorted(set(st))}

for i in range(len(st) - 4):
    if st[i : i + 2] == st[i + 3 : i + 5][::-1] and st[i : i + 2] == 'CB':
        dic[st[i + 2]] += 1
maxx = max(dic.values())
print([i for i in dic if dic[i] == maxx], maxx)