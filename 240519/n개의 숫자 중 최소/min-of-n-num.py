n=int(input())
arr=list(map(int,input().split()))
min1=arr[0]
for i in arr:
    if i<min1:
        min1=i
cnt=0
for i in arr:
    if i==min1:
        cnt+=1
print(min1,cnt)