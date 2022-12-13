# https://www.acmicpc.net/problem/2606

import sys
c = 0
def dfs(node: int) -> int:
    global c
    
    visit[node] = True

    for i in graph[node]:
        if not visit[i]:
            c += 1
            dfs(i)
    return c

v = int(sys.stdin.readline().strip())
e = int(sys.stdin.readline().strip())
graph = [[] for _ in range(v + 1)]
visit = [False] * (v + 1)

for _ in range(e):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

print(dfs(1))