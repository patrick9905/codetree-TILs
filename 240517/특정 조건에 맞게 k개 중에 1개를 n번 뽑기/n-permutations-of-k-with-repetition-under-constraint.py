k,n=tuple(map(int,input().split()))

a=[]
def choose(num):
    if num>=n:
        print(*a)
        return
        
    for i in range(1,k+1):
        if num>=2 and a[-1]==a[-2] and a[-1]==i:
            continue
        a.append(i)
        choose(num+1)
        a.pop()


choose(0)