n=int(input('enter'))
i=1
sum1=0
sum2=0
while i<=n:
	if i%2==0:
		sum1=sum1+(i**2)
		print(sum1)
		i=i+1
	else:
        sum2=sum2+(i**2)
    	print(sum2)
        i=i+1