#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# CyberQuest 2023 二次選考：フィボナッチ数列 Easy：接続スクリプト
#   nc cq-quest.singularitybattlequest.club 38410
# 前提パッケージ
#   https://pypi.org/project/pwntools/
#     「Installation」を参考にしてください。
from pwn import *
import binascii


SERVER = ('cq-quest.singularitybattlequest.club', 38410)


response = b''


def title(conn):
    r = conn.recvline() # フィボナッチ数列の一般項を答えてください。
    print(r.decode(), end='')
    r = conn.recvline() #   F(1) = 1
    print(r.decode(), end='')
    r = conn.recvline() #   F(2) = 1
    print(r.decode(), end='')
    r = conn.recvline() #   F(n) = F(n-1) + F(n-2) ただしn>=3
    print(r.decode(), end='')
    r = conn.recvline() # 
    print(r.decode(), end='')


def round(conn):
    r = conn.recvline() # Round ? / 10
    print(r.decode(), end='')
    r = conn.recvuntil(b' = ') #   F(2) = 
    print(r.decode(), end='')

    # 答えの入力（キーボードから入力）
    ans = input().strip()
    conn.send(ans.encode() + b'\n')

    # 正答判定
    r = conn.recvline() # Correct. または Wrong.
    print(r.decode(), end='')
    if b'Correct' in r:
        return True
    else:
        return False


def main():
    conn = remote(*SERVER)

    # 接続時の表示情報
    title(conn)

    # ラウンド処理
    for _ in range(10):
        if not round(conn):
            # 不正解
            # コネクション切断
            conn.close()
            exit()

    # フラグゲット
    r = conn.recvline() # 
    print(r.decode(), end='')

    # コネクション切断
    conn.close()


if __name__ == '__main__':
    main()
