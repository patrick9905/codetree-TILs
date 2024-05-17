k,n=tuple(map(int,input().split()))

a=[]
def print1():
    for i in a:
        print(i,end=' ')
    print()

def choose(num):
    if num>=n+1:
        print1()
        return
    for i in range(1,n+1):
        a.append(i)
        choose(num+1)
        a.pop()
    return

choose(1)