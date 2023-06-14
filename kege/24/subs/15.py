st = open('24_1146.txt').readline()
# st = st.replace('A', ' ').replace('B', ' ').replace('C', ' ').replace('E', ' ').replace('F', ' ')
# print(min(len(i) for i in st.split()))
minn = float('inf')
count = 1

for i in range(len(st) - 1):
    if st[i] == st[i + 1] == 'D':
        count += 1
    else:
        minn = min(minn, count) if count > 1 else minn
        count = 1
minn = min(minn, count) if count > 1 else minn
print(minn)