# https://www.acmicpc.net/problem/1707
# https://only-wanna.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1707%EB%B2%88-%EC%9D%B4%EB%B6%84-%EA%B7%B8%EB%9E%98%ED%94%84

import sys
sys.setrecursionlimit(20000)

def dfs(node,group):
    global err                # error check

    if err:
        return                # error 나면 바로 return

    visit[node] = group       # 해당 그룹으로 vertex 등록

    for k in graph[node]:     # 해당 vertex에 연결된 것들중
        if not visit[k]:      # 아직 방문안했으면 
            dfs(k,-group)
        elif visit[node] == visit[k]:  # 인접한데 같은 그룹이면
            err = True                 # error
            return

test_case = int(sys.stdin.readline().strip())

for _ in range(test_case):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    visit = [False] * (v + 1)
    err = False

    for _ in range(e):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
    
    for i in range(1, v + 1):
        if not visit[i]:     # 아직 방문안했으면
            dfs(i,1)         # dfs
            if err:          # dfs가 error 후 리턴했으면
                break        # 멈춤
    
    if err:
        print("NO")
    else:
        print("YES")