# https://www.acmicpc.net/problem/21606

import sys

count = int(sys.stdin.readline().strip)
loca = str(sys.stdin.readline().strip)
graph = [[] for _ in range(count + 1)]
visit = [False] * (count + 1)
first = True

for _ in range(count):
    start, end = map(int, sys.stdin.readline().split())

    graph[start].append(end)
    graph[end].append(start)

def dfs(node,i):
    if first:
        if i == "0":
            first = False
            return

    visit[node] = i

    for i in graph[node]:
        if not visit[i]:
            dfs(i,i+1)
    
    if i == "0":
        re

for j in range(count + 1):
    if not visit[j]:
        dfs(j,str(loca)[j])