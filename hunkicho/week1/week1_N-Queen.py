# https://www.acmicpc.net/problem/9663

# import sys
# from turtle import width
# n = int(sys.stdin.readline())

# all_page = [0] * n #열
# a = [False] * n #행
# b = [False] * ((n * 2) - 1) #정방향 대각
# c = [False] * ((n * 2) - 1) #역방향 대각


# def queen(n) -> None:
#     first = 0
#     count = 0
#     for i in range(n):
#         print("i=",i)
#         if (not a[i] 
#             and not b[first+i]
#             and not c[first-i+(n-1)]
#             ):
#             print("qwe")
#             count += 1
#             if i == n-1:
#                 print(count)
#         else:
#             a[i] = True
#             b[i+first] = True
#             c[i-first+(n-1)] = True
#             queen(first+1)
#             a[i] = False
#             b[i+first] = False
#             c[i-first+(n-1)] = False
# queen(8)


# import sys
# n = int(sys.stdin.readline())

# pos = [0] * n #열
# flag_a = [False] * n #행
# flag_b = [False] * ((n * 2) - 1) #정방향 대각
# flag_c = [False] * ((n * 2) - 1) #역방향 대각
# sum = [0]


# def queen(i) -> None:
#     for j in range(n):
#         if(not flag_a[j]
#             and not flag_b[i+j]
#             and not flag_c[i-j+(n-1)]):
#             pos[i] = j
#             if i == n-1:
#                 # for i in range(n):
#                 #     print(f'{pos[i]:2}', end='')
#                 # print()
#                 sum[0] += 1
#             else:
#                 flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = True
#                 queen(i + 1)
#                 flag_a[j] = flag_b[i+j] = flag_c[i-j+(n-1)] = False
# queen(0)
# print(sum[0])

# import sys
# n = int(sys.stdin.readline())

# pos = [0] * n #열
# flag_a = [False] * n #행
# flag_b = [False] * ((n * 2) - 1) #정방향 대각
# flag_c = [False] * ((n * 2) - 1) #역방향 대각
# sum = [0]


# def queen(i) -> None:
#     for j in range(n):
#         if(not flag_a[j]
#             and not flag_b[i+j]
#             and not flag_c[i-j+7]):
#             pos[i] = j
#             if i == 7:
#                 # for i in range(8):
#                 #     print(f'{pos[i]:2}', end='')
#                 # print()
#                 sum[0] += 1
#             else:
#                 flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = True
#                 queen(i + 1)
#                 flag_a[j] = flag_b[i+j] = flag_c[i-j+7] = False
# queen(0)
# print(sum[0])

# https://seongonion.tistory.com/103
# import sys

# n = int(sys.stdin.readline())

# ans = 0
# row = [0] * n

# def is_promising(x):
#     for i in range(x):
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
#             return False
    
#     return True

# def n_queens(x):
#     global ans
#     if x == n:
#         ans += 1
#         return

#     else:
#         for i in range(n):
#             # [x, i]에 퀸을 놓겠다.
#             row[x] = i
#             if is_promising(x):
#                 n_queens(x+1)

# n_queens(0)
# print(ans)

# https://velog.io/@inhwa1025/BOJ-9663%EB%B2%88-N-Queen-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# n = int(input())
# result = 0


# # 퀸을 놓은 후 그 이후의 줄에 대해서만 불가능한 칸 체크
# def visit(x, y, in_visited):
#     tmp_visited = [visi[:] for visi in in_visited]
#     for i in range(1, n-x):
#         tmp_visited[x+i][y] = True  # 아래 방향 체크
#         if 0 <= y-i < n:
#             tmp_visited[x+i][y-i] = True    # 왼쪽 아래 대각선 체크
#         if 0 <= y+i < n:
#             tmp_visited[x+i][y+i] = True    # 오른쪽 아래 대각선 체크
#     return tmp_visited


# def recursion(q, _visited):     # q번째 줄에 퀸을 둘 수 있는 경우들을 확인하는 재귀함수
#     global result
#     # 한 줄에 퀸이 하나씩 들어가야 함
#     # 한 줄 전체가 불가능한 경우 아예 n개의 퀸을 모두 놓을 수 없으므로 재귀 종료
#     for idx in range(q, n):
#         if sum(_visited[idx]) == n:
#             return 0
#     # 마지막 줄에 도달한 경우 가능한 모든 경우를 세고 재귀 종료
#     if q == (n-1):
#         result += n - sum(_visited[q])
#         return 0

#     for i in range(n):
#         if not _visited[q][i]:   # 퀸을 둘 수 있는 경우
#             tmp = visit(q, i, _visited)     # 퀸을 뒀을 때 불가능한 칸들 체크
#             recursion(q+1, tmp)     # 그 다음 줄에 대해 재귀 호출
#         # 재귀호출 종료 후 퀸을 둘 수 있는 다른 경우에 대해 체크


# visited = [[False for _ in range(n)] for _ in range(n)]
# recursion(0, visited)   # 0번째 줄부터 탐색 시작
# print(result)



#박현우님의 코드
# nQueenCnt = 0
# n = int(input())
# board = [-1 for i in range(n)]

# def check(x):
#     for i in range(x):
#         if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
#             return False

#     return True

# def findNqueenCnt(idx):
#     global nQueenCnt

#     if idx == n:
#         nQueenCnt += 1
#         return

#     for i in range(n):
#         board[idx] = i

#         if check(idx):
#             findNqueenCnt(idx + 1)

# findNqueenCnt(0)
# print(nQueenCnt)


# https://fre2-dom.tistory.com/247

import sys
# pypy3 해결.. python(3%) 시간초과

# 대각선 체크 방법
# 현재 위치가 (3,3) 이라고 하면 왼쪽 대각선의 좌표는 (2,2),(1,1),(0,0) 이 된다.
# 

# 대각선의 퀸이 있는지 확인
def check(x):
    for i in range(x):
        if abs(graph[x] - graph[i]) == x - i:
            return False
    return True


# 체스 판의 열을 dfs 탐색
def dfs(queen):
    global res

    # n번째 퀸을 놓으려 한다면 리턴 (n개의 퀸을 놓았기 때문.)
    if queen == n:
        res += 1 # 방법의 수 카운트
        print(graph)
        return

    # 모든 체스판의 열을 확인
    for i in range(n):
        # i 번째 열의 퀸을 놓지 않았다면
        if not visited[i]:
            graph[queen] = i # (queen, i)에 퀸을 둔다.

            # 대각선의 겹치는 퀸이 있는지 확인
            if check(queen):
                # 백 트래킹
                visited[i] = True # 퀸을 놓는다.
                dfs(queen + 1) # 재귀적으로 퀸을 놓을 수 있는 열을 찾는다.
                visited[i] = False # 재귀 탐색 후 퀸을 n개 놓을 수 없다면 퀸을 놓지 않는 것으로 초기화 후 다른 열을 탐색


n = int(sys.stdin.readline())
graph = [0 for _ in range(n)] # n번째 열의 퀸의 위치
visited = [False for _ in range(n)] # 체스판의 탐색 여부
res = 0 # 퀸을 놓는 방법의 수

dfs(0)
print()
