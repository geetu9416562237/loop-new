# def prime():
    
n=int(input("enter a value"))
i=1
factor=0
while i>=n:
    if n%i==0:
        factor=factor+1
    i+=1
if factor==2:
    print("prime") 
else:
    print("not prime")
# prime()

 user=int(input("enter:"))
# i=1
# t=0
# while i<=user:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2: 
#         t+=1
#     else:
#         t+=1
#     i+=1

