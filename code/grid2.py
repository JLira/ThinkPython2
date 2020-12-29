def grid(l=4,c=4):
  l1 = '+' + '-' * c + '+' + '-' * c + '+'
  ln = '|' + ' ' * c + '|' + ' ' * c + '|'
  print(l1)
  for i in range(l):
    print(ln)
  print(l1)    
  for i in range(l):
    print(ln)
  print(l1)
