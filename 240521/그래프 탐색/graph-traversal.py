n, m = map(int, input().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1  # 무방향 그래프이므로 양쪽 다 연결

def dfs(v):
    for i in range(1, n + 1):  # n을 사용하여 노드 범위를 순회
        if arr[v][i] and not visited[i]:
            visited[i] = 1  # 방문 표시를 1로
            dfs(i)

visited[1] = 1  # 시작 노드를 방문 표시
dfs(1)
print(sum(visited))  # 방문한 노드의 개수를 출력