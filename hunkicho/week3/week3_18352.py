# https://www.acmicpc.net/problem/18352

# import sys
# from collections import deque

# n, m, k, x = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(n + 1)]
# visit = [0] * (n + 1)
# just = 0

# for _ in range(m):
#     start, end = map(int, sys.stdin.readline().split())
#     graph[start].append(end)

# def bfs(node):
#     global just
#     q = deque([node])

#     while q:
#         n = q.popleft()
#         for i in graph[n]:
#             if visit[i] == 0 or visit[i] > visit[n] + 1:
#                 q.append(i)
#                 visit[i] = visit[n] + 1
#                 just = 1

# bfs(x)

# if just == 0:
#     print(-1)
# else:
#     for j in range(len(visit)):
#         if visit[j] == k:
#             print(j)
#             just = 1


# 83%에서 틀림
import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
just = 0

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

def bfs(node):
    global j
    q = deque([node])
    visit[node] = 0

    while q:
        n = q.popleft()
        for i in graph[n]:
            
            if visit[i] == 0:
                q.append(i)
                visit[i] = visit[n] + 1

bfs(x)
for j in range(len(visit)):
    if visit[j] == k:
        print(j)
        just = 1
if just == 0:
    print(-1)