n=int(input("enter a num: "))
i=1
factor=0
Pos=0
while i<=n:
    if n%i==0:
        factor=factor+1
    i+=1
if factor==2:
    Pos=Pos+1
    print(Pos,"prime")




