# https://www.acmicpc.net/problem/2606

import sys

v = int(sys.stdin.readline().strip())
e = int(sys.stdin.readline().strip())
graph = [[] for _ in range(v+1)]
check = 0
com = 0

for _ in range(e):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

visit = [False] * (v + 1)

def dfs(node):
    global com
    com += 1
    visit[node] = True
    for j in graph[node]:
        if not visit[j]:
            dfs(j)

# for i in range(1,v + 1):
#     if not visit[i]:
#         check += 1
#         if check >= 2:
#             print(com - 1)
#             exit()

dfs(1)
print(com-1)