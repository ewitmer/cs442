from Node import Node
from KB import KB
from resolution import pl_resolution
from resolution import negate
from resolution import clause_convert
from resolution import resolve_pair
from parse_logic import to_cnf
from parse_logic import parse_logic

# tree in CNF
KB = Node(None, "&")
c1 = Node(None, "||")
c2 = Node(None, "||")
c3 = Node(None, "||")
c4 = Node(None, "~")
a = Node(None, "~")


c12 = Node(None, "~")
c13 = Node("P21", None)
c14 = Node("B11", None)
c1.addChild(c12)
c1.addChild(c14)
c12.addChild(c13)

c22 = Node(None, "~")
c23 = Node("B11", None)
c24 = Node("P12", None)
c25 = Node("P21", None)
c2.addChild(c22)
c2.addChild(c24)
c2.addChild(c25)
c22.addChild(c23)

c32 = Node(None, "~")
c33 = Node("P12", None)
c34 = Node("B11", None)
c3.addChild(c32)
c3.addChild(c34)
c32.addChild(c33)

c4.addChild(Node("B11",None))
a.addChild(Node("P12",None))

KB.addChild(c1)
KB.addChild(c2)
KB.addChild(c3)
KB.addChild(c4)


#pl_resolution(KB,a)
#print(clause_convert(c1))
#print(clause_convert(c2))
#print(clause_convert(c3))
#print(clause_convert(c4))
#print(clause_convert(a))

#print(pl_resolution(KB,a))


""" 
KB2 = Node(None, "&")
c1 = Node("A", None)
c2 = Node("B", None)
c3 = Node("C", None)

a2 = Node("D", None)

#print(pl_resolution(KB2,a2))

#P, P==> Q
KB3 = Node(None, "&")
c1 = Node("P", None)
c2 = Node(None, "||")
c3 = Node(None, "~")
c4 = Node("P", None)
c5 = Node("Q", None)
KB3.addChild(c1)
KB3.addChild(c2)
c2.addChild(c3)
c3.addChild(c4)
c2.addChild(c5)

a3 = Node(None, "~")
a3.addChild(Node("Q", None))
print(pl_resolution(KB3,a3))

c1 = {'MY': False, 'IM': True} 
c2 = {'IM': False, 'MY': True}
print(resolve_pair(c1,c2)) """

kb = KB()

kb.addKnowledge(to_cnf(parse_logic('(H==>((G&H)==>A))')))
kb.addKnowledge(to_cnf(parse_logic('(~H==>~((G&H)==>A))')))
a = to_cnf(parse_logic('H'))
print(a)

print(pl_resolution(kb.root,a))