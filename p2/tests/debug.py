from KB import KB
from parse_logic import parse_logic
from parse_logic import to_cnf
from basic import tt_entails
from resolution import pl_resolution

kb2 = KB()

# add ~P11
print('Adding ~P11 knowledge base.\n')
kb2.addKnowledge(to_cnf(parse_logic('~P11')))

# add (B11<==>(P12||P21))
print('Adding (B11<=>(P12||P21)) knowledge base.\n')
kb2.addKnowledge(to_cnf(parse_logic('(B11<=>(P12||P21))')))

# add (B21<==>(P11||P22||P31))
print('Adding (B21<=>(P11||P22||P31)) knowledge base.\n')
kb2.addKnowledge(to_cnf(parse_logic('(B21<=>(P11||P22||P31))')))

# add ~B11
print('Adding ~B11 knowledge base.\n')
kb2.addKnowledge(to_cnf(parse_logic('~B11')))

# add ~B21
print('Adding B21 knowledge base.\n')
kb2.addKnowledge(to_cnf(parse_logic('B21')))

a = parse_logic('P12')
print(kb2.root)
print(pl_resolution(kb2.root, a))