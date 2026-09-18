n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
m=input()
sum=0
cnt=0
for i in arr:
    if i[0]==m:
        sum+=len(i)
        cnt+=1

print(cnt,f'{sum/cnt:.2f}')
