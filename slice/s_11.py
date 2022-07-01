s = input()

print(s[:s.find('h') + 1] + s[s.find('h') + 1:s.rfind('h')].replace('h', 'H')  + s[s.rfind('h'):])