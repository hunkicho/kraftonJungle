# https://www.acmicpc.net/problem/2178

# https://ji-gwang.tistory.com/295

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 한 점을 기준으로 (위, 아래, 왼쪽, 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(a,b):
    
    q = deque()
    q.append([a,b])

    while q:
        x, y = q.popleft()
        
        for i in range(4): #좌우상하
            nx = x + dx[i] # 행값
            ny = y + dy[i] # 열값

            if nx >= n or ny >= m or nx < 0 or ny < 0:    # 미로 범위 벗어났으면
                continue

            if graph[nx][ny] == 1:                        # 해당 좌표 이동 가능하면 (1이면), 왔던데 아니면(좌표값 업데이트 했으면 좌표값은 2 이상이다)
                graph[nx][ny] = graph[x][y] + 1           # 해당 좌표값(1) = 현재좌표값(1) + 1
                q.append([nx, ny])                        # 해당 좌표에서 또 이동

    return graph[n - 1][m - 1]                            # 탐색 다 했으면 해당 좌표 값 구하기(배열 0번째 부터 해서 -1)

print(bfs(0,0))