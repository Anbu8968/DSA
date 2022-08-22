a=int(input())
l=[chr(i+64) for i in range(1,a+1)]
n=int(input())
c=1
i=0
while len(l)!=1:
    # print(l)
    if i==len(l):
        i=0
    if c%n==0 or c%10==n:
        l.remove(l[i])
        i-=1
    c+=1
    i+=1
print(l)
