k,n=tuple(map(int,input().split()))
a=[]


def p():
    for i in a:
        print(i,end=' ')
    print()
def choose(num):
    if num==n:
        for i in range(n):
            if a[i-1]==a[i-2] and a[i-2]==a[i-3]:
                return
        p()
        return
    for i in range(1,k+1):
        
        a.append(i)
        choose(num+1)
        a.pop()

choose(0)