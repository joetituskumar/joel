full=[int(x) for x in input().split()]
emi=[]
for i in full:
  if i not in emi:
    emi.append(i)
if len(emi)==2:
  print("yes")
