from __future__ import print_function
import timeit

def timeFunction(f, n, repeat=1):
    return timeit.timeit(f.__name__ + '(' + str(n) + ')', setup="from __main__ import " + f.__name__, number=repeat) / repeat
'''
def fib1(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib1(x - 1) + fib1(x - 2)

def fib2(x):
    A = []
    A.append(0)
    A.append(1)
    for i in range(2, x + 1):
        A.append(A[i - 1] + A[i - 2])
    return A[x]

def fib3(x):
    if x == 0:
        return 0
    else:
        a = 0
        b = 1
        for i in range(x - 1):
            a, b = b, a + b
        return(b)

def printFunctionTimes(func, func_range):
    for i in func_range:
        for j in func:
            print("n=",i, j.__name__, round(timeFunction(j, i),8),end="\t")
        print('\n')

printFunctionTimes((fib1,fib2,fib3),range(5,40,5))
class functionPlotter:
    def __init__(self, f,inc=1):
        self.f=f
        self.i=1
        self.inc=inc
        self.nexttime=[]
        self.maximum=0
        self.scale=0
    def timeNext(self):
        self.nexttime.append(timeFunction(self.f, self.i))
        self.i+=1
    def plot(self):
        self.maximum=max(self.nexttime)
        if self.maximum==0:
            self.maximum=1
        self.scale=500/self.maximum-1
        for i in range(1,len(self.nexttime)):
            line(i, self.nexttime[i-1]*self.scale,i+1, self.nexttime[i]*self.scale)
def setup():
    size(500,500)
    global fp
    fp=functionPlotter(fib1)

def draw():
    global fp
    background(255)
    fp.timeNext()
    fp.plot()
            
'''
def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                     # create new list of n zeros
    for j in range(n):
        total = 0                     # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)          # record the average
    return A

def runprefix_average1(n):
    prefix_average1(range(n))

def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                     # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j + 1]) / (j + 1)  # record the average
    return A

def runprefix_average2(n):
    prefix_average2(range(n))


def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                   # create new list of n zeros
    total = 0                     # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j]               # update prefix sum to include S[j]
        A[j] = total / (j + 1)        # compute average based on current sum
    return A

def runprefix_average3(n):
    prefix_average3(range(n))
    
class functionsPlotter:
    def __init__(self, functions, colors, inc):
        self.functions=functions
        self.colors=colors
        self.i=1
        self.inc=inc
        self.times=[]
        self.scale=0
    def timeNext(self):
        for j in self.functions:
            self.times.append(timeFunction(j, self.i))
        self.i+=self.inc
    def plot(self):
        self.scale=max(self.times)
        if self.scale==0:
            self.scale=1
        self.scale=500/self.scale-1
        for k in range(0,len(self.times)-3,3):
            stroke(*self.colors[0])
            line(k, self.times[k]*self.scale, k+3, self.times[k+3]*self.scale)
            stroke(*self.colors[1])
            line(k, self.times[k+1]*self.scale, k+3, self.times[k+4]*self.scale)
            stroke(*self.colors[2])
            line(k, self.times[k+2]*self.scale, k+3, self.times[k+5]*self.scale)
def setup():
    size(500,500)
    global fp
    fp=functionsPlotter((runprefix_average1,runprefix_average2,runprefix_average3),((255,0,0),(0,255,0),(0,0,255)),10)

def draw():
    global fp
    background(255)
    fp.timeNext()
    fp.plot()