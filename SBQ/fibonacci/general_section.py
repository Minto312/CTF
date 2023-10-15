from fractions import Fraction
import sys
import re
import netcat
sys.setrecursionlimit(15000)

def fibMul(fn1, fn2):
    a = fn1[0]
    b = fn1[1]
    c = fn2[0]
    d = fn2[1]
    return (a*c + 5*b*d, a*d + b*c)

def fibExp(fn, n):
    if (n == 0):
        return (Fraction(1), Fraction(1))
    if (n % 2 == 0):
        return fibExp(fibMul(fn, fn), n / 2)
    return fibMul(fn, fibExp(fn, n - 1))

def fibMin(fn1, fn2):
    a = fn1[0]
    b = fn1[1]
    c = fn2[0]
    d = fn2[1]
    return (a - c, b - d)

def fibMain(n):
    fibNum1 = (Fraction(1, 2), Fraction( 1, 2))
    fibNum2 = (Fraction(1, 2), Fraction(-1, 2))

    fibNum3 = fibMin(fibExp(fibNum1, n), fibExp(fibNum2, n)) 
    fibNum4 = (Fraction(0, 1), Fraction(1, 5))
    return fibMul(fibNum3, fibNum4)

def fib(n):
    return fibMain(n)[0].numerator

n_re = re.compile(r'F\(([0-9][0-9]+)\)')
m_re = re.compile(r'% ([0-9]+)')
# nc = netcat.Netcat('35.78.8.36',38411) #2
nc = netcat.Netcat('35.78.8.36',38412) #3

while True:
    r = nc.read()
    print(r)
    n = n_re.search(r).group(1)
    print(n)
    m = m_re.search(r).group(1)
    print(m)
    nc.write(fib(int(n)) % int(m))