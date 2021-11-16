a=["a","d","a","s","d","a","d","s","w","s","v","a ","b","a","a","e"]
b=[]
i=0
while i<len(a):
    count=0
    j=0
    while j<len(a):
        if a[i]==a[j]:
            count+=1
        j+=1
    if[count,a[i]] not in b:
        b.append([count,a[i]])
    i+=1
print(b)

