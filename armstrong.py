n=int(input())
sum1 = 0
temp=n
while temp > 0:
  digit =temp % 10
  sum1=sum1+ digit**3
  temp=temp // 10
if n == sum1:
  print("yes")
else:
  print("no")
  
