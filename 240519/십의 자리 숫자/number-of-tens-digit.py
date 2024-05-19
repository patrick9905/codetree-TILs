arr=list(map(int,input().split()))
ar=[0]*11
for i in arr:
    if i==0:
        break
    ar[int(i/10)]+=1

for i in range(1,10):
    print(f"{i} - {ar[i]}")