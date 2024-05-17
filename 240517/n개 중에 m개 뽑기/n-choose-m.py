n,m=tuple(map(int,input().split()))
a=[]
def f(curr,l):
    if curr>=m+1:
        print(*a)
        return
    for v in range(l+1,n+1):
        a.append(v)
        f(curr+1,v)
        a.pop()

f(1,0)
# n,m=tuple(map(int,input().split()))

# a=[]
# def choose(num,cnt):
#     if num>=n+1:
#         if cnt==m:
#             print(*a)
#         return
    
#     choose(num+1,cnt)
#     a.append(num)
#     choose(num+1,cnt+1)
#     a.pop()
    
# choose(1,0)