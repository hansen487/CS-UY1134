class PList:
    class _Node:
        __slots__='_data','_prev','_next'
        def __init__(self,data,prev,next):
            self._data=data
            self._prev=prev
            self._next=next
    class Position:
        def __init__(self,plist,node):
            self._plist=plist
            self._node=node
        def data(self):
            return self._node._data
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        def __ne__(self,other):
            return not (self == other)
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._plist is not self:
            raise ValueError('p does not belong to this PList')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    def _make_position(self,node):
        if node is self._head or node is self._tail:
            return None
        else:
            return self.Position(self,node)
    def __init__(self):
        self._head=self._Node(None,None,None)
        self._head._next=self._tail=self._Node(None,self._head,None)
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        return self._make_position(self._head._next)
    def last(self):
        return self._make_position(self._tail._prev)
    def before(self,p):
        node=self._validate(p)
        return self._make_position(node._prev)
    def after(self,p):
        node=self._validate(p)
        return self._make_position(node._next)
    def __iter__(self):
        pos = self.first()
        while pos:
            yield pos.data()
            pos=self.after(pos)
    def _insert_after(self,data,node):
        newNode=self._Node(data,node,node._next)
        node._next._prev=newNode
        node._next=newNode
        self._size+=1
        return self._make_position(newNode)
    def add_first(self,data):
        return self._insert_after(data,self._head)
    def add_last(self,data):
        return self._insert_after(data,self._tail._prev)
    def add_before(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node._prev)
    def add_after(self,p,data):
        node=self._validate(p)
        return self._insert_after(data,node)
    def delete(self,p):
        node=self._validate(p)
        data=node._data
        node._prev._next=node._next
        node._next._prev=node._prev
        node._prev=node._next=node._data=None
        self._size-=1
        return data
    def replace(self,p,data):
        node=self._valdiate(p)
        olddata=node._data
        node._data=data
        return olddata
    def rev_itr(self):
        pos = self.last()
        while pos:
            yield pos.data()
            pos=self.before(pos)

class Counters:
    class _Item:
        def __init__(self,name):
            self._name=name
            self._count=0
    class Counter:
        def __init__(self,Plistposition, counterposition):
            self._Plistposition = Plistposition
            self._counterposition = counterposition
        def name(self):
            return self._counterposition.data()._name
        def count(self):
            return self._Plistposition.data().count
    class InnerLList:
        def __init__(self, count):
            self._L = PList()
            self.count = count
        def getcount(self):
            return self.count
    def __init__(self):
        self._L=PList()
    def new_counter(self,name):
        if self._L.last() == None or self._L.last().data().getcount() != 0:
            self._L.add_last(Counters.InnerLList(0))
        self._L.last().data()._L.add_last(Counters._Item(name))
        return Counters.Counter(self._L.last(), self._L.last().data()._L.last())   #might need to change later
    def delete_counter(self,counter):
        counter._Plistposition.data()._L.delete(counter._counterposition)
        if counter._Plistposition.data()._L.is_empty():
            self._L.delete(counter._Plistposition)
        counter._counterposition=None
    def increment_counter(self,counter):
        counter._counterposition.data()._count += 1
        countercount = counter._counterposition.data()._count
        try:
            before_position=self._L.before(counter._Plistposition)
            if before_position == None or countercount != before_position.data().count:
                self._L.add_before(counter._Plistposition, Counters.InnerLList(countercount))
                before_position = self._L.before(counter._Plistposition)
            before_position.data()._L.add_last(counter._counterposition.data())
            counter._Plistposition.data()._L.delete(counter._counterposition)
            if counter._Plistposition.data()._L.is_empty():
                self._L.delete(counter._Plistposition)
            counter._Plistposition = before_position
            counter._counterposition = before_position.data()._L.last()
        except ValueError:
            raise ValueError('counter does not belong to this Counter')
    def __iter__(self):
        cposition=self._L.first()
        pposition=cposition.data()._L.first()
        while cposition:
            yield Counters.Counter(cposition, pposition)
            pposition=cposition.data()._L.after(pposition)
            if pposition == None:
                cposition=self._L.after(cposition)
                if cposition != None:
                    pposition=cposition.data()._L.first()
                else:
                    cposition == False
                    
class Counters_SLOW:
    class _Item:
        def __init__(self,name):
            self._name=name
            self._count=0
    class Counter:
        def __init__(self,position):
            self._position=position
        def name(self):
            return self._position.data()._name
        def count(self):
            return self._position.data()._count            
    def __init__(self):
        self._L=PList()
    def new_counter(self,name):
        self._L.add_last(Counters._Item(name))
        return Counters_SLOW.Counter(self._L.last())
    def delete_counter(self,counter):
        self._L.delete(counter._position)
        counter._position=None
    def increment_counter(self,counter):
        counter._position.data()._count+=1
        before_position=self._L.before(counter._position)
        while (before_position and 
              before_position.data()._count
              < counter.count()):
            new_position=self._L.add_before(before_position,counter._position.data())
            self._L.delete(counter._position)
            counter._position=new_position
            before_position=self._L.before(counter._position)
    def __iter__(self):
        position=self._L.first()
        while position:
            yield Counters_SLOW.Counter(position)
            position=self._L.after(position)



#below is what you can use to test the code            
from time import time
start_time1 = time()
C=Counters()           
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
counters=[C.new_counter(name) for name in names]
C.increment_counter(counters[3])
C.increment_counter(counters[4])
C.increment_counter(counters[5])
for i in range(4):
    C.increment_counter(counters[9])
for i in range(5):
    C.increment_counter(counters[6])
    C.increment_counter(counters[7])
    C.increment_counter(counters[8])
#for c in C:
#    print(c.name(), c.count())

#names=("John","Guruprasad","Jason","Duc","Eric","Xinran","Kent","Leon","Ian")
#counters=[C.new_counter(name) for name in names]
#
#for i in range(100):
#    for cp in counters:
#        C.increment_counter(cp) 
#for i in range(len(counters)):
#    for j in range(i):
#        C.increment_counter(counters[i])
#C.delete_counter(counters[3])
#for c in C:
#    print(c.name(),c.count())
end_time1 = time()
elapsed1 = end_time1 - start_time1

start_time2 = time()
D=Counters_SLOW()           
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
counters=[D.new_counter(name) for name in names]
D.increment_counter(counters[3])
D.increment_counter(counters[4])
D.increment_counter(counters[5])
for i in range(4):
    D.increment_counter(counters[9])
for i in range(5):
    D.increment_counter(counters[6])
    D.increment_counter(counters[7])
    D.increment_counter(counters[8])
#for c in C:
#    print(c.name(), c.count())
#names=("John","Guruprasad","Jason","Duc","Eric","Xinran","Kent","Leon","Ian")
#counters=[D.new_counter(name) for name in names]
#
#for i in range(100):
#    for cp in counters:
#        D.increment_counter(cp) 
#for i in range(len(counters)):
#    for j in range(i):
#        D.increment_counter(counters[i])
#D.delete_counter(counters[3])
#for d in D:
#    print(d.name(),d.count())
end_time2 = time()
elapsed2 = end_time2 - start_time2
print(elapsed1, elapsed2)

