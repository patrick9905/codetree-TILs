arr=[]
for i in range(10):
    arr.append(input())

n=input()
cnt=0
for i in arr:
    if i[-1]==n :
        print(i)
        cnt+=1
if cnt==0:
    print('None')