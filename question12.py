product =int(input("enter a value"))
num=len(str(product))
i=1
num1=1
while i<=product:
    num2=product%10
    num=num+num2
    num=num//10
    if i==product:
        print(product)
    else:
        print("nhi h ")
    i=i+1