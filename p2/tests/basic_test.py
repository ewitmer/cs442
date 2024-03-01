from Node import Node
from basic import get_symbols
from basic import pl_true
from basic import tt_check_all
from basic import tt_entails

#build tree
root = Node(None, "==>")
n1 = Node("B12", None)
n2 = Node(None, "||")
n3 = Node("P11", None)
n4 = Node("P22", None)
n5 = Node("P12", None)
root.addChild(n1)
root.addChild(n2)
n2.addChild(n3)
n2.addChild(n4)
n2.addChild(n5)

#test get_symbols
print(get_symbols(root))

model1 = {
  "B12": True,
  "P11": False,
  "P22": False,
  "P12": False
}

model2 = {
  "B12": True,
  "P11": False,
  "P22": True,
  "P12": False
}

model3 = {
  "B12": True,
  "P11": True,
  "P22": True,
  "P12": True
}

model4 = {
  "B12": False,
  "P11": True,
  "P22": True,
  "P12": True  
}

#test pl_true
print(pl_true(root,model1))
print(pl_true(root,model2))
print(pl_true(root,model3))
print(pl_true(root,model4))

#test tt_entails

# Modus Ponens
# P, P==>Q :: Q
KBa = Node(None, "&")
n1a = Node("P", None)
n2a = Node(None, "==>")
n3a = Node("P", None)
n4a = Node("Q", None)
KBa.addChild(n1a)
KBa.addChild(n2a)
n2a.addChild(n3a)
n2a.addChild(n4a)

a = Node("Q", None)

print(tt_entails(KBa,a))

# Wumpus World
KB = Node(None, "&")

# ~P11
n11 = Node(None, "~")
n12 = Node("P11", None)
KB.addChild(n11)
n11.addChild(n12)

# B11 <=> (P12 || P21)
n21 = Node(None, "<=>")
n22 = Node("B11", None)
KB.addChild(n21)
n21.addChild(n22)
n23 = Node(None, "||")
n21.addChild(n23)
n24 = Node("P12", None)
n25 = Node("P21", None)
n23.addChild(n24)
n23.addChild(n25)

# B21 <=> (P11 || P22 || P31)
n31 = Node(None, "<=>")
n32 = Node("B21", None)
KB.addChild(n31)
n31.addChild(n32)
n33 = Node(None, "||")
n31.addChild(n33)
n34 = Node("P11", None)
n35 = Node("P22", None)
n36 = Node("P31", None)
n33.addChild(n34)
n33.addChild(n35)
n33.addChild(n36)

# ~B11
n41 = Node(None, "~")
n42 = Node("B11", None)
KB.addChild(n41)
n41.addChild(n42)

# B21
n51 = Node("B21", None)
KB.addChild(n51)

a = Node("P12", None)
print('wumpus')
print(tt_entails(KB,a))

# Horn Clauses
# MY ==> IM
KB3 = Node(None, "&")

n31 = Node(None, "==>")
n32 = Node("MY", None)
n33 = Node("IM", None)
KB3.addChild(n31)
n31.addChild(n32)
n31.addChild(n33)

# ~MY ==> (~IM & MA)
n34 = Node(None, "==>")
n35 = Node(None, "~")
n36 = Node(None, "&")
n365 = Node(None, "~")
n37 = Node("MY", None)
n38 = Node("IM", None)
n39 = Node("MA", None)
KB3.addChild(n34)
n34.addChild(n35)
n34.addChild(n36)
n35.addChild(n37)
n36.addChild(n365)
n365.addChild(n38)
n36.addChild(n39)

# (IM || MA) ==> HO
n40 = Node(None, "==>")
n41 = Node(None, "||")
n42 = Node("IM", None)
n43 = Node("MA", None)
n44 = Node("HO", None)
KB3.addChild(n40)
n40.addChild(n41)
n40.addChild(n44)
n41.addChild(n42)
n41.addChild(n43)

# HO ==> MA
n45 = Node(None, "==>")
n46 = Node("HO", None)
n47 = Node("MA", None)
KB3.addChild(n45)
n45.addChild(n46)
n45.addChild(n47)


a3 = Node("MY", None)
b3 = Node("MA", None)
c3 = Node("HO", None)

print("it is mythical: "+str(tt_entails(KB3,a3)))
print("it is magical: "+str(tt_entails(KB3,b3)))
print("it is horned: "+str(tt_entails(KB3,c3)))

a3n = Node(None, "~")
a3n.addChild(a3)

b3n = Node(None, "~")
b3n.addChild(b3)

c3n = Node(None, "~")
c3n.addChild(c3)

print("it is NOT mythical: "+str(tt_entails(KB3,a3n)))
print("it is NOT magical: "+str(tt_entails(KB3,b3n)))
print("it is NOT horned: "+str(tt_entails(KB3,c3n)))
