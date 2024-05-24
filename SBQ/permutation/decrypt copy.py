import itertools
from tqdm import tqdm

c = 'bos_kQeu_DCuetyoyr{wttPeusbiun-_ionoStutn-Stoiwerkt-mroaNu__teuerFdtscarietnS}u utc ?l tr- re'
# c = 'bos_kQeu_DCuetyoyr{wttPeusbiun-_ionoStutn-Stoiwerkt-mroaNu__teuerFdtscarietnS}uutc?ltr-re'
key_frese = 'CyberQuest{'
# len(c) = 93 89

C   = 0
Y_1 = 1
B   = 2
E_1 = 3
R   = 4
Q   = 5
U_1 = 6
E_2 = 7
S   = 8
T   = 9
bracket = 10
U_2 = -6
Y_2 = -8


KEY_LENGTH = 19
k = [B,-1,S,-2,-3,Q,E_2,U_1,-4,-5,C,U_2,E_1,T,Y_1,-7,Y_2,R,bracket]
key = []
while len(key) < len(c):
    key += k

# 確定していない部分のカギ
random_key = [x for x in range(11,KEY_LENGTH)]
random_keys = list(itertools.permutations(random_key))

ex_csv = ''

decrypted = ['' for _ in range(len(key) + KEY_LENGTH)]
key_count = 0
for rnd_key in tqdm(random_keys):
    for i, k in enumerate(key):
        if i > len(c) - 1:
            break
        key_count = i // (KEY_LENGTH)
        
        if k < 0:
            decrypted[rnd_key[abs(k + 1)] + (KEY_LENGTH*key_count)] = c[i]
        else:
            decrypted[k + (KEY_LENGTH*key_count)] = c[i]
        
    # insert , to decrypted every KEY_LENGTH
    # d = ''
    # for i, x in enumerate(decrypted):
    #     if i % KEY_LENGTH == 0 and i != 0:
    #         d += ','
    #     d += x
    # ex_csv += d + '\n'
    if (''.join(decrypted)[:19] == 'CyberQuest{Do_you_k'):
        print(rnd_key)
    ex_csv += ''.join(decrypted) + '\n'

with open('ex.csv', 'w') as f:
    f.write(ex_csv)