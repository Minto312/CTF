import itertools

t = 'rtcuertu'
out = ''
for x in itertools.permutations(t):
    out += 'S' + ''.join(x) + '\n'
with open('c.csv', 'w') as f:
    f.write(out)