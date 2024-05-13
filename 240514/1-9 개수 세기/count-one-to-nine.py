arrm=[0]*10
n=int(input())
arr = list(map(int, input().split()))
for i in arr:
    arrm[i]+=1

for i in range(1,10):
    print(arrm[i])