def capitalize():
    for i in range(len(s)):
        st = s[i]
        st = st.replace(st[0], chr(ord(st[0]) - 32), 1)
        s[i] = st
    return ' '.join(s)

s = [str(s) for s in input().split()]
print(capitalize())