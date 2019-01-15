n,k=map(int,input().split())
for i in range(n,k+1):
   temp=i
   sum1 = 0
  while temp > 0:
    digit =temp % 10
    sum1=sum1+ digit**3
    temp=temp // 10
    if i== sum1:
      print(i)
