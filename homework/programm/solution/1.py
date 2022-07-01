st = input()

print(st[st.rfind(' '):] + ' ' + st[:st.find(' ')])