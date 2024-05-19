arr=[0]*4

for _ in range(3):
    a=list(input().split())
    if a[0]=='Y' and int(a[1])>=37:
        arr[0]+=1
    elif a[0]=='N' and int(a[1])>=37:
        arr[1]+=1
    elif a[0]=='Y' and int(a[1])<37:
        arr[2]+=1
    else:
        arr[3]+=1

if int(arr[0])>=2:
    arr.append('E')

print(*arr)