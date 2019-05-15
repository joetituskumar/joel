n=int(input())
rev=0
las=0
while(n>0):
  las=n%10
  rev=rev*10+las
  n=n//10
print(rev)
