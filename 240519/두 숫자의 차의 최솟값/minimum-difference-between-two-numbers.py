n=int(input())
arr=list(map(int,input().split()))
min=100
for i in range(len(arr)-1):
    if abs(arr[i]-arr[i+1])<min:
        min= abs(arr[i]-arr[i+1])

print(min)