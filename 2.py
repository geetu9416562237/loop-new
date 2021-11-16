row=0
while row<=6:
    col=0
    while col<=4:
        if ((col==0 or col==4 ) and (row!=0)or (row==0  or row==3) and(col>0 and col<4)):
            print("*",end=" ")
        else:
            print(end="  ")
        col+=1
    print()
    row+=1