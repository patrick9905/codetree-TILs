n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    if a%2==0:
        arr.append(a)

for i in arr[::-1]:
    print(i,end='')