n=5
ch=65
x=1
while x<=n:
    y=1
    while y<=x:
        print(chr(ch)+"",end="")
        if ch<80:
            ch+=1
        else:
            ch=0
        y+=1
    x+=1
    print()