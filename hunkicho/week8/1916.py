# https://www.acmicpc.net/problem/1916

import sys
from collections import deque

city = int(sys.stdin.readline().strip())
bus = int(sys.stdin.readline().strip())
graph = [[] for _ in range(city + 1)]
visit = [1001 * 100001] * (city + 1)

for i in range(bus):
    s, e, d = map(int, sys.stdin.readline().split())
    graph[s].append([e, d])

s_city, e_city = map(int, sys.stdin.readline().split())

def bfs(a: int, c: int) -> None:
    q = deque()
    q.append([a, c])

    while q:
        s, d = q.popleft()
        
        for i in graph[s]:
            if visit[i[0]] > d:
                visit[i[0]] = d
            q.append([i[0], visit[i[0]]])


bfs(1, 0)
print(visit)