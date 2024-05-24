#!/usr/local/bin/python3.10 -u

import time
from Crypto.Util.number import getPrime, getRandomInteger, getRandomNBitInteger

flag = 'tjctf{1m4g1n3_7h3_4cc0un7_h4ck1n6_4nd_d14m0nd5_4r3_r34l_7h1n65}'
p = getPrime(512)
q = getPrime(512)

sub = getRandomInteger(20)

# hehe u cant guess it since its random :P
my_password = getRandomNBitInteger(256)

n = p*q
c = pow(my_password, 65537, n)
dont_leak_this = (p-sub)*(q-sub)

def solve(n, c, dont_leak_this):
    from sympy import symbols, Eq, solve
    from Crypto.Util.number import inverse, long_to_bytes, isPrime
    import math
    import time


    # p と q をシンボルとして定義
    p, q = symbols('p q')

    # 方程式を設定
    eq1 = Eq(p * q, n)

    # 探索開始時間を記録
    start_time = time.time()

    # n の平方根付近から探索を始める
    sqrt_n = int(math.isqrt(n))

    # 20ビットの全ての可能なsubの値を試す
    found = False
    for _sub in range(524288, 1048575):
        # 方程式を設定
        eq2 = Eq((p - _sub) * (q - _sub), dont_leak_this)
        
        # 連立方程式を解く
        solutions = solve((eq1, eq2), (p, q), dict=True)

        # 解の存在を確認
        if solutions:
            for sol in solutions:
                p_val = sol[p]
                q_val = sol[q]
                
                # 解を整数として取得
                p_val = int(p_val)
                q_val = int(q_val)

                # p と q が素数かどうかを確認
                if p_val > 0 and q_val > 0 and isPrime(p_val) and isPrime(q_val) and p_val * q_val == n:
                    p, q = p_val, q_val
                    found = True
                    break

            if found:
                break

        # # 計算時間が2.5秒を超えたら終了
        # if time.time() - start_time > 2.5:
        #     raise TimeoutError("Calculation time exceeded 2.5 seconds")

    if not found:
        raise ValueError("No valid solution found within the given time.")

    # 秘密鍵を求める
    e = 65537
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)

    # my_passwordを復号
    my_password = pow(c, d, n)
    print(f'my_password = {my_password}')
    return my_password

    # my_passwordをバイト列に変換して表示





def gamechat():
    print("<Bobby> i have an uncrackable password maybe")
    print(f"<Bobby> i'll give you the powerful numbers, {c} and {n}")
    print("<Bobby> gl hacking into my account")
    print("<Bobby> btw do you want to get my diamond stash")
    print("<Bobby> i'll send coords")
    print(f"<Bobby> {dont_leak_this}")
    print("<Bobby> oop wasnt supposed to copypaste that")
    print("<Bobby> you cant crack my account tho >:)")
    tic = time.time()
    resp = solve(n, c, dont_leak_this)
    toc = time.time()
    print(resp.strip())
    if (toc-tic >= 2.5):
        print("<Bobby> you know I can reset my password faster than that lol")
    elif (resp.strip() != str(my_password)):
        print("<Bobby> lol nice try won't give password that easily")
    else:
        print("<Bobby> NANI?? Impossible?!?")
        print("<Bobby> I might as wel give you the flag")
        print(f"<Bobby> {flag}")
    print("Bobby has left the game")


gamechat()
