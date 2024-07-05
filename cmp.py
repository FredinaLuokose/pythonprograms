def istrcmp(x,y):
  x=x.lower()
  y=y.lower()
  if x==y:
    return True
  else:
    return False
print(istrcmp("python","python"))
print(istrcmp("python","java"))