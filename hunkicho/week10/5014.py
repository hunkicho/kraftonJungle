import sys
from collections import deque

# f: 건물 총 높이
# s: 현재 층
# g: 스타트링크 층
# u: u층 위로 이동
# d: d층 아래로 이동

def bfs(s: int) -> None:
    visit[s] = True                                        # 방문 처리
    q = deque([s])                                         # 큐 선언
    
    while q:
        
        n = q.popleft()

        if n == g:                                         # 스타트링크에 도착 했으면
            print(result[n])
            return

        for i in graph[n]:
            for j in range(2):
                if i[j] > 0 and i[j] <= f:                 # 도착한 층은 0 < 층 <= 건물 높이 
                    if not visit[i[j]]:                    # 방문한적 없으면
                        q.append(i[j])
                        visit[i[j]] = True                 # 방문처리
                        result[i[j]] = result[n] + 1       # 버튼 누른 횟수 저장
    print("use the stairs")
                    
                    
    


if __name__ == "__main__":
    f, s, g, u, d = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(f + 1)]
    visit = [False] * (f + 1)
    result = [0] * (f + 1)

    if (s > g and d == 0) or (s < g and u == 0):
        print("use the stairs")
    else:
        for i in range(1,f + 1):
            graph[i].append([i+u, i-d])
        bfs(s)