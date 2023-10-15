c = 'bos_kQeu_DCuetyoyr{wttPeusbiun-_ionoStutn-Stoiwerkt-mroaNu__teuerFdtscarietnS}u utc ?l tr- re'
key_frese = 'CyberQuest{'

keys_point = {x:[] for x in key_frese}
for i, char in enumerate(c[0:19]):
    if char in key_frese:
        keys_point[char].append(i)
# print(keys_point)


maxm = 0
for x in keys_point.values():
    if min(x) > maxm:
        maxm = min(x)
# print(maxm)


count = 0
for x in c:
    if x == ' ':
        count += 1
# print(count)

# print(c[0:19])

# print(len(c))
# print(len('CyberQuest{Do_you_know_Substiution-Permuttion-tetwork-Strucaure_aNd_Fiiste  Srtt cu-nl}?eet'))


# ch = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j']
# t = ''
# tt = ''
# for i,x in enumerate(c):
#     if i % 19 == 0 and i != 0:
#         t += ','
#         tt += ','
#     t += x
#     tt += ch[i % 19]
# with open('crypto.csv', 'w') as f:
#     f.write(t + '\n')
#     f.write(tt)

print(c[0:31])
print(c[31:62])
print(c[62:93])
