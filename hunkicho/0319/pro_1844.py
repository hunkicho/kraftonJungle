# https://school.programmers.co.kr/learn/courses/30/lessons/1844

#print( [[0] * 5 for _ in range(4)] )
#a = [[]] * 5
#print(a)


from collections import deque

from collections import deque

def bfs(x,y,maps):
    n = len(maps[0]) - 1
    m = len(maps) - 1
    visit = [[0 for _ in range(n + 1)]  for _ in range(m + 1)]
    print(visit)
    visit[0][0] = 1
    
    q = deque([(x, y)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0 ,1, -1]
    
    while q:
        nx, ny= q.popleft()
        
        for i in range(4):
            if nx + dx[i] < 0 or nx + dx[i] > m or ny + dy[i] < 0 or ny + dy[i] > n:
                continue
            if visit[nx + dx[i]][ny + dy[i]] == 0:
                if maps[nx + dx[i]][ny + dy[i]] == 1:
                    visit[nx + dx[i]][ny + dy[i]] = visit[nx][ny] + 1
                    q.append((nx + dx[i], ny + dy[i]))
                        
    if visit[m][n] == 0:
        return -1
    else:
        return visit[m][n]
        

def solution(maps):
    answer = 0
    answer = bfs(0,0,maps)
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))