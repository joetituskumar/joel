n=int(input())
sod=0
while(n>0):
    las=n%10
    sod=sod+(las*las)
    n=n//10
print(sod)
