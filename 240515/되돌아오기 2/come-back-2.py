n=input()
x,y=0,0
dx,dy=[1,0,-1,0],[0,-1,0,1]
dir_num=3
t=0
for i in range(len(n)):
    if n[i]=='F':
       x+=dx[dir_num]
       y+=dy[dir_num] 
    elif n[i]=='R':
        dir_num=(dir_num+1)%4
    elif n[i]=='L':
        dir_num=(dir_num+3)%4
    t+=1
    if x==0 and y==0:
        print(t)
print(-1)