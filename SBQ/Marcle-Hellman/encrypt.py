#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CyberQuest 2021 二次予選：crypto：Marcle-Hellmanナップサック暗号
from random import randint
from secret import flag, p


def main():
    assert flag[:11] == 'CyberQuest{'
    assert flag[-1] == '}'
    fb = ''
    for c in flag:
        fb += '%08d' % (int(bin(ord(c))[2:]))
    n = len(fb)
    w = [randint(1, 10)]
    for i in range(1, n):
        w.append(randint(sum(w[:i]) + 1, w[-1] * 3))
    w = [n % p for n in w]
    print('p =', p)
    print('w =', w)

    c = 0
    # print(fb)
    for i, b in enumerate(fb):
        c += int(b) * w[i] % p
        c %= p
        # print(c)
    print('c =', c)


if __name__ == '__main__':
    main()
