st = open('24_2251.txt').readline()
st = st.split('D')
maxx = float('-inf')

for i in range(len(st) - 2):
    maxx = max(maxx, len(st[i]) + len(st[i + 1]) + len(st[i + 2]) + 2)
print(maxx)