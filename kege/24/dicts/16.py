st = open('24_2509.txt').readline().strip()
dic = {let : st.count(let) for let in sorted(set(st))}
print(max(dic.values()) - min(dic.values()))