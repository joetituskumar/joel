n,a=map(int,input().split())
c,li=0,[]
for i in range(n+1,a):
  c=0
  for j in range(2,i):
    if i%j==0:
      c=c+1
  if c==0:
    li.append(i)

print(*li)

