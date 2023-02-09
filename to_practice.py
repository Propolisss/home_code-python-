process = [i.split() for i in open('22.txt')]
def find_min_process(cores_):
    minn_ = float('inf')
    ind_ = ''

    for i in range(len(cores_)):
        summ_ = 0
        for j in range(len(cores_[i])):
            if cores_[i][j][0] in dic:
                summ_ += int(cores_[i][j][1])
        if summ_ < minn_:
            minn_ = summ_
            ind_ = i
    return ind_, minn_
core = 3
cores = [[] for _ in range(core)]
dic = {'0' : 0}
count_zeroes = 0
for i in process:
    if i[2] == '0':
        count_zeroes += 1



count = 0
f = False
while len(dic) < len(process) + 1:
    for elem in process:
        if elem[0] not in dic:
            if elem[2] == '0':
                flag = False
                for i in range(core):
                    if len(cores[i]) == 0:
                        cores[i].append(elem)
                        dic[elem[0]] = int(elem[1])
                        flag = True
                        count += 1
                        break
                if not flag:
                    ind, summ = find_min_process(cores)
                    cores[ind].append(elem)
                    dic[elem[0]] = int(elem[1])
                    count += 1
            else:
                if count == count_zeroes and all(sub in dic for sub in elem[2:]):
                    ind, summ = find_min_process(cores)
                    cores[ind].append(elem)
                    dic[elem[0]] = int(elem[1])
last = []
inner_maxx = float('-inf')

for i in cores:
    inner_summ = 0
    for j in range(len(i)):
        if max(dic[sub] for sub in i[j][2:]) > inner_summ:
            inner_summ += max(dic[sub] for sub in i[j][2:]) - inner_summ + dic[i[j][0]]
        else:
            inner_summ += dic[i[j][0]]
    if inner_summ > inner_maxx:
        inner_maxx = inner_summ
        last = [int(i[j][0]), inner_summ]
print(sum(last))