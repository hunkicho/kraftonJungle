# https://www.acmicpc.net/problem/2637

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
indegree = [0] * (n + 1)
hap = [[] for _ in range(n + 1)]
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(n + 1)]

#방향 그래프의 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c]) # vertex A에서 B로 이동 가능
    # 진입 차수를 1 증가
    indegree[b] += 1
    hap[b].append([a,c])
print("firsthap",hap)
# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        #큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        if hap[now] == 0:
            hap[now] = 1

        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        
        for i in graph[now]:
            indegree[i[0]] -= 1
            hap[i[0]] = hap[now] * hap[i[0]]
            print("노드",i[0], "의 합은",hap[now] * hap[i[0]])
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i[0]] == 0:
                q.append(i[0])
            hap[now] = 0
            print(now,"의 합은",hap[now])
    
    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')
    print(hap)

topology_sort()

[[], [], [], [], [], [[1, 2], [2, 2]], [[5, 2], [3, 3], [4, 4]], [[5, 2], [6, 3], [4, 5]]]