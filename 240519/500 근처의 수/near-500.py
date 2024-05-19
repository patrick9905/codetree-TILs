arr=list(map(int,input().split()))
max_u=0
min_u=999
for i in arr:
    if i>500 and i< min_u:
        min_u=i
    elif i<500 and i>max_u:
        max_u=i

print(max_u, min_u)