n = int(input())
arr=[]
ans=0
def backtracking():
    global ans
    if len(arr)==n:
        ans+=1
        return
    for i in range(1,5):
        if len(arr)+i>n:
            continue
        for _ in range(i):
            arr.append(i)
        backtracking()
        for _ in range(i):
            arr.pop()

backtracking()
print(ans)       
# Please write your code here.
