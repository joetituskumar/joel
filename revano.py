n=int(input())
las=0
rev=0
for i in range(len(str(n))):
    las=n%10
    rev=rev*10+las
    n=n//10
print(rev)
