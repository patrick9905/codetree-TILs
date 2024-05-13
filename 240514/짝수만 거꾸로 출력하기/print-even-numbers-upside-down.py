n=int(input())
arr=list(map(int,input().split()))
arrn=[]
for i in arr:
    if int(i)%2==0:
        arrn.append(i)

for i in arrn[::-1]:
    print(i,end=' ')