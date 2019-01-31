def swap(a):
  rev=0
  while(a>0):
    rem=a%10
    rev=rev*10+rem
    a=a//10
  return rev
n,k=map(int,input().split())
c=swap(n)
d=swap(k)
print(c,d)
