n=int(input())
arr=list(map(int,input().split()))
max1=arr[0]

min=arr[0]

for i in arr:
    if i > max1:
        max1=i
    if i < min:
        min=i

for i in range(n):
    if arr[i]==max1:
        arr[i]=min

max2=arr[0]
for j in range(n):
    if arr[j]>max2:
        max2=arr[j]

print(max1, max2)