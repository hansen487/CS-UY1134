class HT:
    class _Item:
        __slots__= '_key', '_value'
        def __init__(self, k, v):
            self._key = k            
            self._value = v 
            
    def __init__(self):
        self.h0 = []
        self.h1 = []
        self.minus = 0
    
    def __getitem__(self, key):
        for item in self.h0:
            if key == item._key:
                yield item._value
        for item in self.h1:
            if key == item._key:
                yield item._value
    
    def __setitem__(self, k, v):
        digits = []
        for char in str(k):
            digits.append(char)
        digit = int(digits.pop(0))
        for item in self.h0:
            if digit == item._key:
                oldvalue = item._value
                item._value = v
                while digit in self.h1:
                    for item1 in self.h1:
                        if item1._key == digit:
                            oldervalue = item1._value
                            item1._key = oldvalue
                            oldvalue = oldervalue
                            if len(digits) != 1:
                                digit = digits.pop[0]
                            else:
                                digit += 10
                self.h1.append(self._Item(digit,oldvalue))
                return
        self.h0.append(self._Item(digit, v))
        
    def __len__(self):
        return len(self.h0) + len(self.h1) - self.minus
        
    def __delitem__(self, k):
        digits = []
        for char in str(k):
            digits.append(char)
        digit = int(digits.pop(0))
        for item in self.h0:
            if item._key == digit:
                item._value = None
                self.minus += 1
        for item1 in self.h1:
            if item1._key == digit:
                item1._value == None
                self._minus += 1
    
    def __iter__(self):
        for item in self.h0:
            if item._value != None:
                yield (item._key, item._value)
        for item in self.h1:
            if item._value != None:
                yield (item._key, item._value)
                
    def keys(self):
        for item in self.h0:
            yield item._key
        for item in self.h1:
            yield item._key
            
    def values(self):
        for item in self.h0:
            yield item._value
        for item in self.h1:
            yield item._value
    
    def items(self):
        for item in self.h0:
            yield item
        for item in self.h1:
            yield item
    
    def __contains__(self, key):
        for item in self.h0:
            if item._key == key:
                return True
        for item in self.h1:
            if item._key == key:
                return True
        return False
    
    
T=HT()
for i in range(50):
    T[i]=i*i+1
#for i in T.keys():
#    T[i]=T[i]+1
#for i in range(5,400):
#    if i in T:
#        del T[i]
#K=list(T.items())
#K.sort()
for item in iter(T):
    print(item, end = ", ")
print(len(T))
                                                                                                                    
                            
                            
                            
                    
                            
                    
        
                                                                                                            