a,b=tuple(map(int,input().split()))
tmp=[0]*b
while(a>1):
    tmp[int(a)%int(b)]+=1
    a=int(a/b)
ans=0
for i in tmp:
    ans+=(i**2)
print(ans)