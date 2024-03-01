from Node import Node

# test instantiation, add child, get node type
test = Node("P", None)
test1 = Node(None, "^")
test.addChild(test1)
print(test.isLeaf() == False)
print(test.isSymbol() == True)
print(test.isConnective() == False)
print(test1.isLeaf() == True)
print(test1.isSymbol() == False)
print(test1.isConnective() == True)
