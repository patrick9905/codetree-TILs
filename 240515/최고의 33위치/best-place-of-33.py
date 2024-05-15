n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
ans=0
for y in range(n-2):
    for x in range(n-2):
        cnt=0
        for i in range(y,y+3):
            for j in range(x,x+3):
                cnt+=a[i][j]
        ans=max(ans,cnt)
print(ans)