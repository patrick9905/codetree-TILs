n=int(input())
a=[]
visited=[False]*(n+1)
def f(num):
    if num>=n+1:
        print(*a)
        return
    for i in range(1,n+1):
        if visited[i]==True:
            continue
        a.append(i)
        visited[i]=True
        
        f(num+1)
        a.pop()
        visited[i]=False

f(1)