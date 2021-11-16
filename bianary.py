# print("Enter Binary number:")
binary=int(input("enter a value"))
sum= 0
i = 0
while (binary!=0):

        rem = binary % 10
        binary = binary // 10
        sum= sum+ rem*2**i
        i=i+1
print("Decimal number is: ",sum) 
