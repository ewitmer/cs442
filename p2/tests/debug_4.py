from KB import KB
from parse_logic import parse_logic
from parse_logic import to_cnf
from basic import tt_entails
from resolution import pl_resolution

kb = KB()

kb.addKnowledge(to_cnf(parse_logic('(H==>((G&H)==>A))')))
kb.addKnowledge(to_cnf(parse_logic('(~H==>~((G&H)==>A))')))
#kb.addKnowledge(to_cnf(parse_logic('(A==>X)')))
#kb.addKnowledge(to_cnf(parse_logic('(~A==>~X)')))
a = to_cnf(parse_logic('A'))
print(a)

print(pl_resolution(kb.root,a))