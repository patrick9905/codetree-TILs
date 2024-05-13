arr=[0]*10
a,b=map(int,input().split())
arr.append(a)
arr.append(b)
for i in range(3,10):
    arr[i]=arr[i-1]+arr[i-2]*2

for i in arr:
    print(i,end=' ')