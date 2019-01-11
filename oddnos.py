N,Q=[int(x) for x in input().split()]
li=[]
for i in range(N+!,Q):
  if i % 2 != 0:
    li.append(i)
print(*li)
