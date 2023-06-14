st = open('24_279.txt').readline()
print(st.count('BOSS') - (st.count('JBOSS') + st.count('BOSSJ') - st.count('JBOSSJ')))