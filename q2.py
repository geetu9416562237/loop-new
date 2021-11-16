a= [ ['g', 'f''g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
s=""
while i<len(a):
    j=0
    b=""
    while j<len(a[i]):
        b=a[i][j]
        s=s+b
        j+=1
    i+=1
print(s) 