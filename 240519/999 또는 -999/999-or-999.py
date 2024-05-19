arr=list(map(int,input().split()))
max1=arr[0]
min1=arr[0]
for i in arr:
    if i==999 or i==-999:
        break
    if i>max1:
        max1=i
    if i<min1:
        min1=i

print(max1,min1)