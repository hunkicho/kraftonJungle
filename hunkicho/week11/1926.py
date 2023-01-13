import sys
from collections import deque

def bfs(x: int, y:int) -> int :
    q = deque()
    q.append((x, y))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    calc_width = 1                                                                  # 그림 크기. bfs내부에 진입했으면 일단 1이 하나 있다는 말이기 때문에 처음 크기를 1로 초기화

    graph[x][y] = 0                                                                 # 방문한 곳은 0으로 초기화 하여 이후 다시 방문하지 않도록 함

    while q:
        qx, qy = q.popleft()
        
        for k in range(4):
            nx = qx + dx[k]
            ny = qy + dy[k]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
        
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0                                                   # 방문한 곳은 0으로 초기화 하여 이후 다시 방문하지 않도록 함
                calc_width += 1                                                     # 그림 크기 계산

    return calc_width
    

if __name__ == "__main__":
    # n: 가로길이
    # m: 세로길이
    n , m = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]           # 탐색할 그래프 생성
    pic_count = 0
    pic_width = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                rtn_value = bfs(i, j)
                pic_width = rtn_value if rtn_value > pic_width else pic_width           # 리턴 받은 그림 크기 중 최대값 저장
                pic_count += 1                                                          # 그림 갯수 계산

    print(pic_count)
    print(pic_width)