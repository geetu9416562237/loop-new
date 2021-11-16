row=0
while row<=4:
    col=0
    while col<=3:
        if ((col==0 or col==4) and (row!=0) or (row==1) and (row==1 or row==2)):
            print("*",end=" ")
        else:
            print(end="  ")
        col+=1
    print()
    row+=1