n,t=tuple(map(int,input().split()))
r,c,d=tuple(input().split())

D={'R':1,'D':3,'U':0,'L':2}
r=int(r)-1
c=int(c)-1
dxs, dys = [0, 1, -1, 0], [-1, 0, 0, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n
i=0
move_dir=D[d]
for _ in range(t):

    nx,ny=r+dys[move_dir],c+dxs[move_dir]
    if not in_range(nx,ny):
        move_dir=3-move_dir
    else:
        r,c=nx,ny
print(r+1,c+1)