# https://www.acmicpc.net/problem/1197



# 이거는 시간초과
# https://0x15.tistory.com/36

# 특정 원소가 속한 집합을 찾기
# def find(x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]


# # 두 원소가 속한 집합을 합치기
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b


# # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
# v, e = map(int, input().split())
# parent = [0] * (v + 1)  # 부모 테이블 초기화하기

# # 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
# edges = []
# result = 0

# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(1, v + 1):
#     parent[i] = i

# # 모든 간선에 대한 정보를 입력 받기
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
#     edges.append((cost, a, b))

# # 간선을 비용순으로 정렬
# edges.sort()

# # 간선을 하나씩 확인하며
# for edge in edges:
#     cost, a, b = edge
#     # 사이클이 발생하지 않는 경우에만 집합에 포함
#     if find(a) != find(b):
#         union(a, b)
#         result += cost

# print(result)



# https://hillier.tistory.com/54
# Kruskal 알고리즘 이용

# 1. root를 저장하는 Vroot 배열 생성(여기서 root는 연결요소 중 가장 작은 값, 처음에는 자기 자신을 저장)
# 2. 간선들(Elist)을 가중치 기준으로 정렬
# 3. 간선들이 이은 두 정점을 find 함수를 통해 두 root(sRoot eRoot)를 찾는다.
# 4. 두 root가 다르다면 큰 root값을 작은 root값으로 만들어 연결되게 해준다.
# 5. 가중치를 더한다.

import sys
input = sys.stdin.readline
 
V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split()))) # edge 정보
 
Elist.sort(key=lambda x: x[2]) # kruskal 사용하기 위해 가중치 기준으로 오름차순 정렬
 
def find(x):
    print(Vroot)
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
 
answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:  # 같은 곳 온게 아니면(cycle이 아니면)
        if sRoot > eRoot: 
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
 
print(answer)