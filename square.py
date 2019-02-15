x1,y1  = map(int,input().split())
x2,y2  = map(int,input().split())
x3,y3  = map(int,input().split())
x4,y4  = map(int,input().split())
emi=[]
for i in (x1,y1,x2,y2,x3,y3,x4,y4):
  if i not in emi:
    emi.append(i)
if len(emi)==2:
  print("yes")
else:
  print("no")
