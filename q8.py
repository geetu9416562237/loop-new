a=[234,34,24,554,45,43,65]
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i+=1
print(max)
j=0
max1=0
while i<len(a):
    if a[j]!=max1:
        if a[j]>max1:
            max1=a[j]
    j+=1
print(max1)