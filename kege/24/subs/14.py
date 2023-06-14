st = open('24_1145.txt').readline().strip()
st = st.split('D')
print(min(len(i) + 2 for i in st[1:-1] if len(i) > 0))