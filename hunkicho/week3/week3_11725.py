# https://www.acmicpc.net/problem/11725

# 트리의 부모 찾기
# 루트가 없는 트리가 주어진다. 이때 트리의 루트는 1이라 가정
# 두 정점이 주어지는데 어떤게 부모인지 모름
# 처음 방문할 때 마다 그 전에 방문한 노드 기록 후 출력


import sys
sys.setrecursionlimit(10 ** 6)

count = int(sys.stdin.readline().strip())
graph = [[] for _ in range(count + 1)]

for _ in range(count - 1):
    start, end = map(int, sys.stdin.readline().split())

    graph[start].append(end)
    graph[end].append(start)

#print(graph)
visit_dfs = [False] * (count + 1)

def dfs(node):
    for i in graph[node]:
        if visit_dfs[i] == False:
            visit_dfs[i] = node
            dfs(i)
dfs(1)

for j in range(2, count + 1):
    print(visit_dfs[j])