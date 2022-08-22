# # # a=int(input())
# # # l=[i for i in range(1,a+1)]
# # # n=int(input())
# # # ll=a
# # # while len(l)!=1:
# # #     for i in l:
# # #         if i%n==0:
# # #             l.remove(i)
# # #         if i%10==n:
# # #             l.remove(i)
# # #             #print(l)
# # #     print(l)
# # #     break
# # #     # if len(l)>1:
# # #     #     ll=[j for j in range(ll+1,1+len(l)+l[-1])]
# # #     #     l=ll
# # # x=l[0]
# # # z=x%a
# # # print(z)


# # a=int(input())
# # l=[i for i in range(1,a+1)]
# # n=int(input())
# # i=0
# # c=1
# # while len(l)!=1:
# #     if c%n==0:
# #         l.remove(i)
# #     if c%10==n:
# #         l.remove(i)
# #     if a-1==i:
# #         i=0
# #     else:
# #         i+=1
# #     c+=1
# # print(l)



# # elements = ['a','b','c','d','e','f','g','h','i']
# # count1= 1
# # n=len(elements)
# # i=0
# # while(elements.count('-')<n-1):
# #     if i==n:
# #         i=0
# #     if elements[i]!='-':
# #         if count1%4==0 or count1%10==4:
# #             count1+=1
# #             elements[i]='-' 
# #         if elements[i]!='-':
# #             count1+=1
# #     i+=1
# # print(elements)


# from curses.ascii import NL


# a=int(input())
# l=[chr(i+64) for i in range(1,a+1)]
# n=int(input())
# c=1
# i=0
# while len(l)>1:
#     if c%n==0 or c%10==n:
#         c+=1
#         print(l)
#         print(l[i])
#         l.remove(l[i])
#     if i==n:
#         i=0
#     c+=1
#     i+=1
# print(l)
    


# a=int(input())
# l=[chr(i+64) for i in range(1,a+1)]
# n=int(input())
# c=1
# i=0
# while len(l)!=1:
#     print(l)
#     if c%n==0 or c%10==n:
#         l.remove(l[i])
#         c+=1
#     # if c%10==n:
#     #     l.remove(l[i])
#     #     c+=1
#     if len(l)-1==i:
#         i=0
#         c+=1
#     else:
#         i+=1
#         c+=1
# print(l)


# a=int(input())
# l=[chr(i+64) for i in range(1,a+1)]
# n=int(input())
# c=1
# i=0
# while len(l)!=1:
#     print(l)
#     if c%n==0 or c%10==n:
#         l.remove(l[i])
#         i-=1
#     if i==len(l)-1:
#         i=0
#     c+=1
#     i+=1
# print(l)


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