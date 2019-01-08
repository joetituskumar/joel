n=int(input())
if n % 400 == 0:
  print("yes")
elif n % 100==0:
  print("no")
else:
  if n % 4== 0:
    print("yes")
