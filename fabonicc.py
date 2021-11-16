user=int(input("enter a value "))
a=0
b=1
count=0
if user<=0:
    print("enter the positive num")
elif user==1:
    print("enter a upto num")
    print(a)
else:
    print("this is ryt num")

    while count<user:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
