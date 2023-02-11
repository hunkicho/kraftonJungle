# https://www.acmicpc.net/problem/6603


# 나의 틀린답
# import sys
# from itertools import combinations

# if __name__ == "__main__":
#     case = []
#     while True:
#         row = list(map(int, sys.stdin.readline().split()))
#         if row[0] == 0:
#             break

#         case.append(row[1:])
    
#     for i in case:
#         new_row = list(set(combinations(i, 6)))
#         new_row.sort()
#         for j in new_row:
#             print(j)
#         print("")


# 인터넷에서 찾아본거
# import itertools

# while True:

#     array = list(map(int, input().split()))

#     k = array[0]
#     S = array[1:]

#     for i in itertools.combinations(S, 6):
#         print(*i)

#     if k == 0:
#         exit()
#     print()


# 위 기반으로 내가 고쳐본거. 근데 위에게 더 깔끔해보인다.
# import sys
# from itertools import combinations

# if __name__ == "__main__":
#     case = []
#     while True:
#         row = list(map(int, sys.stdin.readline().split()))  # 테스트 케이스 입력
#         if row[0] == 0:
#             break

#         case.append(row[1:])                                # 맨 처음 숫자는 제시되는 숫자의 갯수이기 떄문에 뺀다.
    
#     for i in case:
#         new_row = combinations(i, 6)
#         for j in new_row:
#             print(*j)
#         print("")

# 이게 깔끔한듯
# from itertools import combinations

# while True:

#     array = list(map(int, input().split()))

#     k = array[0]
#     S = array[1:]

#     for i in combinations(S, 6):
#         print(*i)

#     if k == 0:
#         exit()
#     print()

def dfs(depth, idx):
    if depth == 6:
        print(*out)
        return

    for i in range(idx, k):
        out.append(S[i])
        dfs(depth + 1, i + 1)
        out.pop()


while True:
    array = list(map(int, input().split()))
    k = array[0]
    S = array[1:]
    out = []
    dfs(0, 0)
    if k == 0:
        exit()
    print()