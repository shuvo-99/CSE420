def augmentation(regex):
  if regex[-1] != '#':
    regex = regex + '#'
  return regex

regex = '(a|b)*abb#'
augmented_regex = augmentation(regex)
print(augmented_regex)