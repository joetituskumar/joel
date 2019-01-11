N,K=map(int,input().split())
li=[]
for i in range(N+1,K):
  if i % 2 ==0:
    li.append(i)
print(*li)
    
