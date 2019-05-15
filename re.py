n=input()
li=["a","e","i","o","u","A","E","I","O","U"]
li1=[]
for i in range(0,len(n)):
    if n[i] not in li:
        li1.append(n[i])
print("".join(li1[-1::-1]))
