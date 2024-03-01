from KB import KB
from parse_logic import parse_logic
from parse_logic import to_cnf
from basic import tt_entails
from resolution import pl_resolution
import copy
import time

def create_alpha(symbol):
  print('Setting alpha = '+symbol)
  return to_cnf(parse_logic(symbol))


def create_p1():
  # create new knowledge base
  kb = KB()

  # add P ==> Q
  kb.addKnowledge(to_cnf(parse_logic('(P==>Q)')))

  # add P
  kb.addKnowledge(to_cnf(parse_logic('P')))

  return kb.root

def create_p2():
  kb = KB()

  # add ~P11
  kb.addKnowledge(to_cnf(parse_logic('~P11')))

  # add (B11<==>(P12||P21))
  kb.addKnowledge(to_cnf(parse_logic('(B11<=>(P12||P21))')))

  # add (B21<==>(P11||P22||P31))
  kb.addKnowledge(to_cnf(parse_logic('(B21<=>(P11||P22||P31))')))

  # add ~B11
  kb.addKnowledge(to_cnf(parse_logic('~B11')))

  # add ~B21
  kb.addKnowledge(to_cnf(parse_logic('B21')))

  return kb.root

def create_p3():
  # create new knowledge base
  kb = KB()

  # add (MY==>IM)
  kb.addKnowledge(to_cnf(parse_logic('(MY==>IM)')))

  # add (~MY==>(~IM&MA))
  kb.addKnowledge(to_cnf(parse_logic('(~MY==>(~IM&MA))')))

  # add ((IM||MA)==>HO)
  kb.addKnowledge(to_cnf(parse_logic('((IM||MA)==>HO)')))

  # add (HO==>MA)
  kb.addKnowledge(to_cnf(parse_logic('(HO==>MA)')))

  return kb.root

def create_p4():

  kb = KB()

  # A: X is a good door
  kb.addKnowledge(to_cnf(parse_logic('(A==>X)')))
  kb.addKnowledge(to_cnf(parse_logic('(~A==>~X)')))

  # B: At least one door Y or Z is good
  kb.addKnowledge(to_cnf(parse_logic('(B==>(Y||Z))')))
  kb.addKnowledge(to_cnf(parse_logic('(~B==>~(Y||Z))')))

  # C: A and B are both knights
  kb.addKnowledge(to_cnf(parse_logic('(C==>(A&B))')))
  kb.addKnowledge(to_cnf(parse_logic('(~C==>~(A&B))')))


  # D: X and Y are both good doors
  kb.addKnowledge(to_cnf(parse_logic('(D==>(X&Y))')))
  kb.addKnowledge(to_cnf(parse_logic('(~D==>~(X&Y))')))

  # E: X and Z are both good doors
  kb.addKnowledge(to_cnf(parse_logic('(E==>(X&Z))')))
  kb.addKnowledge(to_cnf(parse_logic('(~E==>~(X&Z))')))

  # F: Either D or E is a knight
  kb.addKnowledge(to_cnf(parse_logic('(F==>((D==>~E)||(E==>~D)))')))
  kb.addKnowledge(to_cnf(parse_logic('(~F==>~((D==>~E)||(E==>~D))')))

  # G: If C is a knight, so is F
  kb.addKnowledge(to_cnf(parse_logic('(G==>(C==>F))')))
  kb.addKnowledge(to_cnf(parse_logic('(~G==>~(C==>F))')))

  # H: If G and H are knights, so is A
  kb.addKnowledge(to_cnf(parse_logic('(H==>((G&H)==>A))')))
  kb.addKnowledge(to_cnf(parse_logic('(~H==>~((G&H)==>A))')))

  return kb.root

def create_p5():
  kb = KB()

  # H: If G and H are knights, so is A
  kb.addKnowledge(to_cnf(parse_logic('(H==>((G&H)==>A))')))
  kb.addKnowledge(to_cnf(parse_logic('(~H==>~((G&H)==>A))')))

  return kb.root



############
# PROBLEM 1
############

print(30*'*')
print("MODUS PONENS TEST")
print(30*'*')

# alpha = Q
print('Answer with model checking:')
print(tt_entails(create_p1(),create_alpha('Q')))

print('\nAnswer with resolution solver:')
print(pl_resolution(create_p1(),create_alpha('Q')))

############
# PROBLEM 2
############

print('\n')
print(30*'*')
print("WUMPUS WORLD")
print(30*'*')

# alpha = ~P12
print('Answer with model checking:')
print(tt_entails(create_p2(),create_alpha('~P12')))

print('\nAnswer with resolution solver:')
print(pl_resolution(create_p2(),create_alpha('~P12')))

############
# PROBLEM 3
############

print('\n')
print(30*'*')
print("HORN CLAUSES")
print(30*'*')

# alpha = MY
print('Answer with model checking:')
print(tt_entails(create_p3(),create_alpha('MY')))

print('\nAnswer with resolution solver:')
print(pl_resolution(create_p3(),create_alpha('MY')))

# alpha = ~MY
print('\nAnswer with model checking:')
print(tt_entails(create_p3(),create_alpha('~MY')))

print('\nAnswer with resolution solver:')
print(pl_resolution(create_p3(),create_alpha('~MY')))

# alpha = MA
print('\nAnswer with model checking:')
print(tt_entails(create_p3(),create_alpha('MA')))

print('\nAnswer with resolution solver:')
print(pl_resolution(create_p3(),create_alpha('MA')))

# alpha = HO
print('\nAnswer with model checking:')
print(tt_entails(create_p3(),create_alpha('HO')))

print('\nAnswer with resolution solver:')
print(pl_resolution(create_p3(),create_alpha('HO')))


############
# PROBLEM 4
############

# alpha = X
print('\nAnswer with model checking:')
print(tt_entails(create_p4(),create_alpha('X')))

print('\nAnswer with resolution solver:')
start = time.time()
print(pl_resolution(create_p4(),create_alpha('X')))
end = time.time()
print('Time to run: '+'{:.2f}'.format(end-start))

# alpha = Y
print('\nAnswer with model checking:')
print(tt_entails(create_p4(),create_alpha('Y')))

print('\nAnswer with resolution solver:')
start = time.time()
print(pl_resolution(create_p4(),create_alpha('Y')))
end = time.time()
print('Time to run: '+'{:.2f}'.format(end-start))

# alpha = Z
print('\nAnswer with model checking:')
print(tt_entails(create_p4(),create_alpha('Z')))

print('\nAnswer with resolution solver:')
start = time.time()
print(pl_resolution(create_p4(),create_alpha('Z')))
end = time.time()
print('Time to run: '+'{:.2f}'.format(end-start))

# alpha = ~Y
print('\nAnswer with model checking:')
print(tt_entails(create_p4(),create_alpha('~Y')))

print('\nAnswer with resolution solver:')
start = time.time()
print(pl_resolution(create_p4(),create_alpha('~Y')))
end = time.time()
print('Time to run: '+'{:.2f}'.format(end-start))

# alpha = ~Z
print('\nAnswer with model checking:')
print(tt_entails(create_p4(),create_alpha('~Z')))

print('\nAnswer with resolution solver:')
start = time.time()
print(pl_resolution(create_p4(),create_alpha('~Z')))
end = time.time()
print('Time to run: '+'{:.2f}'.format(end-start))

############
# PROBLEM 5
############

# alpha = X
print('\nAnswer with model checking:')
print(tt_entails(create_p5(),create_alpha('H')))

print('\nAnswer with resolution solver:')
start = time.time()
print(pl_resolution(create_p5(),create_alpha('H')))
end = time.time()
print('Time to run: '+'{:.2f}'.format(end-start))