import re
import netcat

class Fibonacci:
    def __init__(self):
        self.fiblist = [0, 1, 1]
    
    def solve_fibonacci(self,n):
        if n < len(self.fiblist):
            return self.fiblist[n]
        else:
            while (len(self.fiblist) <= n):
                self.fiblist.append(self.fiblist[-1] + self.fiblist[-2])
            return self.fiblist[n]

fib = Fibonacci()
fib.solve_fibonacci(int(1e5))
n_re = re.compile(r'F\(([0-9]+)\)')
m_re = re.compile(r'% ([0-9]+)')
# nc = netcat.Netcat('35.78.8.36',38411) #2
nc = netcat.Netcat('35.78.8.36',38412) #3
while True:
    r = nc.read()
    print(r)
    n = n_re.findall(r)[-1]
    m = m_re.findall(r)[-1]
    nc.write(fib.solve_fibonacci(int(n)) % int(m))