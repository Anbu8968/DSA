c=list(map(int,input().split()))
s=int(input())
c=sorted(c)[::-1]
i=0
l=[]
def coins(i,s):
    if i==len(c):
        return 0
    if s>=c[i]:
        s-=c[i]
        l.append(c[i])
        coins(i,s)
    else:
        i+=1
        coins(i,s)
coins(i,s)
print(l)