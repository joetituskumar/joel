s=input()
c=0
for i in range(0,len(s)):
  if s[i]==".":
    c=c+1
  if i == len(s)-1:
    c=c+1
print(c)
