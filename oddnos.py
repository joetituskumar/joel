N,Q=map(int,input().split())
li=[]
for i in range(N+1,Q):
  if i % 2 != 0:
    li.append(i)
print(*li)
