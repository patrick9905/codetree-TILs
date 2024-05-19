n=int(input())
arr=[]
max=0
for i in range(n):
    if i not in arr:
        arr.append(i)
for j in arr:
    if max<j:
        max=j
if len(arr)==0:
    print(-1)
else:
    print(max)