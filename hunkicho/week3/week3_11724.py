# https://www.acmicpc.net/problem/11724
# https://velog.io/@devjuun_s/%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98-%EB%B0%B1%EC%A4%80-11724%EB%B2%88python


# RecursionError는 재귀와 관련된 에러
# 가장 많이 발생하는 이유는 Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때
import sys

sys.setrecursionlimit(10**6) 

v, e = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
check = 0

for _ in range(e):
    start, end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

visit = [False] * (v + 1)

def dfs(node):
    visit[node] = True
    for i in graph[node]:
        if visit[i] != True:
            dfs(i)

for j in range(1,v + 1):
    if not visit[j]:     # 분리되어 있으면 visit가 False 이기 때문에 check + 1
        check += 1           
        dfs(j)
print(check)