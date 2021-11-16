a=[2,4,5,3,7,35,334]
i=0
b=[]
while i<len(a):
    j=0
    sum=""
    y=str(a[i])
    while j<len(y):
        if a[j]=="0":
            sum=sum+"zero"
        elif a[j]=="1":
            sum=sum+"one"
        elif a[j]=="2":
            sum=sum+"two"
        elif a[j]=="3":
            sum=sum+"three"
        elif a[j]=="4":
            sum=sum+"four"
        elif a[j]=="5":
            sum=sum+"five"
        elif a[j]=="6":
            sum=sum+"six"
        elif a[j]=="7":
            sum=sum+"seven"
        elif a[j]=="8":
            sum=sum+"eight"
        elif a[j]=="9":
            sum=sum+"nine"
        j+=1
    b.append(sum)

    i+=1
print(b)
