st = open('24_2506.txt').readline()
dic = {let : st.count(let) for let in sorted(set(st))}
maxx = max(dic.values())
print([i for i in dic if dic[i] == maxx], maxx)