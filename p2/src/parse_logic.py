from Node import Node
from itertools import combinations 

def parse_logic(logic):
  """ accepts a propositional logic statement written in fully paranthesized form
      with no spaces in between each symbol and connective 
      and returns a tree representation of that sentence """

  # add appropriate spacing
  logic = logic.replace('(', '( ')\
    .replace(')', ' )')\
      .replace('~', ' ~ ')\
        .replace('&', ' & ')\
          .replace('||', ' || ')\
            .replace('<=>', ' <=> ')\
              .replace('==>', ' ==> ')\
                .replace('  ', ' ')
  
  # split the string
  logic = logic.split(' ')
  
  # fixes edge cases with leading negation
  space = ''
  while space in logic: 
    logic.remove(space)    

  # keeps track of parent nodes
  stack = []
  
  # instantiate root of tree, add to stack, set to current node
  root = Node(None, None)
  stack.append(root)
  current_node = root

  for symb in logic:
    
    # start a new 'left node' and attach it to the parent and set to current
    if symb == "(":
      current_node.createChild(0)
      stack.append(current_node)
      current_node = current_node.children[0]

    # negation updates current node, then adds a child to the node and moves to it
    elif symb == '~':
      current_node.connective = symb
      current_node.createChild(0)
      current_node = current_node.children[0]

   # if a connective (x-negation), update current node and add a new child
   # child is effectively a 'right node', but the tree may not be binary
    elif symb in ["&", "||", "==>", "<=>"]:
      current_node.connective = symb
      position = len(current_node.children)
      current_node.createChild(position)
      stack.append(current_node)
      current_node = current_node.children[position]
    
    # move up the tree
    elif symb == ')':
      current_node = stack.pop()

    # indicates it is a leaf node, update and move up the tree
    else:
      current_node.symbol = symb
      current_node = stack.pop()

  return root

def replace_bicond(node):
  node.connective = '&'
  A = node.children[0]
  B = node.children[1]
  node.children[0] = Node(None, '==>')
  node.children[1] = Node(None, '==>')
  node.children[0].addChild(A)
  node.children[0].addChild(B)
  node.children[1].addChild(B)
  node.children[1].addChild(A)

  return node

def replace_cond(node):
  
  node.connective = '||'

  A = node.children[0]
  B = node.children[1]
  node.children = []
  new_a = Node(None, '~')
  node.addChild(new_a)
  node.addChild(B)
  new_a.addChild(A)

  return node

def eliminate_neg(node):
  
  # double-negation elimation
  if node.children[0].connective == '~':
    node = node.children[0].children[0]

  # deMorgan: &
  elif node.children[0].connective == '&':
    A = node.children[0].children[0]
    B = node.children[0].children[1]
    node.connective = '||'
    A_neg = Node(None, '~')
    B_neg = Node(None, '~')
    A_neg.addChild(A)
    B_neg.addChild(B)
    node.children = [A_neg, B_neg]

  # deMorgan: ||
  elif node.children[0].connective == '||':
    A = node.children[0].children[0]
    B = node.children[0].children[1]
    node.connective = '&'
    A_neg = Node(None, '~')
    B_neg = Node(None, '~')
    A_neg.addChild(A)
    B_neg.addChild(B)
    node.children = [A_neg, B_neg]

  return node



def flatten_and(node):
  root = node
  stack = []
  stack.append(root)

  while len(stack) > 0:
    current_node = stack.pop()
    
    if current_node.connective == '&':
      C = current_node.children
      for child in C:
        if child.connective == '&':
          current_node.children.extend(child.children)
          current_node.children.remove(child)

    stack.extend(current_node.children)  
  
  return root
    
def flatten_or(node):

  root = node
  stack = []
  stack.append(root)

  while len(stack) > 0:
    current_node = stack.pop()
      
    if current_node.connective == '||':
      C = current_node.children
      for child in C:
        if child.connective == '||':
          current_node.children.extend(child.children)
          current_node.children.remove(child)

    stack.extend(current_node.children) 
  
  return root
 
def flatten_not(node):

  root = node
  stack = []
  stack.append(root)

  while len(stack) > 0:
    current_node = stack.pop()
    
    if current_node.connective == '~':
      if current_node.children[0].connective == '~':
        current_node = current_node.children[0].children[0]

    stack.extend(current_node.children) 
  
  return root

def flatten(node):



  node = flatten_and(node)
  node = flatten_or(node)
  node = flatten_not(node)

  return node

def update_node(root, old, new):
  
  if root == old:
    return new
  else: 
    if root.children != None:
      for child in root.children:
        update_node(child, old, new)

  return root


def to_cnf(node):
  """ converts a tree representing a sentence in propositional logic
      to a tree in conjunctive normal form """
  
  # Eliminate A <=> B, replace with (A ==> B) & (B ==> A) 
  stack = []
  stack.append(node)

  while len(stack) > 0:
    current_node = stack.pop()
    
    if current_node.connective == '<=>':
      current_node.replace_bicond()
      stack.append(current_node)
    
    stack.extend(current_node.children)

  # Eliminate A ==> B, replace with ~ A || B
  stack = []
  stack.append(node)

  while len(stack) > 0:
    current_node = stack.pop()
    
    if current_node.connective == '==>':
      current_node.replace_cond()
      stack.append(current_node)

    stack.extend(current_node.children)

  node = flatten_or(node)
  node = flatten_and(node)

  # move ~ inward (deMorgan: &)
  stack = []
  stack.append(node)

  while len(stack) > 0:
    current_node = stack.pop()

    if current_node.connective == '~' and current_node.children[0].connective == '&':
      current_node.demorgan_and()
      stack.append(current_node)
    
    stack.extend(current_node.children)

  # move ~ inward (deMorgan: ||)
  stack = []
  stack.append(node)

  while len(stack) > 0:
    current_node = stack.pop()

    if current_node.connective == '~' and current_node.children[0].connective == '||':
      current_node.demorgan_or()
      stack.append(current_node)
    
    stack.extend(current_node.children)

  # eliminate double negatives
  stack = []
  stack.append(node)

  while len(stack) > 0:
    current_node = stack.pop()

    if current_node.connective == '~' and current_node.children[0].connective == '~':
      current_node.symbol = current_node.children[0].children[0].symbol
      current_node.connective = None
      current_node.children = [] 
  
    stack.extend(current_node.children)

  # distribute || over & NOTE: this only works in the form (A & B & C...) || D
  stack = []
  stack.append(node)

  while len(stack) > 0:
    current_node = stack.pop()

    if current_node.connective == '||':
      for child in current_node.children:
        if child.connective == '&':
          current_node.dist_or()
          stack.append(current_node)
    
    stack.extend(current_node.children)   

  node = flatten(node)
  node = flatten_or(node)

  return node



