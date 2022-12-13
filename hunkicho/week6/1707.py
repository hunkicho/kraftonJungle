# https://www.acmicpc.net/problem/1707
# 이분그래프
# 인접한 노드끼리 같은 색깔이면 이분그래프가 아니다.

import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, g):
    # 방문 시 색깔 지정(여기선 1, -1)
    visit_dfs[node] = g

    for i in graph[node]:
        # 방문 안했으면 dfs 수행
        if not visit_dfs[i]:
            if not dfs(i, -g):   # 아래 조건문에서 그룹이 같아서 false 리턴하면 여기도 조건이 성립되어서 false 리턴함
                return False
        # 방문한 노드면 인접 노드와 그룹이 같으면
        elif visit_dfs[i] == visit_dfs[node]:
            return False
    # 위에 반복문에서 걸러지지 않았으면(인접한 노드끼리 그룹이 같지 않으면) True 리턴
    return True    

test_case = int(sys.stdin.readline())


for _ in range(test_case):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v+1)]
    visit_dfs = [False] * (v + 1)
    for _ in range(e):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    ans = True
    for j in range(1, v + 1):
        if visit_dfs[j] == False:
            ans = dfs(j, 1)
            if not ans:
                break
    print("YES" if ans else "NO")