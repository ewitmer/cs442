import copy
from Node import Node

def negate(a):
    """ returns negation of alpha for resolution by contradiction """
    # adds negation
    if a.connective == None:
      alpha = Node(None, "~")
      alpha.addChild(a)
    # removes negation
    else: 
      alpha = a.children[0]
    return alpha

def clause_convert(clause_node):
    """ inputs a clauses in node data structure and 
        returns the clauses in dict data structure for resolution """
    
    clause_dict = {}
    
    # if the connective is 'or'
    if clause_node.connective == "||":
      for child in clause_node.children:
        if child.symbol != None:
          if child.symbol in clause_dict.keys():
            if clause_dict[child.symbol] == False:
              return None
          else:
            clause_dict[child.symbol] = True
        else:
          value = child.children[0].symbol
          if value in clause_dict.keys():
            if clause_dict[value] == True:
              return None
          clause_dict[value] = False
    
    # if the connective is 'not'
    elif clause_node.connective == "~":
      value = clause_node.children[0].symbol
      if value in clause_dict.keys():
        if clause_dict[value] == True:
          return None
      clause_dict[value] = False

    # if there is no connective
    elif clause_node.symbol != None:
      if clause_node.symbol in clause_dict.keys():
        if clause_dict[clause_node.symbol] == False:
          return None
      clause_dict[clause_node.symbol] = True

    # if there is another connective, raise error: node not in CNF
    else:
      raise ValueError("Node is not in conjunctive normal form")

    return clause_dict


def resolve_pair(c1, c2):
  # get list of overlapping symbols in two conjunctions
  overlap = [key for key in c1 if key in c2]

  # get list of resolvable symbols
  overlap = list(filter(lambda key: c1[key] != c2[key], overlap))
  
  # if there are no ways to resolve these two clauses
  if len(overlap) == 0:
    return [c1, c2]

  # if they will always resolve to tautology
  if len(overlap) > 1:
    return None
  
  remove = overlap[0]

  c1_copy = copy.copy(c1)
  c2_copy = copy.copy(c2)
  del c1_copy[remove]
  del c2_copy[remove]

  c1_copy.update(c2_copy)

  if len(c1_copy) > len(c1):
    return [c1,c2]

  return [c1_copy]


def check_subset(new, clauses):
    """ returns true or false 
        checks if new is a subset of clauses """  
    if(all(x in clauses for x in new)): 
      return True
    else:
      return False

def pl_resolution(KB,a):
    """ returns true or false 
        inputs: KB, the knowledge base, a sentence in propositional logic α, 
        the query, a sentence in propositional logic """

    clauses_n = KB.children
    clauses_n.append(negate(a))

    # convert node structure to dict structure for resolution
    clauses = list(map(lambda x: clause_convert(x), clauses_n))

    cont_loop = True
    
    while cont_loop:
      new = []
      # loop through all clauses in CNF
      print('clauses to check: '+str(len(clauses)))
      for i in range(len(clauses)):
        for j in range(i+1,len(clauses)):
          resolvents = resolve_pair(clauses[i], clauses[j])
          
          # if it results in the empty clause, return True
          if resolvents != None:
            if {} in resolvents:
              return True

            # if the resulting clause is not in the list, add it
            else:
              new = new + list(filter(lambda x: x not in new, resolvents))

      # loop breaks if no progress is made   
      if check_subset(new, clauses):
        cont_loop = False

      # update clauses with new list
      clauses = new
    return False
    

    

    

