arr=list(map(int,input().split()))
arrn=[]
for i in arr:
    if i==0:
        break
    if i%2==0:
        arrn.append(int(i/2))
    else:
        arrn.append(i+3)

for i in arrn:
    print(i,end=' ')