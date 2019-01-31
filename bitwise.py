a,b=map(int,input().split())
c=a|b
b,a=a&c,b&c
print(a,b)
