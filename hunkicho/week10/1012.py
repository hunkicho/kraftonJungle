# https://www.acmicpc.net/problem/1012
# https://hongcoding.tistory.com/72


# 여기서 막힘
# import sys
# from collections import deque

# def bfs(y: int, x: int):
#     visit[y][x] = True
#     q = deque([y, x])
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
    

#     while q:
#         qy, qx,   = q.popleft()

#         for i in range(4):
#             ny = qy + dy[i]
#             nx = qx + dx[i]

#             if not visit[ny][nx]:
#                 q.append([ny , nx])
#                 visit[ny][nx] = True


# if __name__ == "__main__":
#     test_case = int(sys.stdin.readline())
#     for _ in range(test_case):
#         width, height, count = map(int, sys.stdin.readline().split())
#         graph = [[0] * width  for _ in range(height)]
#         visit = [[False] * width  for _ in range(height)]

#         for _ in range(count):
#             x, y = map(int, sys.stdin.readline().split())
#             graph[y][x] = 1

#         bfs(0,0)



# 블로그 봤다.
# 리스트에 담고 1인것만 탐색한다 까지는 생각완료
# 어떻게 탐색할지 구현 못함


import sys
from collections import deque

def bfs(x: int, y: int) -> None:
    q = deque()
    q.append([x, y])                                                    # 나중에 popleft 할 때 여러개 뽑으려면 처음에 선언할 때 초기화 하지 말고 나중에 추가해야 함 

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    graph[x][y] = 0                                                      # 방문한 곳은 0으로 처리하여 다음에 방문 안하게

    while q:
        qx, qy = q.popleft()

        for i in range(4):                                               # 상하좌우 탐색
            nx = qx + dx[i]
            ny = qy + dy[i]

            if nx < 0 or nx >=height or ny < 0 or ny >= width:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0                                         # 방문한 곳은 0으로 처리하여 다음에 방문 안하게
                q.append([nx, ny])


if __name__ == "__main__":
    test_case = int(sys.stdin.readline())                                 # 테스트 케이스
    for _ in range(test_case):
        width, height, count = map(int, sys.stdin.readline().split())     # 가로길이, 세로길이, 배추심은 갯수
        graph = [[0] * width  for _ in range(height)]                     # 그래프 생성
        cnt = 0

        for _ in range(count):                                            # 그래프에 배추 위치 표시
            x, y = map(int, sys.stdin.readline().split())
            graph[y][x] = 1

        for i in range(height):                                           # 그래프 돌면서 배추 심은 곳이면 BFS
            for j in range(width):
                if graph[i][j] == 1:
                    bfs(i,j)
                    cnt += 1                                              # 연결된 배추 다 탐색했으면 카운트 +1
        print(cnt)