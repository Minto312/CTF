import re
import netcat

def matrix_multiply(A, B, mod):
    return [[(A[i][0]*B[0][j] + A[i][1]*B[1][j]) % mod for j in range(2)] for i in range(2)]

def matrix_power(matrix, n, mod):
    result = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2:
            result = matrix_multiply(result, matrix, mod)
        n //= 2
        matrix = matrix_multiply(matrix, matrix, mod)
    return result

def fibonacci_mod(n, mod):
    matrix = [[1, 1], [1, 0]]
    return matrix_power(matrix, n, mod)[0][1]


n_re = re.compile(r'F\(([0-9][0-9]+)\)')
m_re = re.compile(r'% ([0-9]+)')
# nc = netcat.Netcat('35.78.8.36',38411) #2
nc = netcat.Netcat('35.78.8.36',38154) #3

while True:
    r = nc.read()
    print(r)
    n = n_re.search(r).group(1)
    print(n)
    m = m_re.search(r).group(1)
    print(m)
    
    ans = fibonacci_mod(int(n),int(m))
    print(ans)
    nc.write(ans)