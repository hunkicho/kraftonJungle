# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# 내가 푼건데 처참히 실패  

# def solution(numbers, target):
#     def dfs(node, rtn, count):
#         #print(node)
#         visit[node] += 1
#         if visit[node] == 1:
#             rtn += numbers[node]
#         else:
#             rtn -= numbers[node]
#         print(rtn)
        
#         if node == len(numbers) - 1:
#             if rtn == target:
#                 count += 1
#                 return count
    
#         for _ in range(2):
            
#             if node < len(numbers) - 1 and  visit[node + 1] != 2:
#                 dfs(node + 1, rtn, count)

#     answer = 0
#     visit = [0 for _ in range(len(numbers))]
    
    
#     print(dfs(0,0,0))
    
    
    
#     return answer
# solution([1, 1, 1, 1, 1], 3)


# 인터넷 보고 가져왔다.

def DFS(n, order, numbers, target):
    if order == len(numbers)-1:
        if n == target:
            return 1
        
        return 0
    
    case1 = DFS(n+numbers[order+1], order+1, numbers, target)
    case2 = DFS(n-numbers[order+1], order+1, numbers, target)
    
    return case1 + case2

def solution(numbers, target):
    return DFS(numbers[0], 0, numbers, target) + DFS(-numbers[0], 0, numbers, target)

# bfs

from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))
    
    while q:
        n, order = q.popleft()
        
        if order == len(numbers)-1:
            if n == target:
                answer += 1
            continue
        
        q.append((n+numbers[order+1], order+1))
        q.append((n-numbers[order+1], order+1))
    
    return answer