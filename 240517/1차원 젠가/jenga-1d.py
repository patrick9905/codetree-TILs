n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

def delete(a,s,e):
    for i in range(s,e+1):
        a[i]=0
def down(a):
    tmp=[]
    for i in a:
        if i!=0:
            tmp.append(i)
    return tmp

for _ in range(2):
    s,e=tuple(map(int,input().split()))
    s,e=s-1,e-1
    delete(a,s,e)
    a=down(a)

print(len(a))
for i in a:
    print(i)