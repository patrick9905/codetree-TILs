n = int(input())
x, y = 0, 0
ans = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
reach_home = False

for i in range(n):
    direction, distance = input().split()
    distance = int(distance)
    
    if direction == 'N':
        dir_num = 0
    elif direction == 'E':
        dir_num = 1
    elif direction == 'S':
        dir_num = 2
    elif direction == 'W':
        dir_num = 3

    for j in range(distance):
        x += dx[dir_num]
        y += dy[dir_num]
        ans += 1
        if x == 0 and y == 0:
            print(ans)
            reach_home = True
            break
    
    if reach_home:
        break

if not reach_home:
    print(-1)