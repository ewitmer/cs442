from Node import Node

class KB:
  def __init__(self):
    """ constructor to initiate the KB object """

    self.root = Node(None, "&")


  def addKnowledge(self, node):

    self.root.children.append(node)
    self.root.flatten_and()
    self.root.flatten_or()


  

