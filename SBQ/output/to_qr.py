import os
os.chdir('SBQ/output')
import re

with open('output.txt', 'r') as f:
    lines = f.readlines()
    
txt = ''
for line in lines:
    line = re.sub(r'[^a-zA-Z0-9]', '0,', line)
    line = re.sub(r'[a-zA-Z1-9]', '1,', line)
    txt += line + '\n'

with open('out.txt', 'w') as f:
    f.write(txt)