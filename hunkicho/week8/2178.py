# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

def bfs(a: int, b: int) -> None:
    q = deque()
    q.append([a, b])

    while q:
        x, y =q.popleft()
        
        # bfs 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위 벗어났으면
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            # 1일 때만 이동할 수 있고, 값이 1이면 아직 방문을 하지 않았다는 의미
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
    print(graph[n-1][m-1])

n, m = map(int, sys.stdin.readline().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(n):
    line = list(map(int, sys.stdin.readline().strip()))
    graph.append(line)

bfs(0,0)