import os
os.chdir('SBQ/output')
import re

with open('output.txt', 'r') as f:
    lines = f.readlines()
    
txt = ''
for line in lines:
    txt += line[:len(line)-1]

for c in txt:
    if not re.match(r'[a-zA-Z0-9+/=]', c):
        txt = txt.replace(c, '')

new_txt = ''
for i, c in enumerate(txt):
    new_txt += c
    if i % 64 == 0 and i != 0:
        # new_txt += '\n'
        pass

with open('out.txt', 'w') as f:
    f.write(new_txt)