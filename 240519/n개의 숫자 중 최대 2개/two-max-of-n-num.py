n=int(input())
arr=list(map(int,input().split()))
max1=arr[0]
max2=arr[0]
min=arr[0]

for i in arr:
    if i > max1:
        max1=i
    if i < min:
        min=i
print(min)
for i in range(n):
    if arr[i]==max1:
        arr[i]=min

print(*arr)
for i in range(n):
    if arr[i]>max2:
        max2=arr[i]
print(max1, max2)