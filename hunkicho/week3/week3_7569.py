# https://www.acmicpc.net/problem/7569

# 병휘형의 코드
# https://www.acmicpc.net/source/share/23f2a2601445480da81d86024e490633

import sys
from collections import deque

# m -> 칸의 가로
# n -> 칸의 세로
# h -> 상자 수

m, n, h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)] # 3차원 배열로
start_point = []

dx = [-1,1,0,0,0,0]  # 좌우
dy = [0,0,-1,1,0,0]  # 상하
dh = [0,0,0,0,-1,1]  # 위 아래

# 반복문 돌며 익어 있는 토마토 위치 찾는다.
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                start_point.append((i,j,k,0))
#print(start_point)
#[(0, 1, 3, 0), (0, 1, 4, 0), (0, 2, 3, 0), (0, 2, 4, 0)]
#[[0, 1, 3, 0], [0, 1, 4, 0], [0, 2, 3, 0], [0, 2, 4, 0]]
T = 0
def bfs():
    global start_point, T
    global print_cnt
    q = deque(start_point)
    # deque()에 값 넣으면 원소 한개씩 넣는데, append로 넣으면 원소들을 한개로 넣는다
    #q.append(start_point)
    #print(q)
    # [], deque() ->       deque([[0, 1, 3, 0], [0, 1, 4, 0], [0, 2, 3, 0], [0, 2, 4, 0]])
    # (), deque() ->       deque([(0, 1, 3, 0), (0, 1, 4, 0), (0, 2, 3, 0), (0, 2, 4, 0)])
    # (), deque.append ->  deque([[(0, 1, 3, 0), (0, 1, 4, 0), (0, 2, 3, 0), (0, 2, 4, 0)]])

    while q:
        h, y, x, t = q.popleft()
        print(h,y,x,t)
        T = max(T, t)
        for z in range(6):
            print("z=",z)
            nx = x + dx[z]  # n
            ny = y + dy[z]  # m
            nh = h + dh[z]

            if nx >= n or ny >= m or nh >= h or nx < 0 or ny < 0 or nh < 0:
                print("1111",nh,ny,nx,t)
                continue

            if graph[nh][ny][nx] == -1 or graph[nh][ny][nx] == 1:
                print("2222",nh,ny,nx,t)
                continue

            graph[nh][ny][nx] = 1
            print("3333")
            q.append([nh,ny,nx,t+1]) 

print(graph)

bfs()

flag = True
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                flag = False

if flag:
    print(T)
else:
    print(-1)

# from collections import deque
# import sys
# input = sys.stdin.readline

# dr = (0, 1, 0, -1, 0, 0)
# dc = (1, 0, -1, 0, 0, 0)
# dl = (0, 0, 0, 0, 1, -1)

# m, n, h = map(int, input().split()) # c, r, h
# a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# t = []

# print(a)

# for k in range(h): # l
#     for i in range(n): # r
#         for j in range(m): # c
#             if a[k][i][j] == 1: 
#                 t.append((k, i, j)) # d, l, r, c


# def bfs():
#     global t
#     q = deque(t)
#     while q:
#         l, r, c = q.popleft()
#         for i in range(6):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             nl = l + dl[i]
#             if 0 <= nr < n and 0 <= nc < m and 0 <= nl < h:
#                 if a[nl][nr][nc]: continue # 1익은 -1없음 pass
#                 a[nl][nr][nc] = a[l][r][c] + 1
#                 q.append((nl, nr, nc))

# bfs()
# ans = 0
# for i in a:
#     for j in i:
#         for k in j:
#             if k == 0: print(-1); exit(0)
#         ans = max(ans, max(j))
                
# print(ans - 1)