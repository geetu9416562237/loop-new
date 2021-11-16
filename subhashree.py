i=1
while i<=50:
    j=1
    factor=0
    while j<=i:
        if j%i==0:
            factor=factor+1
        j=j+1
    if factor==2:
        print(i)
    i+=1



