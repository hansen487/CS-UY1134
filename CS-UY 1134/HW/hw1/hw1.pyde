#hc1941
#Problem 1
"""
runtime of example1 is O(n)
runtime of example2 is O(n2)
runtime of example3 is O(n^2)
runtime of example4 is O(n) 
runtime of example5 is O(n^3)
"""

#Problem 2
def merge(l1, l2):
    #output=[]
    if len(l1)>=len(l2):
        longer=l1
        shorter=l2
    else:
        longer=l2
        shorter=l1
    for i in range(len(shorter)):
        yield l1[i]
        yield l2[i]
    for j in range(len(shorter), len(longer)):
        yield longer[j]
print([i for i in merge( range(5),range(100,105))])    
print([i for i in merge( range(5),range(100,101))])
print([i for i in merge( range(1),range(100,105))])

#Problem 3
class polynomial():
    def __init__(self, constants):
        self.constants=constants 
        self.poly=''
        self.sum=0
    def evaluate(self, input):
        self.input=input
        self.sum=0
        for k in range(len(self.constants)):
            self.sum+=self.constants[k]*(self.input**(len(self.constants)-k-1))
        return self.sum
    def __str__(self):
        for j in range(len(self.constants)-1):
            self.poly+=str(self.constants[j])+'x^'+str(len(self.constants)-1-j)+'+'
        self.poly+=str(self.constants[j+1])
        return str(self.poly)

P=polynomial((6,2,1,8))
print(str(P))
print([P.evaluate(i) for i in range(10)])

#Problem 4
def sigma(f, first, last):
    sum=0
    for i in range(first, last+1):
        sum+=f(i)
    return sum
def f(n):
    return 1/pow(2,n)
print(sigma(f,2,10))