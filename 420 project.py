class Node:
  node = 0
  def __init__(self, symbol):
    self.symbol = symbol
    self.left = None
    self.right = None
    self.nullable = False
    self.firstpos = set()
    self.lastpos = set()
    self.node_No = self.node_no(symbol)
  
  def node_no(self,symbol):
    if symbol.isalpha() or symbol == '#':
      Node.node += 1
      return Node.node
    
    # print(node_no)

def augmentation(regex):
  if regex[-1] != '#':
    regex = regex + '#'
  return regex

regex = '(a|b)*abb#'
augmented_regex = augmentation(regex)
print(augmented_regex)

for i in regex:
  obj = Node(i)
  print(obj.node_No)

