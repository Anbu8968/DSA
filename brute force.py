from itertools import combinations_with_replacement as c
coins=list(map(int,input().split()))
su=int(input())
l=[]
m=100000000
for i in range(1,su+1):
    x=c(coins,i)
    for j in x:
        xx=list(j)
        if sum(xx)==su:
            if len(xx)<m:
                m=len(xx)
                l=xx
                
print(l)
            