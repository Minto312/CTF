#!/usr/bin/env sagemath
# ref: https://kmyk.github.io/blog/writeups/ctf-2015-plaidctf-2015-lazy/
# load values
import ast

with open('pubkey.txt') as fh:
    b = ast.literal_eval(fh.read())
with open('ciphertext.txt') as fh:
    c = int(fh.read())
    
n = len(b)
print('[*] pubkey: b =', b)
print('[*] ciphertext: c =', c)

# check the density
d = float(n / log(max(b), 2))
print('[*] density: d =', d)


# low-density attack, CLOS method
# prepare a basis
MULTIPLIER = 100
B = matrix(ZZ, n + 1, n + 1)
B.set_block(0, 0, MULTIPLIER * matrix(n, 1, b))
B.set_block(n, 0, MULTIPLIER * matrix([ - c ]))
B.set_block(0, 1, 2 * identity_matrix(n))
B.set_block(n, 1, matrix([ -1 ] * n))
#print('[*] basis: B =', B)

# LLL algorithm
out_text = ''
for x in B.LLL():
    #if x[0] == 0 and all(x_i in [-1, +1] for x_i in x[1 :]):
    if 1:
        #print('[*] found: x =', x)

        # decode x
        m = 0
        for x_i in reversed(x[1 :]):
            m *= 2
            m += int(x_i == +1)
        print('[*] plaintext: m =', m)
        #print('[*]', repr(hex(m).decode('hex')))
        #print('[*]', repr(hex(m).decode('hex')))
        #out_text += f'm = {m}\n'
        #out_text += repr(hex(m).decode('hex')) + '\n\n'

# write the output
with open('a_out.txt', 'w') as f:
    f.write(out_text)