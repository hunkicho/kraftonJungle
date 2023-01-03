import sys
from collections import deque

# f: 건물 총 높이
# s: 현재 층
# g: 스타트링크 층
# u: u층 위로 이동
# d: d층 아래로 이동

def bfs(s: int) -> None:
    count = 0
    visit[s] = True
    q = deque([s])
    
    while q:
        
        n = q.popleft()
        print("n=",n)
        if n == g:
            print(count)
            return
        count += 1
        for i in graph[n]:
            for j in range(2):
                if i[j] > 0 and i[j] <= f:
                    if not visit[i[j]]:
                        q.append(i[j])
                        visit[i[j]] = True
    print("use the stairs")
                    
                    
    


if __name__ == "__main__":
    f, s, g, u, d = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(f + 1)]
    visit = [False] * (f + 1)

    if (s > g and d == 0) or (s < g and u == 0):
        print("use the stairs")
    else:
        for i in range(1,f + 1):
            graph[i].append([i+u, i+d])
        bfs(s)