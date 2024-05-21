n,m=map(int,input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited=[0 for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    arr[a][b]=1
    arr[b][a]=1

def dfs(v):
    for i in range(1,m+1):
        if arr[v][i] and not visited[i]:
            visited[i]=True

            dfs(i)
visited[1]=1
dfs(1)
print(sum(visited))