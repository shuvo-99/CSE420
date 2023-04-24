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



def augmentation(re):
  global regex
  if re[-1] != '#':
    regex = regex + '#'
  return regex

def regex_modify(re):
  r = ''
  for i in range(len(re)):
    if i<=len(re)-1:
      if re[i].isalpha() and re[i+1].isalpha():
        r +=  re[i]+'.'
      elif re[i].isalpha() and re[i+1] == '#':
        r +=  re[i]+'.'
      elif re[i] == ')' and (re[i+1] == '*' or re[i+1] == '+'):
        r +=  re[i]
      elif (re[i] == ')' or re[i] == '*' or re[i] == '+'):
        r +=  re[i]+'.'
      else:
        r+=re[i]
  return r

def node_no(symbol):
  quantify_no = 0
  global node
  if augmented_regex[symbol].isalpha() or augmented_regex[symbol] == '#':
    node += 1
    node_dict[node] = augmented_regex[symbol]
  # if symbol is in '*+|.'

def isNullable(symbol):
  
  # if augmented_regex[symbol].isalpha() or augmented_regex[symbol] == '#':
    # nullable = False
    # if nullable not in nullable_dict:
    #   nullable_dict[nullable] = [augmented_regex[symbol]]
    # else:
    #   nullable_dict[nullable].append(augmented_regex[symbol])
  
  if modified_regex[symbol] == 'ε':
    nullable = True
    # nullable_dict[nullable].append(augmented_regex[symbol])\
    if nullable not in nullable_dict:
      nullable_dict[nullable] = ['ε']  
    else:
      nullable_dict[nullable].append('ε')
          

  elif modified_regex[symbol] == '*':
    operators.append('*')
    nullable = True
    if nullable not in nullable_dict:
      nullable_dict[nullable] = ['*']  
    else:
      nullable_dict[nullable].append('*')
  
  # if symbol == '|':
    # c1 = regex.index(symbol)-1
    # c2 = regex.index(symbol)+1
    # # print(c1,c2)
    # # for v in nullable_dict.values():
    # if (regex[c1] in nullable_dict.values()) or (regex[c2] in nullable_dict.values()):
    #   print('yes')
    #   nullable = True
    #   if nullable not in nullable_dict.keys():
    #     nullable_dict[nullable] = ['|']
    #   else:
    #     nullable_dict[nullable].append('|')
  
  elif modified_regex[symbol] == '|':
    operators.append('|')
    c1 = symbol - 1
    c2 = symbol + 1
    for k,v in nullable_dict.items():

      if modified_regex[c1] in v or modified_regex[c2] in v:
        if k ==False:
          nullable = False
          if nullable not in nullable_dict:
            nullable_dict[nullable] = ['|']
            break
          else:
            nullable_dict[nullable].append('|')
            break
        else:
          nullable = True
          if nullable not in nullable_dict:
            nullable_dict[nullable] = ['|']
            break
          else:
            nullable_dict[nullable].append('|')
            break
  
  
  elif modified_regex[symbol] == '.':
    operators.append('.')
    c1 = symbol - 1
    c2 = symbol + 1
    for k,v in nullable_dict.items():
      if modified_regex[c1] in v and modified_regex[c2] in v:
        if k ==False:
          nullable = False
          if nullable not in nullable_dict:
            nullable_dict[nullable] = ['.']
            break
          else:
            nullable_dict[nullable].append('.')
            break
        else:
          nullable = True
          if nullable not in nullable_dict:
            nullable_dict[nullable] = ['.']
            break
          else:
            nullable_dict[nullable].append('.')
            break

def find_firstpos(symbol):
  
  c1 = symbol - 1
  c2 = symbol + 1

  # '*' condition
  if modified_regex[symbol] == '*':
    fp=[]
    if modified_regex[c1].isalpha():
      for k,v in firstpos_dict.items():
        for j in v:  
          if modified_regex[c1] == j:
            for i in k:
              fp.append(i)
            if (tuple(fp) not in firstpos_dict.keys()):
              firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
              break
            else:
              firstpos_dict[tuple(fp)].append(modified_regex[symbol])
              break
    
    elif modified_regex[symbol-3] == '|':
      
      fp=[]
      for k,v in firstpos_dict.items():
        for j in v:  
          
          if '|' == j:
            for i in k:
              fp.append(i)
            
            if (tuple(fp) not in firstpos_dict.keys()):
              firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
              break
            else:
              firstpos_dict[tuple(fp)].append(modified_regex[symbol])
              break

  # '|' condition
  elif modified_regex[symbol] == '|':
    fp=[]
    for k,v in node_dict.items():
      if modified_regex[c1] ==  v:
        fp.append(k)
      if modified_regex[c2] == v:
        fp.append(k)
        break
    if (tuple(fp) not in firstpos_dict.keys()):
      firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
      
    else:
      firstpos_dict[tuple(fp)].append(modified_regex[symbol])

  # '.' condition 
  # elif modified_regex[symbol] == '.':
  #   fp=[]
  #   if ((modified_regex[c1].isalpha()) and (modified_regex[c2].isalpha() or modified_regex[c2] == '#')) :
  #     for k,v in node_dict.items():
  #       if modified_regex[c1] ==  v:
  #         fp.append(k)
  #       if modified_regex[c2] == v:
  #         fp.append(k)
  #         break
  #     if (tuple(fp) not in firstpos_dict.keys()):
  #       firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
        
  #     else:
  #       firstpos_dict[tuple(fp)].append(modified_regex[symbol])
    
  #   else:
  #     for i in operators:
  #       if modified_regex[c1] == i:
  #         for k,v in nullable_dict.items():
  #           if i in v:
  #             if k ==False:
  #               for key,value in firstpos_dict.items():
  #                 for j in value:
  #                   if modified_regex[c1] == j: 
  #                     for z in key:
  #                       fp.append(z)
  #               #   if modified_regex[c2] == value:
  #               #     fp.append(key)
  #               #     break
  #               if (tuple(fp) not in firstpos_dict.keys()):
  #                 firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
                  
  #               else:
  #                 firstpos_dict[tuple(fp)].append(modified_regex[symbol])
  #             else:
  #               for key,value in firstpos_dict.items():
  #                 for j in value:
  #                   if modified_regex[c1] == j: 
  #                     for z in key:
  #                       fp.append(z)
  #                   if modified_regex[c2] == j: 
  #                     for z in key:
  #                       fp.append(z)
  #               if (tuple(fp) not in firstpos_dict.keys()):
  #                 firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
                  
  #               else:
  #                 firstpos_dict[tuple(fp)].append(modified_regex[symbol])
  
  
  # '.' condition 
  elif modified_regex[symbol] == '.':
    fp=[]
    if ((modified_regex[c1].isalpha()) and (modified_regex[c2].isalpha() or modified_regex[c2] == '#')) :
      # for k,v in node_dict.items():
      #   if modified_regex[c1] ==  v:
      #     fp.append(k)
      #   if modified_regex[c2] == v:
      #     fp.append(k)
      #     break
      # if (tuple(fp) not in firstpos_dict.keys()):
      #   firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
        
      # else:
      #   firstpos_dict[tuple(fp)].append(modified_regex[symbol])
      for k,v in nullable_dict.items():
        if modified_regex[c1] in v:
          if k ==False:
            for key,value in firstpos_dict.items():
              for j in value:
                if '.' == j: 
                  for z in key:
                    if z not in fp:
                      fp.append(z)
            #   if modified_regex[c2] == value:
            #     fp.append(key)
            #     break
            if (tuple(fp) not in firstpos_dict.keys()):
              firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
              
            else:
              firstpos_dict[tuple(fp)].append(modified_regex[symbol])
          else:
            for key,value in firstpos_dict.items():
              for j in value:
                if '.' == j: 
                  for z in key:
                    if z not in fp:
                      fp.append(z)
                if modified_regex[c2] == j: 
                  for z in key:
                    if z not in fp:
                      fp.append(z)
            if (tuple(fp) not in firstpos_dict.keys()):
              firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
                  
            else:
              firstpos_dict[tuple(fp)].append(modified_regex[symbol])

    
    else:
      for i in operators:
        if modified_regex[c1] == i:
          for k,v in nullable_dict.items():
            if i in v:
              if k ==False:
                for key,value in firstpos_dict.items():
                  for j in value:
                    if modified_regex[c1] == j: 
                      for z in key:
                        fp.append(z)
                #   if modified_regex[c2] == value:
                #     fp.append(key)
                #     break
                if (tuple(fp) not in firstpos_dict.keys()):
                  firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
                  
                else:
                  firstpos_dict[tuple(fp)].append(modified_regex[symbol])
              else:
                for key,value in firstpos_dict.items():
                  for j in value:
                    if modified_regex[c1] == j: 
                      for z in key:
                        if z not in fp:
                          fp.append(z)
                    if modified_regex[c2] == j: 
                      for z in key:
                        if z not in fp:
                          fp.append(z)
                if (tuple(fp) not in firstpos_dict.keys()):
                  firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
                      
                else:
                  firstpos_dict[tuple(fp)].append(modified_regex[symbol])
        
      
  # else: 
  #   for k,v in firstpos_dict.items():
  #   if modified_regex[c1] == v:
  #     pass


def find_lastpos(symbol):
  
  c1 = symbol - 1
  c2 = symbol + 1
  # if modified_regex[symbol] == '*':
  #   if modified_regex[c1].isalpha():
  #     for k,v in lastpos_dict.items():
  #       for j in v:  
  #         if modified_regex[c1] == j:
  #           for i in k:
  #             lp.append(i)
  #           if (tuple(lp) not in lastpos_dict.keys()):
  #             lastpos_dict[tuple(lp)] = [modified_regex[symbol]]
  #             break
  #           else:
  #             lastpos_dict[tuple(lp)].append(modified_regex[symbol])
  #             break
  
  # '*' condition 
  if modified_regex[symbol] == '*':
    lp=[]
    if modified_regex[c1].isalpha():
      for k,v in lastpos_dict.items():
        for j in v:  
          if modified_regex[c1] == j:
            for i in k:
              lp.append(i)
            if (tuple(lp) not in lastpos_dict.keys()):
              lastpos_dict[tuple(lp)] = [modified_regex[symbol]]
              break
            else:
              lastpos_dict[tuple(lp)].append(modified_regex[symbol])
              break
    
    
    elif modified_regex[symbol-3] == '|':
      
      lp=[]
      for k,v in lastpos_dict.items():
        for j in v:  
          
          if '|' == j:
            for i in k:
              lp.append(i)
            
            if (tuple(lp) not in lastpos_dict.keys()):
              lastpos_dict[tuple(lp)] = [modified_regex[symbol]]
              break
            else:
              lastpos_dict[tuple(lp)].append(modified_regex[symbol])
              break
  
  # '|' condition         
  elif modified_regex[symbol] == '|':
    lp=[]
    for k,v in node_dict.items():
      if modified_regex[c1] ==  v:
        lp.append(k)
        
      if modified_regex[c2] == v:
        lp.append(k)
        break
    if (tuple(lp) not in lastpos_dict.keys()):
      lastpos_dict[tuple(lp)] = [modified_regex[symbol]]
      
    else:
      lastpos_dict[tuple(lp)].append(modified_regex[symbol])


  # '.' condition 
  elif modified_regex[symbol] == '.':
    lp=[]
    if ((modified_regex[c1].isalpha()) and (modified_regex[c2].isalpha() or modified_regex[c2] == '#')) :
      # for k,v in node_dict.items():
      #   if modified_regex[c1] ==  v:
      #     fp.append(k)
      #   if modified_regex[c2] == v:
      #     fp.append(k)
      #     break
      # if (tuple(fp) not in firstpos_dict.keys()):
      #   firstpos_dict[tuple(fp)] = [modified_regex[symbol]]
        
      # else:
      #   firstpos_dict[tuple(fp)].append(modified_regex[symbol])
      for k,v in nullable_dict.items():
        if modified_regex[c2] in v:
          if k ==False:
            for key,value in lastpos_dict.items():
              for j in value:
                if modified_regex[c2] == j: 
                  for z in key:
                    if z not in lp:
                      lp.append(z)
            #   if modified_regex[c2] == value:
            #     fp.append(key)
            #     break
            if (tuple(lp) not in lastpos_dict.keys()):
              lastpos_dict[tuple(lp)] = [modified_regex[symbol]]
              
            else:
              lastpos_dict[tuple(lp)].append(modified_regex[symbol])
            print(lastpos_dict)
          else:
            for key,value in lastpos_dict.items():
              for j in value:
                if modified_regex[c1] == j: 
                  for z in key:
                    if z not in lp:
                      lp.append(z)
                if modified_regex[c2] == j: 
                  for z in key:
                    if z not in lp:
                      lp.append(z)
            if (tuple(lp) not in lastpos_dict.keys()):
              lastpos_dict[tuple(lp)] = [modified_regex[symbol]]
                  
            else:
              lastpos_dict[tuple(lp)].append(modified_regex[symbol])
            print(lastpos_dict)
    
    else:
      # for i in operators:
      #   if modified_regex[c1] == i:
      for k,v in nullable_dict.items():
        if modified_regex[c2] in v:
          if k ==False:
            for key,value in lastpos_dict.items():
              for j in value:
                if modified_regex[c2] == j: 
                  for z in key:
                    lp.append(z)
            #   if modified_regex[c2] == value:
            #     fp.append(key)
            #     break
            if (tuple(lp) not in lastpos_dict.keys()):
              lastpos_dict[tuple(lp)] = [modified_regex[symbol]]
              
            else:
              lastpos_dict[tuple(lp)].append(modified_regex[symbol])
            print(lastpos_dict)
          else:
            for i in operators:
              if modified_regex[c1] == i:
                for key,value in lastpos_dict.items():
                  for j in value:
                    if modified_regex[c1] == j: 
                      for z in key:
                        if z not in lp:
                          lp.append(z)
                    if modified_regex[c2] == j: 
                      for z in key:
                        if z not in lp:
                          lp.append(z)
                if (tuple(lp) not in lastpos_dict.keys()):
                  lastpos_dict[tuple(lp)] = [modified_regex[symbol]]
                      
                else:
                  lastpos_dict[tuple(lp)].append(modified_regex[symbol])
                print(lastpos_dict)
regex = '(a|b)*abb#'
augmented_regex = augmentation(regex)
print('augmented_regex = ',augmented_regex)

modified_regex = regex_modify(augmented_regex)
print('\nmodified_regex = ',modified_regex)

# rex = ''
node = 0
node_dict = {}
quantifier_dict = {}
nullable = False
nullable_dict = {}
firstpos_dict = {}
lastpos_dict = {}
firstpos=[]
lastpos=[]
operators = []

for i in range(len(augmented_regex)):
  node_no(i)
  # isNullable(i)

print('\nnode_dict = ',node_dict)
for k,v in node_dict.items():
  nullable = False
  if nullable not in nullable_dict:
    nullable_dict[nullable] = [v]
  else:
    nullable_dict[nullable].append(v)

  firstpos.append([k])
  firstpos_dict[tuple([k])] = [v]
  lastpos.append([k])
  lastpos_dict[tuple([k])] = [v]

for i in range(len(modified_regex)):
  isNullable(i)
  find_firstpos(i)
  find_lastpos(i)

print('\nnullable_dict = ',nullable_dict)
print('\nfirstpos = ',firstpos)
print('\nfirstpos_dict = ',firstpos_dict)
print('\nlastpos = ',lastpos)
print('\nlastpos_dict = ',lastpos_dict)



# class Node:
#   def __init__(self, value=None, left=None, right=None): 
#     self.value = value
#     self.left = left
#     self.right = right

# def build_syntax_tree(reg_exp):
#   stack = []
#   for char in reg_exp:
#     if char.isalpha():
#       node = Node(char) 
#       stack.append(node)
#     elif char == '.':
#       right_node = stack.pop() 
#       left_node = stack.pop()
#       node = Node('.', left_node, right_node) 
#       stack.append(node)
#     elif char == '|':
#       right_node = stack.pop()
#       left_node = stack.pop()
#       node = Node('|', left_node, right_node) 
#       stack.append(node)
#     elif char == '*':
#       node = Node('*', stack.pop()) 
#       stack.append(node)
#   root = stack.pop()
#   return root

# class SyntaxTree:
#   def __init__(self, reg_exp):
#     self.root = build_syntax_tree(reg_exp) 
#     self.nullable= {}
#     self.firstpos= {}
#     self.lastpos= {}
#     self.followpos = {}
#     self.compute_nullable(self.root)
#     self.compute_firstpos(self.root) 
#     self.compute_lastpos (self.root)
#     self.compute_followpos(self.root)
#   def compute_nullable(self, node): 
#     if node.value.isalpha(): 
#       self.nullable[node ] = False
#     elif node.value=='*':
#       self.nullable[node] = True
#     elif node.value=='|':
#       self.nullable[node] = self.nullable[node.left] or self.nullable[node.right] 
#     elif node.value=='.':
#       self.nullable[node] = self.nullable[node.left] and self.nullable[node.right]
#   def compute_firstpos (self, node):
#     if node.value.isalpha():
#       self.firstpos [node] = set([node])
#     elif node.value=='*':
#       self.firstpos[node] = self.firstpos[node.left]
#     elif node.value=='|':
#       self.firstpos[node] = self.firstpos[node.left].union(self.firstpos[node.right]) 
#     elif node.value=='.':
#       if self.nullable[node.left]:
#         self.firstpos [node] = self.firstpos[node.left].union(self.firstpos[node.right])
#       else:
#         self.firstpos[node] = self.firstpos[node.left]
#   def compute_lastpos (self, node):
#     if node.value.isalpha():
#       self.lastpos [node] = set([node ])
#     elif node.value=='*':
#       self.lastpos [node ] = self.lastpos[node.left]
#     elif node.value=='|':
#       self.lastpos[node] = self.lastpos[node.left].union(self.lastpos[node.right]) 
#     elif node.value=='.':
#       if self.nullable[node.right]:
#         self.lastpos[node] = self.lastpos[node.left].union(self.lastpos[node.right])
#       else:
#         self.lastpos[node] = self.lastpos[node.left]

#   def compute_followpos(self,node):
#     if node.value == '.':
#       for n in self.lastpos[node.left]:
#         self.followpos.setdefault(n,set()).update(self.firstpos[node.right])
#     elif node.value=='*':
#       for n in self.lastpos[node.left]:
#         self.followpos.setdefault(n,set()).update(self.firstpos[node.left])
#     elif node.value=='|':
#       pass

# class DFA:
#   def __init__(self, syntax_tree, alphabet): 
#     self.syntax_tree = syntax_tree 
#     self.alphabet = alphabet
#     self.states = [] 
#     self.transitions = {}
#   def build(self):
#     start_state = self.syntax_tree.firstpos[self.syntax_tree.root] 
#     self.states.append(start_state)
#     stack = [start_state]
#     while stack:
#       state = stack.pop()
#       for char in self.alphabet: 
#         new_state = set()
#         for n in state:
#           if n.value == char:
#             new_state.update(self.syntax_tree.followpos[n])
#           if new_state and new_state not in self.states:
#             self.states.append(new_state) 
#             stack.append(new_state)
#           if state not in self.transitions: 
#             self.transitions[state] = {} 
#           self.transitions[state][char] = new_state
  
#   def recognize(self, input_str):
#     current_state = self.states[0]
#     for char in input_str:
#       curren_state = self.transitions[curren_state][char]
#     return self.syntax_tree.root in current_state

# # if name == 'main': 
# reg_exp1 = 'ab' 

# reg_exp2 = '([a-z]|[A-Z])([a-z]|[A-Z]|[0-9])'
# alphabet = ['a', 'b', 'c', 'd']
# dfa = DFA(SyntaxTree(reg_exp1), alphabet)
# dfa.build()
# print (dfa.recognize ('ab')) # should output True 
# print (dfa.recognize('abc')) # should output False
# dfa = DFA(SyntaxTree (reg_exp2), alphabet) 
# dfa.build()
# print (dfa.recognize('aA1')) # should output True 
# print (dfa.recognize ('1aA')) # should output False