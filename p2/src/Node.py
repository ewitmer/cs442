class Node:
  def __init__(self, symbol, connective, children = []):
    """ constructor to initiate the node object """
    
    # symbol, or None if a connective node.
    self.symbol = symbol

    # connective, or None if a symbol node.
    self.connective = connective
    
    # children
    self.children = []
  
  # print function
  def __str__(self, level=0):
    
    if self.symbol == None:
      value = self.connective
    else:
      value = self.symbol

    ret = "\t"*level+repr(value)+"\n"
    
    for child in self.children:
      ret += child.__str__(level+1)
    
    return ret

  def addChild(self, node):
    """ add child to tree """

    self.children.append(node)

  def createChild(self, position = 0):
    """ create new child to add to tree at specific position """

    new = Node(None, None)
    self.children.insert(position, new)

  def isLeaf(self):
    """ check if node is a leaf node """

    return len(self.children) == 0

  def isSymbol(self):
    """ check if node is a symbol """

    return self.symbol != None


  def isConnective(self):
    """ check if node is a connective """

    return self.connective != None
  
  def replace_bicond(self):
    self.connective = '&'
    A = self.children[0]
    B = self.children[1]
    self.children = []
    self.addChild(Node(None, '==>'))
    self.addChild(Node(None, '==>'))
    self.children[0].addChild(A)
    self.children[0].addChild(B)
    self.children[1].addChild(B)
    self.children[1].addChild(A)

  def replace_cond(self):    
    self.connective = '||'
    A = self.children[0]
    B = self.children[1]
    self.children = []
    new_a = Node(None, '~')
    self.addChild(new_a)
    self.addChild(B)
    new_a.addChild(A)

  def demorgan_and(self):
    
    if len(self.children) != 1:
      raise ValueError('demorgan and error')

    hold_children = self.children[0].children
    self.connective = '||'
    self.children = []
    for child in hold_children:
      new = Node(None, '~')
      new.addChild(child)
      self.addChild(new)

  def demorgan_or(self):
    if len(self.children) != 1:
      raise ValueError('demorgan or error')

    hold_children = self.children[0].children
    self.connective = '&'
    self.children = []
    for child in hold_children:
      new = Node(None, '~')
      new.addChild(child)
      self.addChild(new)

  def eliminate_neg(self):
      self.symbol = self.children[0].children[0].symbol
      self.connective = None
      self.children = [] 

  def dist_or(self):

    if len(self.children) != 2:
      raise ValueError("Error: must be in form (A & B) || C")

    if self.children[0].connective == '&':
      A = self.children[0].children
      b = self.children[1]

    else:
      A = self.children[1].children
      b = self.children[0]

    self.children = []

    for child in A:
      new_child = Node(None, "||")
      self.addChild(new_child)
      new_child.addChild(child)
      new_child.addChild(b)
  
    self.connective = '&'


  def flatten_and(self):

    stack = []
    stack.append(self)

    while len(stack) > 0:
      current_node = stack.pop()
      
      if current_node.connective == '&':
        C = current_node.children
        for child in C:
          if child.connective == '&':
            current_node.children.extend(child.children)
            current_node.children.remove(child)

      stack.extend(current_node.children)  
    
  def flatten_or(self):

    stack = []
    stack.append(self)

    while len(stack) > 0:
      current_node = stack.pop()
      
      if current_node.connective == '||':
        C = current_node.children
        for child in C:
          if child.connective == '||':
            current_node.children.extend(child.children)
            current_node.children.remove(child)

      stack.extend(current_node.children) 
 
  def flatten_not(self):

    stack = []
    stack.append(self)

    while len(stack) > 0:
      current_node = stack.pop()
      
      if current_node.connective == '~':
        C = current_node.children
        for child in C:
          if child.connective == '~':
            current_node = current_node.children[0].children[0]

      stack.extend(current_node.children) 

