n=input()
arr= list(map(int,input().split()))
arrn=[i**2 for i in arr]
for i in arrn:
    print(i,end=' ')