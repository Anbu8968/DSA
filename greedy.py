co=list(map(int,input().split()))
co=sorted(co)[::-1]
s=int(input())
i=0
c=0
l=[]
while s!=0:
    if co[i]<=s:
        s-=co[i]
        l.append(co[i])
        c+=1
    else:
        i+=1
print(c)
print(l)