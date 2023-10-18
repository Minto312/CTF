def trial_wheel_factorize(n: int):
    assert n > 1
    if n in [2, 3, 5]:
        return True
    elif n%2 == 0 or n%3 == 0 or n%5 == 0:
        return False
    i = 7
    c = 0
    wheel = [4, 2, 4, 2, 4, 6, 2, 6]
    while i < n**0.5+1:
        if n%i == 0:
            return False
        i += wheel[c%8]
        c += 1
    return True

for i in range(19992521826443995304719, 19992521826443995304719*5):
    if trial_wheel_factorize(i):
        print(i)
        break
    else:
        print('no')