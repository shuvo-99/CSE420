# class Node:
  
#   # nullable = False

#   def __init__(self, symbol):
#     self.regex = symbol
#     self.left = None
#     self.right = None
#     self.nullable = self.isNullable(symbol)
#     print(self.nullable)
#     self.firstpos = set()
#     self.lastpos = set()
#     self.node_No = self.node_no(symbol)
#     print(self.nullable)

#   def isNullable(self,symbol):
#     if symbol.isalpha() or symbol == '#':
#       # self.nullable = False
#       return False
#     else:
#       # self.nullable = True
#       return True
    
      # return .nullable


# for i in regex:
#   obj = Node(i)
#   print(obj.node_No)

# obj = Node(regex)



def augmentation(regex):
  if regex[-1] != '#':
    regex = regex + '#'
  return regex

def node_no(symbol):
  global node
  if symbol.isalpha() or symbol == '#':
    node += 1
    node_dict[node] = symbol

regex = '(a|b)*abb#'
augmented_regex = augmentation(regex)
print(augmented_regex)

node = 0
node_dict = {}
for i in regex:
  node_no(i)
print(node_dict)