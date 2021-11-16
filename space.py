l="i am geetu sharma"
i=0
a=[]
count=0
# g=l.split()
while i<len(l):
    if l[i]==" ":
        r=("space"+str(count))
        # a.append(r)
        count+=1
        a.append(r)
    else:
        a.append(l[i])
    i+=1
print(a)