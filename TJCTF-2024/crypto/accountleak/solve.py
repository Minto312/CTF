# from math import lcm
def solve(c, n, dont_leak_this):
    from Crypto.Util.number import long_to_bytes
    from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
    from sympy import symbols, Eq, solve

    e = 65537

    # p と q をシンボルとして定義
    p, q, sub = symbols('p q sub', positive=True, integer=True)

    # 方程式を設定
    eq1 = Eq(p * q, n)
    eq2 = Eq(dont_leak_this - n, -sub*p + -sub*q + sub**2)

    solutions = solve((eq1, eq2), (p, q), dict=True)

    if solutions:
        for sol in solutions:
            p_val = sol[p].evalf()
            q_val = sol[q].evalf()

            # 解を整数として取得
            p_val =  int(p_val)
            q_val = int(q_val)
            
            print(f'p = {p_val}, q = {q_val}')
    else:
        print("No solution found.")

    phi_n = (p_val-1)*(q_val-1)
    d = pow(e, -1, phi_n)

    # 復号（通常の公開鍵 e で復号）
    decrypted_int = pow(c, d, n)
    return decrypted_int

import netcat
import re

nc = netcat.Netcat('tjc.tf', 31601)
c_re = re.compile(r'powerful numbers, (.*?) and')
n_re = re.compile(r'and (.*?)\n')
dont_leak_this_re = re.compile(r'[0-9]+')

nc.read()
r = nc.read()
print(r)
c = c_re.findall(r)[0]
n = n_re.findall(r)[0]

print(f'{c=}')
print(f'{n=}')

nc.write('yea')
nc.read()
r = nc.read()
print(r)
dont_leak_this = int(dont_leak_this_re.findall(r)[0])
print(f'{dont_leak_this=}')
nc.write(solve(int(c), int(n), dont_leak_this))
print(nc.read())