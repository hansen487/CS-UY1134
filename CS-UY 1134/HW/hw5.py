class LeakyStack:
    def __init__(self, maxsize=0):
        self._capacity = maxsize 
        self._S = []
    
    def push(self, x):
        self._S.append(x)
        if len(self._S) > self._capacity:
            self._S.pop(0)

    def is_empty(self):
        return len(self._S) == 0 
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty!')
        return self._S.pop()
    
    def __len__(self):
        return len(self._S)
    
    def __str__(self):
        return 'The stack is: '+''.join(str(i) for i in self._S)

#stack = LeakyStack(5)
#for i in range(5):
#    stack.push(i)
#print(len(stack))       
#print(str(stack))
#stack.push(6)
#print(str(stack))
#e = LeakyStack()
#print(e.is_empty())
#stack.pop()
#print(stack)
#e.pop()
