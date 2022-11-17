# https://www.acmicpc.net/problem/2665

# https://devlibrary00108.tistory.com/562

import sys
import heapq

count = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(count)]
visited = [[0] * count for _ in range(count)]

def dijkstra():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = []
    heapq.heappush(q,[0,0,0])
    visited[0][0] = True

    while q:
        cnt, x, y = heapq.heappop(q)
        if x == count - 1 and y == count - 1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= count or ny >= count or nx < 0 or ny < 0:  # 범위 벗어났으면
                continue

            if visited[nx][ny] == True:           # 방문한적 있으면
                continue

            visited[nx][ny] = True                # 방문처리
            if graph[nx][ny] == 0:
                heapq.heappush(q,[cnt + 1, nx, ny])    # 뚫어야 되니까 + 1 
            elif graph[nx][ny] == 1:
                heapq.heappush(q,[cnt,nx,ny])          # 가면 되니까 그대로
  
print(dijkstra())