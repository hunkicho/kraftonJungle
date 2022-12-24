# https://www.acmicpc.net/problem/18352

import sys
from collections import deque

def bfs(node: int, group: int):
    visit[node] = True
    q = deque()
    q.append([node, group])

    while q:
        n = q.popleft()
        group = n[1] + 1
        for i in graph[n[0]]:
            if not visit[i]:
                q.append([i, group])
                visit[i] = True
                visit_distance[i] = group

v, e, k, x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(v + 1)]
visit = [False] * (v + 1)
visit_distance = [False] * (v + 1)

for i in range(e):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

bfs(x, 0)

if visit_distance.count(k) < 1:
    print(-1)
else:
    for j in range(1, v + 1):
        if visit_distance[j] == k:
            print(j)