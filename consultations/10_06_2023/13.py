st = 'ABM BCM CDN DEG EF GFE HGN MCNH NGD TAMHF'
dic = {s[0] : s[1:] for s in st.split()}

def f(start, end):
    if start[-1] == end:
        return ('C' in start or 'G' in start)
    return sum(f(start + let, end) for let in dic[start[-1]] if let not in start)
print(f('T', 'F'))