st = open('24_2250.txt').readline().strip()
st = st.split('A')
maxx = float('-inf')

for i in range(len(st) - 1):
    maxx = max(maxx, len(st[i]) + len(st[i + 1]) + 1)
print(maxx)