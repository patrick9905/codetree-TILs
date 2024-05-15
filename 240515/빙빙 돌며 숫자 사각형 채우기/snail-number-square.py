n, m= map(int,input().split())
answer = [
    [0] * m
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n


dys, dxs = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0          
dir_num = 0           
answer[y][x] = 1

for i in range(2, n*m+1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    if not in_range(nx, ny) or answer[ny][nx] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]  

    x, y = nx, ny  
    answer[y][x] = i 

for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()