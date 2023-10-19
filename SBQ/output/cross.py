import os
os.chdir('SBQ/output')

with open('output.txt', 'r') as f:
    lines = f.readlines()
    
txt = ''
for i, line in enumerate(lines):
    txt += line[i]
    
print(txt)