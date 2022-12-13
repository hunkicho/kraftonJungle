# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node: int) -> None:
    visit[node] = True

    for i in graph[node]:
        if not visit[i]:
            dfs(i)

v, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(v + 1)]
visit = [False] * (v + 1)
count = 0

for _ in range(e):
    start, end = map(int, sys.stdin.readline().split())

    graph[start].append(end)
    graph[end].append(start)

for i in range(1, v + 1):
    
    if not visit[i]:
        count += 1
        dfs(i)

print(count)