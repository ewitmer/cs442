from Node import Node
from KB import KB
from basic import tt_entails
from parse_logic import parse_logic
from parse_logic import to_cnf

kb = KB()

p1 = to_cnf(parse_logic('(P==>Q)'))
p2 = to_cnf(parse_logic('P'))
kb.addKnowledge(p1)
kb.addKnowledge(p2)

a = to_cnf(parse_logic('Q'))
print(kb.root)
print(a)
print(tt_entails(kb.root,a))

r = to_cnf(parse_logic('(B11<=>(P12||P21))'))
kb2 = KB()
kb2.addKnowledge(r)
print(kb2.root)
  