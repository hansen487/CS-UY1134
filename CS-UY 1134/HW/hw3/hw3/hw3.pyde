import ctypes
class MyList:
    def __init__(self,I=None):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        if I:
            self.extend(I)

    def __len__(self):
        return self._n

    def is_empty(self):
        return len(self)==0

    def append(self,x):
        if self._n==self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n]=x
        self._n+=1

    def extend(self,I):
        for x in I:
            self.append(x)

    def pop(self,i=-1):
        r=self[i]
        del self[i]
        return r

    def _resize(self,newsize):
        A=self._make_array(newsize)
        self._capacity=newsize
        for i in range(self._n):
            A[i]=self._A[i]
        self._A=A

    def _make_array(self,size):
        return (size*ctypes.py_object)()

    def __getitem__(self,i):
        if isinstance(i,slice):
            A=MyList()
            for j in range(*i.indices(self._n)):               
                A.append(self._A[j])
            return A
        if i<0:
            i=self._n+i
        return self._A[i]

    def __setitem__(self,i,x):
        if i<0:
            i=self._n+i
        self._A[i]=x

    def __iter__(self):
        for i in range(len(self)):
            yield self._A[i]

    def __str__(self):
        return "[" \
               +"".join( str(i)+"," for i in self[:-1]) \
               +(str(self[-1]) if not self.is_empty() else "") \
               +"]"

    def __delitem__(self,i):
        if isinstance(i,slice):
            A=MyList()
            for j in reversed(range(*i.indices(self._n))):               
                del self[j]
        else:
            if i<0:
                i=self._n+i
            for j in range(i,self._n-1):
                self._A[j]=self._A[j+1]
            self[-1]=None        
            self._n-=1

    def __add__(self,other):
        A=MyList(self)
        A.extend(other)
        return A

    def __mul__(self,times):
        A=MyList()
        for t in range(times):
            A.extend(self)
        return(A)

    __rmul__=__mul__

    def __contains__(self,x):
        for y in self:
            if x==y:
                return True
        return False

    def index(self,x):
        for i in range(len(self)):
            if self[i]==x:
                return i
        return None

    def count(self,x):
        c=0
        for y in self:
            if x==y:
                c+=1
        return c

    def remove(self,x):
        del self[self.index(x)]

    def reverse(self):
        for i in range(len(self)//2):
            A[i],A[-i]=A[-i],A[i]
            
x=MyList()

    