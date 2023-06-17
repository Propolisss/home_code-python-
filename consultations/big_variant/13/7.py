st = 'ABD BCFE CG DCGH EKF FCKL GM KL LGM MH'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return 'C' in start or 'L' in start
    return sum(f(start + let, end) for let in dic[start[-1]] if let not in start)
print(f('A', 'H'))