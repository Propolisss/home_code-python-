nums = [i.replace(';', ' ').split() for i in open('22.txt')]
dic = {'0' : 0}

while len(dic) < len(nums) + 1:
    for s in nums:
        if all(sub in dic for sub in s[2:]):
            if s[2] == '0':
                dic[s[0]] = int(s[1]) + max(dic[sub] for sub in s[2:])
            else:
                dic[s[0]] = int(s[1]) + max(dic[sub] for sub in s[2:]) + 5
print(max(dic.values()))