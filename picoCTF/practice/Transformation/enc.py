
def enc():
    ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

    arr = []

    for i in range(0, len(flag), 2):
        arr += chr((ord(flag[i]) << 8) + ord(flag[i + 1]))


def dec():
    cipher = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ'

    ans = ''
    for c in cipher:
        c_int = ord(c)

        c_big = int(c_int >> 8)
        c_little = c_int - (c_big << 8)

        ans += chr(c_big) + chr(c_little)

    print(ans)

dec()