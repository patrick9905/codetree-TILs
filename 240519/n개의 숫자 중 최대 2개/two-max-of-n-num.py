n=int(input())
arr=list(map(int,input().split()))
max1=arr[0]
max2=arr[0]
arr1=[]
for i in arr:
    if i > max1:
        max1=i
for i in range(n):
    if arr[i]==max1:
        arr[i]=arr[0]
for i in arr:
    if i>max2:
        max2=i
print(max1, max2)