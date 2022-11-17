# https://www.acmicpc.net/problem/1260
# https://velog.io/@sobing/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-1260%EB%B2%88-DFS%EC%99%80-BFS

import sys
from collections import deque

v,e,s = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
for _ in range (e):
    start, end = map(int,sys.stdin.readline().split())  # edge 입력받기
    graph[start].append(end)   # start에 연결된 node append
    graph[end].append(start)   # end에 연결된 node append
    graph[start].sort()        # 정렬
    graph[end].sort()          # 정렬
visit_bfs = [False] * (v+1)    # 방문여부 배열 초기화
visit_dfs = [False] * (v+1)    # 방문여부 배열 초기화

def dfs(node):
    visit_dfs[node] = True     # 방문시 방문여부 -> True
    print(node,end=' ')        # 방문했으므로 print
    for n in graph[node]:      # 해당 node에 연결된 배열 반복
        if not visit_dfs[n]:   # 방문 안했으면
            dfs(n)             # 재귀

def bfs(node):
    visit_bfs[node] = True     # 방문시 방문여부 -> True
    q = deque([(node)])          # 큐 선언

    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if not visit_bfs[i]:    # 해당 노드 자식들 전부 append
                q.append(i)
                visit_bfs[i] = True

dfs(s)
print()
bfs(s)