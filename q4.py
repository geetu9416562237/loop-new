list = [6,1,3,5,6,3,1,4,3,2,]
i=0
l=[]
while i<len(list):
    if list[i] not in l:
        l.append(list[i])
    i+=1
j=0
m=1
while j<len(l):
    m*=l[j]
    j+=1
print(m)