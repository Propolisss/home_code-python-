a = int(input())
b = int(input())

for i in range(a, b + 1):
    st = str(i)
    for j in range(len(st)):
        if st.count(st[j]) == 3:
            print(i)
            break