def get_symbols(node):
  """ gets all symbols from a logical proposition represented as a tree """
  symbols = set()
  
  # base case: node is a symbol
  if node.isSymbol():
    symbols.add(node.symbol)
  
  # recursive case: node is not a symbol
  else:
    for child in node.children:
      symbols = symbols.union(get_symbols(child))
  
  return symbols

def pl_true(node, model):
  """ returns True or False
      inputs a node (kb or a) and a model (dict)
      determines if the sentence is T or F in the model """    
  
  # if node is symbol, look it up in the model
  if node.isSymbol():
    return model[node.symbol]
  
  # if the connective is NOT, return the negative of the first child (operator precedence)
  elif node.connective == "~":
    if node.children == None:
      return None
    else:
      return not pl_true(node.children[0], model)
  
  # if the connective is AND, check all children, if any are false, return false
  elif node.connective == "&":
    for child in node.children: 
      if (pl_true(child, model) == False):
        return False
    return True

  # if the connective is OR, check all children, if any are true, return true
  elif node.connective == "||":
    for child in node.children:
      if (pl_true(child, model) == True):
        return True
    return False

  # if the connective is IMPLIES, if the left node is true and right is false, return false
  elif node.connective == "==>":
    if pl_true(node.children[0], model) == True and pl_true(node.children[1], model) == False:
      return False
    else: 
      return True

  # if the connective is BICONDITIONAL, if the left node is equal to the right node return true
  elif node.connective == "<=>":
    if pl_true(node.children[0], model) == pl_true(node.children[1], model):
      return True
    else:
      return False

def update_model(model, P, b):
  """ Updates model for truth table """

  model_u = model.copy()
  model_u[P] = b
  return model_u

def tt_entails(KB, a):
  """ returns True or False
      inputs kb, the knowledge base, a sentence in propositional logic 
      a, the query, a sentence in propositional logic.
      propositional logic statements are represented by a tree structure """

  # get set of symbols from KB and alpha then combine
  kb_symbols = get_symbols(KB)
  a_symbols = get_symbols(a)
  symbols = kb_symbols.union(a_symbols)

  return tt_check_all(KB, a, symbols, {})
    
    
def tt_check_all(KB, a, symbols, model):    
  """ returns True or False """
  if len(symbols) == 0:
    if pl_true(KB, model):
      return pl_true(a, model)
    else:
      return True  # when KB is false, always return true
  else:
    P = list(symbols)[0]
    rest = set(list(symbols)[1:])
    return (tt_check_all(KB, a, rest, update_model(model,P,True)) and tt_check_all(KB, a, rest, update_model(model,P,False)))
