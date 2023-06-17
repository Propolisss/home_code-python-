st = 'АВГ БДЗВА ВГИЗ ГИЕ ДЗК ЕИМ ЖВЗЛ З ИЛ ЛЗК МЛ'
dic = {s[0] : s[1:] for s in st.split()}
ans = set()
def f(start, end):
    if start[-1] == end:
        ans.add(start)
        return 1
    return sum(f(start + let, end) for let in dic[start[-1]] if let not in start)
print(f('А', 'К'))
print(max(len(i) for i in ans) - 1)