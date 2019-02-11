li=[]
n=int(input())
a=1
b=1
c=0
for i in range(0,n):
  a=b
  b=c
  c=a+b
  li.append(c)
print(*li)
