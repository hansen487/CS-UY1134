import random


class BST:
    class _Node:
        def __init__(self,parent,left,right,data):
            self._left=left
            self._right=right
            self._parent=parent
            self._data=data
            self._depth = 0
            
    class Position:
#        def __ne__(self, other):
#            return not (self == other)           

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            if self._node._data == None:
                return None
            else:
                return self._node._data

#        def __eq__(self, other):
#            return type(other) is type(self) and other._node is self._node    
        
    def __init__(self):
        self._root=None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def is_root(self, n):
        return self._root == n

    def is_leaf(self, n):
        if n._left == None and n._right == None:
            return True
        else:
            return False
        
    def parent(self, p):
        return self._make_position(p._node._parent)
    
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None
    
    def insert(self,x):
        if self._root == None:
            self._root=BST._Node(None,None,None,x)
            self.size += 1
            return self._make_position(self._root)
        else:
            self._rec_insert(self._root,x)        
    
    def depth(self, n):
        if self.is_root(n):
            return 0
        else:
            return 1 + self.depth(n._parent)
    
    def assign_depth(self):
        for n in self.inorder():
            n._depth = self.depth(n)
    
    def height(self):
        return max(self.depth(n) for n in self.inorder() if self.is_leaf(n))
    
    def add_left(self, p, e):
        p._node._left = self._Node(p._node, None, None, e)                  
        return self._make_position(p._node._left)
        
    def add_right(self, p, e):
        p._node._right = self._Node(p._node, None, None, e)                 
        return self._make_position(p._node._right)
        
    def _rec_insert(self,n,x):
        if x<n._data:
            if n._left == None:
                n._left=BST._Node(n,None,None,x)
                self.size += 1
                return self._make_position(n._left)
            else:
                self._rec_insert(n._left,x)
        else:
            if n._right == None:
                n._right=BST._Node(n,None,None,x)
                self.size += 1
                return self._make_position(n._right)
            else:
                self._rec_insert(n._right,x)
                
    def search_le(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_search_le(self._root,x)
        
    def _rec_search_le(self,n,x):
        if x<n._data:
            if n._left:
                return self._rec_search_le(n._left,x)
            else:
                return None
        else:
            if n._right:
                rv=self._rec_search_le(n._right,x)
                if rv:
                    return rv
                else:
                    return n._data
            else:
                return n._data
            
    def search_le_node(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_search_le_node(self._root,x)
        
    def _rec_search_le_node(self,n,x):
        if x<n._data:
            if n._left:
                return self._rec_search_le_node(n._left,x)
            else:
                return None
        else:
            if n._right:
                rv=self._rec_search_le_node(n._right,x)
                if rv:
                    return rv
                else:
                    return n
            else:
                return n
           
    def _subtree_first_position(self, p):
        walk = p
        while self.left(walk) is not None: 
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        walk = p
        while self.right(walk) is not None: 
            walk = self.right(walk)
        return walk
    
    def inorder(self):
        n = self.first_node()
        while n is not self.last_node():
            yield n
            n = self.after_node(n)
        yield self.last_node()
        
    def first_node(self):
        node = self._root
        while node._left != None:
            node = node._left
        return node
    def left(self, p):
        return self._make_position(p._node._left)
    
    def right(self, p):
        return self._make_position(p._node._right)
    
    def root(self):
        return self._make_position(self._root)
    
    def first(self):
        p = self.root()
        while self.left(p) != None:
            p = self.left(p)
        return p
    
    def last_node(self):
        node = self._root
        while node._right != None:
            node = node._right
        return node
    
    def last(self):
        p = self.root()
        while self.right(p) != None:
            p = self.right(p)
        return p
    
    def before(self, p):
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            while above.element() > p.element():
                above = self.parent(above)
            return above
    
    def after(self, p):                            
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            while above.element() < p.element():
                above = self.parent(above)
            return above
            
    def after_node(self, n):
        if n._left == None and n._right == None:
            if n._parent._left == n:
                return n._parent
            elif n._parent._right == n:
                if n == self.last_node():
                    return None
                else:
                    while n._parent._data<n._data:
                        n = n._parent
                    return n._parent
        elif n._right != None:
            if n._right._left != None:
                n = n._right._left
                while n._left != None:
                    n = n._left
                if n._right == None or n._right._data > n._data:
                    return n
                else:
                    n = n._right
                    while n._left != None:
                        n = n._left
                    return n
            else:
                return n._right
        else:
            while n._parent._data<n._data:
                n = n._parent
            return n._parent

    def __iter__(self):
        n = self.first_node()
        while n._data is not self.last_node()._data:
            yield n._data
            n = self.after_node(n)
        yield self.last_node()._data
            
    def search_ge(self, x):
            node = self.search_le_node(x)
            if self.last_node() == node:
                return self.last_node()._data
            else:
                node = self.after_node(node)
                return node._data
                   
    def pos_le(self,x):
        if self._root==None:
            return None
        else:
            return self._rec_get_le(self.root(),x)
        
    def _rec_get_le(self,p,x):
        if x < p.element():
            if self.left(p):
                return self._rec_get_le(self.left(p),x)
            else:
                return None
        else:
            if self.right(p):
                rv=self._rec_get_le(self.right(p),x)
                if rv:
                    return rv
                else:
                    return p
            else:
                return p
            
    def pos_ge(self, x):
        if x > self.last().element():
            return None
        p = self.pos_le(x)
        if self.last() == p:
            return self.last()
        else:
            p = self.after(p)
            return p
         
    def print(self):
        self.assign_depth()
        height = self.height()
        lst = []
        for i in range(height+1):
            lst.append([])
        for node in self.inorder():
            x = node._depth
            lst[x].append(node._data)
            for i in lst:
                if i != lst[x]:
                    i.append(len(str(node._data))*' ')
        for i in lst:
            for j in i:
                print(j, end = '')
            print()
    
    def range(self, x, y):
        p = self.pos_ge(x)
        while p.element() <= y:
            yield p.element()
            p = self.after(p)
        
    def pos_range(self, x, y):
        p = self.pos_ge(x)
        while p.element() <= y:
            yield p
            p = self.after(p)
            
            
T=BST()
L=list(range(10,100,10))
random.shuffle(L)
for i in L:
    T.insert(i)
    #print(i, end = ' ')
#iterates the elements in the BST
#for i in iter(T):
#    print(i, end=' ')

#tests for search_ge(x)
#print(T.search_ge(23))
#print(T.search_ge(38))
#print(T.search_ge(90))

#test for len(T)
#print(len(T))

#tests print
#T.print()

#tests T.first()
#print(T.first())
#print(T.first().element())

#tests T.last()
#print(T.last())
#print(T.last().element())

##tests T.before()
#print(T.root())
#print(T.root().element())
#print(T.before(T.root()))
#print(T.before(T.root()).element())

#tests T.after()
#print(T.root())
#print(T.root().element())
#print(T.after(T.root()))
#print(T.after(T.root()).element())
#print(T.after(T.after(T.root())).element())
#print(T.after(T.after(T.after(T.root()))).element())
#tests T.pos_le()
#print(T.pos_le(33).element())
#print(T.pos_le(9))

#test T.pos_ge()
#print(T.pos_ge(46).element())
#print(T.pos_ge(99))
#for i in range(5,105,5):
    #print(T.search_le(i))
    
#tests T.range()
#for i in T.range(12, 66):
#    print(i, end = ' ')
#
##tests T.pos_range()
#for i in T.pos_range(12, 66):
#    print(i, end = ' ')

#PROBLEM 8
def create_balanced_tree(x, p = None, T = None):
    if T == None:
        T = BST()
        x /= 2
        p = T.insert(x)
    if x != 1:
        x  /= 2
        left = T.add_left(p, p.element() - x)
        right = T.add_right(p, p.element() + x)
        create_balanced_tree(x, left, T)
        create_balanced_tree(x, right, T)
    return T
        
#create_balanced_tree(16).print()
#create_balanced_tree(64).print()

#PROBLEM 9
def problem9(x):
    mid = x//2
    T1 = BST()
    for i in range(mid):
        T1.insert(i)
        T1.insert(x-i)
    T1.print()
    
problem9(20)