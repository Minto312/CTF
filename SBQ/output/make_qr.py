from PIL import Image
import os
os.chdir('SBQ/output')

# Read binary data from file
with open('binary_data.txt', 'r') as f:
    binary_data = f.readline()

out = ''
for i in binary_data:
    if i == 1:
        out += '■'
    else:
        out += '□'
    
        
print(out)