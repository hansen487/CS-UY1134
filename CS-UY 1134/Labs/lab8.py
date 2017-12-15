class ExpressionTree:
  """An arithmetic expression tree."""

  #-------------------------- nested Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a node."""
    __slots__ = '_element', '_parent', '_left', '_right' # streamline memory usage

    def __init__(self, element, parent=None, left=None, right=None):
      self._element = element
      self._parent = parent
      self._left = left
      self._right = right

  #-------------------------- nested Position class --------------------------
  class Position:
    """An abstraction representing the location of a single element."""

    def __init__(self, container, node):
      """Constructor should not be invoked by user."""
      self._container = container
      self._node = node

    def element(self):
      """Return the element stored at this Position."""
      return self._node._element

    def __eq__(self, other):
      """Return True if other is a Position representing the same location."""
      return type(other) is type(self) and other._node is self._node

    def __ne__(self, other):
      """Return True if other does not represent the same location."""
      return not (self == other)            # opposite of __eq__


 
  def is_root(self, p):
    """Return True if Position p represents the root of the tree."""
    return self.root() == p

  def is_leaf(self, p):
    """Return True if Position p does not have any children."""
    return self.num_children(p) == 0

  def is_empty(self):
    """Return True if the tree is empty."""
    return len(self) == 0


  def preorder_indent(self, p=None, d=0):
    """Print preorder representation of subtree of T rooted at p at depth d."""
    if p==None:
        p=self.root()
    print(d*"   "+ str(p.element())) # use depth for indentation
    for c in self.children(p):
        self.preorder_indent( c, d+1)

  def sibling(self, p):
    """Return a Position representing p's sibling (or None if no sibling)."""
    parent = self.parent(p)
    if parent is None:                    # p must be the root
      return None                         # root has no sibling
    else:
      if p == self.left(parent):
        return self.right(parent)         # possibly None
      else:
        return self.left(parent)          # possibly None

  def children(self, p):
    """Generate an iteration of Positions representing p's children."""
    if self.left(p) is not None:
      yield self.left(p)
    if self.right(p) is not None:
      yield self.right(p)

  def _subtree_inorder(self, p):
    """Generate an inorder iteration of positions in subtree rooted at p."""
    if self.left(p) is not None:          # if left child exists, traverse its subtree
      for other in self._subtree_inorder(self.left(p)):
        yield other
    yield p                               # visit p between its subtrees
    if self.right(p) is not None:         # if right child exists, traverse its subtree
      for other in self._subtree_inorder(self.right(p)):
        yield other

  #------------------------------- utility methods -------------------------------
  def _validate(self, p):
    """Return associated node, if position is valid."""
    if not isinstance(p, self.Position):
      raise TypeError('p must be proper Position type')
    if p._container is not self:
      raise ValueError('p does not belong to this container')
    if p._node._parent is p._node:      # convention for deprecated nodes
      raise ValueError('p is no longer valid')
    return p._node

  def _make_position(self, node):
    """Return Position instance for given node (or None if no node)."""
    return self.Position(self, node) if node is not None else None

  #-------------------------- binary tree constructor --------------------------
#  def __init__(self):
#    """Create an initially empty binary tree."""
#    self._root = None
#    self._size = 0

  #-------------------------- public accessors --------------------------
  def __len__(self):
    """Return the total number of elements in the tree."""
    return self._size
  
  def root(self):
    """Return the root Position of the tree (or None if tree is empty)."""
    return self._make_position(self._root)

  def parent(self, p):
    """Return the Position of p's parent (or None if p is root)."""
    node = self._validate(p)
    return self._make_position(node._parent)

  def left(self, p):
    """Return the Position of p's left child (or None if no left child)."""
    node = self._validate(p)
    return self._make_position(node._left)

  def right(self, p):
    """Return the Position of p's right child (or None if no right child)."""
    node = self._validate(p)
    return self._make_position(node._right)

  def num_children(self, p):
    """Return the number of children of Position p."""
    node = self._validate(p)
    count = 0
    if node._left is not None:     # left child exists
      count += 1
    if node._right is not None:    # right child exists
      count += 1
    return count
    
  def hasx(self, p = None):
    if p == None:
        p = self.root()
    S = []
    for item in self._subtree_inorder(p):
        S.append(item.element())
    if 'x' in S:
        return True
    else:
        return False

  #-------------------------- nonpublic mutators --------------------------
  def _add_root(self, e):
    """Place element e at the root of an empty tree and return new Position.

    Raise ValueError if tree nonempty.
    """
    if self._root is not None:
      raise ValueError('Root exists')
    self._size = 1
    self._root = self._Node(e)
    return self._make_position(self._root)

  def _add_left(self, p, e):
    """Create a new left child for Position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a left child.
    """
    node = self._validate(p)
    if node._left is not None:
      raise ValueError('Left child exists')
    self._size += 1
    node._left = self._Node(e, node)                  # node is its parent
    return self._make_position(node._left)

  def _add_right(self, p, e):
    """Create a new right child for Position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a right child.
    """
    node = self._validate(p)
    if node._right is not None:
      raise ValueError('Right child exists')
    self._size += 1
    node._right = self._Node(e, node)                 # node is its parent
    return self._make_position(node._right)

  def _replace(self, p, e):
    """Replace the element at position p with e, and return old element."""
    node = self._validate(p)
    old = node._element
    node._element = e
    return old

  def _delete(self, p):
    """Delete the node at Position p, and replace it with its child, if any.

    Return the element that had been stored at Position p.
    Raise ValueError if Position p is invalid or p has two children.
    """
    node = self._validate(p)
    if self.num_children(p) == 2:
      raise ValueError('Position has two children')
    child = node._left if node._left else node._right  # might be None
    if child is not None:
      child._parent = node._parent   # child's grandparent becomes parent
    if node is self._root:
      self._root = child             # child becomes root
    else:
      parent = node._parent
      if node is parent._left:
        parent._left = child
      else:
        parent._right = child
    self._size -= 1
    node._parent = node              # convention for deprecated node
    return node._element
  
  def _attach(self, p, t1, t2):
    """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

    As a side effect, set t1 and t2 to empty.
    Raise TypeError if trees t1 and t2 do not match type of this tree.
    Raise ValueError if Position p is invalid or not external.
    """
    node = self._validate(p)
    if not self.is_leaf(p):
      raise ValueError('position must be leaf')
    if not type(self) is type(t1) is type(t2):    # all 3 trees must be same type
      raise TypeError('Tree types must match')
    self._size += len(t1) + len(t2)        # attached t1 as left subtree of node
    t1._root._parent = node
    node._left = t1._root
    t1._root = None             # set t1 instance to empty
    t1._size = 0        # attached t2 as right subtree of node
    t2._root._parent = node
    node._right = t2._root
    t2._root = None             # set t2 instance to empty
    t2._size = 0
      
  def unattach(self, p):
      T1 = ExpressionTree()
      T2 = ExpressionTree()
      left = self.left(p)
      right = self.right(p)
      left._node._parent = None
      right._node._parent = None
      p._node._left = None
      p._node._right = None
      T1._root=left._node
      T2._root=right._node
      return (T1, T2)
    
  def __init__(self, token=None, left=None, right=None):
    """Create an expression tree.

    In a single parameter form, token should be a leaf value (e.g., '42'),
    and the expression tree will have that value at an isolated node.

    In a three-parameter version, token should be an operator,
    and left and right should be existing ExpressionTree instances
    that become the operands for the binary operator.
    """
    self._root=None
    self._size=0
    super().__init__()                        # LinkedBinaryTree initialization
    if token == None:
        self._root = None
        self._size = 0
    else:    
        if not isinstance(token, str):
          raise TypeError('Token must be a string')
        self._add_root(token)                     # use inherited, nonpublic method
        if left is not None:                      # presumably three-parameter form
          if token not in '+-*x/':
            raise ValueError('token must be valid operator')
          self._attach(self.root(), left, right)  # use inherited, nonpublic method

  def __str__(self):
    """Return string representation of the expression."""
    pieces = []                 # sequence of piecewise strings to compose
    self._parenthesize_recur(self.root(), pieces)
    return ''.join(pieces)

  def _parenthesize_recur(self, p, result):
    """Append piecewise representation of p's subtree to resulting list."""
    if self.is_leaf(p):
      result.append(str(p.element()))                    # leaf value as a string
    else:
      result.append('(')                                 # opening parenthesis
      self._parenthesize_recur(self.left(p), result)     # left subtree
      result.append(p.element())                         # operator
      self._parenthesize_recur(self.right(p), result)    # right subtree
      result.append(')')                                 # closing parenthesis

  def evaluate(self):
    """Return the numeric result of the expression."""
    return self._evaluate_recur(self.root())

  def _evaluate_recur(self, p):
    """Return the numeric result of subtree rooted at p."""
    if self.is_leaf(p):
      return float(p.element())      # we assume element is numeric
    else:
      op = p.element()
      left_val = self._evaluate_recur(self.left(p))
      right_val = self._evaluate_recur(self.right(p))
      if op == '+':
        return left_val + right_val
      elif op == '-':
        return left_val - right_val
      elif op == '/':
        return left_val / right_val
      else:                          # treat 'x' or '*' as multiplication
        return left_val * right_val 
        
  def flip_operator(self, p):
      if p.element() == '+':
          self._replace(p, '-')
      elif p.element() == '-':
          self._replace(p, '+')
      elif p.element() == '*':
          self._replace(p, '/')
      elif p.element() == '/':
          self._replace(p, '*')
        


def tokenize(raw):
  """Produces list of tokens indicated by a raw expression string.

  For example the string '(43-(3*10))' results in the list
  ['(', '43', '-', '(', '3', '*', '10', ')', ')']
  """
  SYMBOLS = set('+-*/() ')    # allow for '*' or 'x' for multiplication

  mark = 0
  tokens = []
  n = len(raw)
  for j in range(n):
    if raw[j] in SYMBOLS:
      if mark != j:                 
        tokens.append(raw[mark:j])  # complete preceding token
      if raw[j] != ' ':
        tokens.append(raw[j])       # include this token
      mark = j+1                    # update mark to being at next index
  if mark != n:                 
    tokens.append(raw[mark:n])      # complete preceding token
  return tokens

def build_expression_tree(tokens):
  """Returns an ExpressionTree based upon by a tokenized expression.

  tokens must be an iterable of strings representing a fully parenthesized
  binary expression, such as ['(', '43', '-', '(', '3', '*', '10', ')', ')']
  """
  S = []                                        # we use Python list as stack
  for t in tokens:
    if t in '+-*/':                            # t is an operator symbol
      S.append(t)                               # push the operator symbol
    elif t not in '()':                         # consider t to be a literal
      S.append(ExpressionTree(t))               # push trivial tree storing value
    elif t == ')':       # compose a new tree from three constituent parts
      right = S.pop()                           # right subtree as per LIFO
      op = S.pop()                              # operator symbol
      left = S.pop()                            # left subtree
      S.append(ExpressionTree(op, left, right)) # repush tree
    # we ignore a left parenthesis
  return S.pop()

#if __name__ == '__main__':
#  big = build_expression_tree(tokenize('(100-(10+(3*(12/4))))'))
#  for item in big._subtree_inorder(big.root()):
#      print(item.element(), end = '')
#      
#  #print(big, '=', big.evaluate())
  
def solve(equation_string):
    #print(equation_string)
    equation_list = equation_string.split('=')
    if 'x' in equation_list[1]:
        equation_list[0], equation_list[1] = equation_list[1], equation_list[0]
    #print(equation_list[0]+'='+equation_list[1])
    LT = build_expression_tree(tokenize(equation_list[0]))
    RT = build_expression_tree(tokenize(equation_list[1]))
    count = 0
    while LT.root().element() != 'x':
        subtree = LT.unattach(LT.root())
        T1 = subtree[0]
        T2 = subtree[1]
        LT.flip_operator(LT.root())
        print('T1:', T1)
        print('T2:', T2)
        print('LT:', LT)
        print('RT:', RT)
        if T1.hasx():
            if count == 0:
                NRT = ExpressionTree()
                NRT._root=RT.root()._node
                LT._attach(LT.root(),NRT, T2)
                RT = LT
            else:
                rightsubtrees = RT.unattach(RT.root())
                LT._attach(LT.root(), rightsubtrees[1], T2)
                rightsubtree = LT
                RT._attach(RT.root(), rightsubtrees[0], rightsubtree)
            LT = T1
            count += 1
        elif T2.hasx():
            if count == 0:
                NRT = ExpressionTree()
                NRT._root=RT.root()._node
                LT._attach(LT.root(), T1, NRT)
                RT = LT
            else:
                if LT.root().element() == '*':
                    LT.flip_operator(LT.root())
                #print('RT is', RT)
                leftsubtrees = RT.unattach(RT.root())
                LT._attach(LT.root(), T1, leftsubtrees[1])
                leftsubtree = LT
                RT._attach(RT.root(), leftsubtree, leftsubtrees[0])
            LT = T2
        count += 1
        print('LT is', LT)
    print(RT)
    print(LT,'=',RT.evaluate())
        
    
            
            

#solve('(((10*3)+3)*(9*9))=((100-(10+(3*(12/4))))*(330/(((x/7)*3)-8)))')
solve("(10+x)=52")
solve("(100-x)=58")
#solve("(10*x)=420")
#solve("(126/x)=3")


