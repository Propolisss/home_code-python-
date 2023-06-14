st = open('24_2505.txt').readline()
dic = {let : 0 for let in sorted(set(st))}

for i in range(len(st) - 2):
    if st[i] == st[i + 2]:
        dic[st[i + 1]] += 1
maxx = max(dic.values())
print([i for i in dic if dic[i] == maxx], maxx)