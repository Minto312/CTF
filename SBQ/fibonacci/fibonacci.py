import re
import netcat

class Fibonacci:
    def __init__(self):
        self.fiblist = [0, 1, 1]
        # self.solve_fibonacci(600000)
    
    def solve_fibonacci(self,n):
        if n < len(self.fiblist):
            return self.fiblist[n]
        else:
            while (len(self.fiblist) <= n):
                self.fiblist.append(self.fiblist[-1] + self.fiblist[-2])
            return self.fiblist[n]
fib = Fibonacci()
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
    nc.write(fib.solve_fibonacci(int(n)) % int(m))