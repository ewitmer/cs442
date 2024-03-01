from Node import Node
from parse_logic import parse_logic
from parse_logic import replace_bicond
from parse_logic import replace_cond
from parse_logic import to_cnf
from parse_logic import eliminate_neg


""" 
logic = input("what would you like to tell me: ")
root = parse_logic(logic)
for child in root.children:
  print(child.symbol)
  print(child.connective) """
""" 
parse_logic('((P&Q)==>~(Q&P))')
parse_logic('(P&Q)')
parse_logic('(P||Q||R)')
parse_logic('(P&~(A&B))')
parse_logic('((A||B)&(~A&B))')
parse_logic('~A')
parse_logic('~(A||B)')

parse_logic('((~B11||P12||P21)&((~P12&~P21)||B11))')


root = parse_logic('((~P12&~P21)||B11)')
print(root)
new = to_cnf(root)
print(new)
"""
""" root2 = to_cnf(parse_logic('~P11'))
print(root2)

root = parse_logic('(B11<=>(P12||P21))')
root = to_cnf(root)
print(root) """

root = parse_logic('(MY==>IM)')
#print(to_cnf(root))

root = parse_logic('(~MY==>(~IM&MA))')
#print(to_cnf(root))

from KB import KB
from parse_logic import parse_logic
from parse_logic import to_cnf
from basic import tt_entails
from resolution import pl_resolution
print('start')
root = parse_logic('(H<=>((G&H)==>A))')
a = to_cnf(root)
print('final_')
print(a)
