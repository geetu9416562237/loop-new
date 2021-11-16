number=int(input("enter a value"))
rev=0
while number>0:
    num=number%10
    rev=rev*10+num
    number=number//10
    print("this is reverse number",rev)
