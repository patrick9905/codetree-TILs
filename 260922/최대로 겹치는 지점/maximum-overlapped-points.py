n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x=[0]*101
for i,j in segments:
    for idx in range(i-1,j):
        x[idx]+=1

print(max(x))

# Please write your code here.