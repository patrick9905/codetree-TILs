n = int(input())

painted = {}
start = 0

for _ in range(n):
    x, direction = input().split()
    x = int(x)

    if direction == 'L':
        for pos in range(start - x, start):
            painted[pos] = painted.get(pos, 0) + 1
        start -= x
    else:
        for pos in range(start, start + x):
            painted[pos] = painted.get(pos, 0) + 1
        start += x

answer = sum(count >= 2 for count in painted.values())
print(answer)