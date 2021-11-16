n=int(input("enter a number: "))
sum=0
rev=0
count=0
while n>0:
    Num=n%10
    rev=rev*10+Num
    sum=sum+Num
    n=n//10
    count=count+1
print(sum)
print(rev)
print(count)