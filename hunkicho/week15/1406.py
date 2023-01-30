# https://www.acmicpc.net/problem/1406

# 30분 안에 문제 못품
# 여기까지가 나의 풀이

# import sys
# import copy

# if __name__ == "__main__":
#     first_str = list(sys.stdin.readline().strip())
#     oper = int(sys.stdin.readline())
#     cursor = len(first_str)

#     for _ in range(oper):
#         command = list(map(str, sys.stdin.readline().rstrip()))
#         if command[0] == 'L':
#             cursor -= 1
#         if command[0] == 'D':
#             cursor += 1
#         if command[0] == 'B':
#             first_str = copy.deepcopy(first_str[cursor:])
#             cursor = 0
#         if command[0] == 'P':
#             cursor = 1 #???


# 답 봤다.
# https://seongonion.tistory.com/53

# import sys

# if __name__ == "__main__":
#     first_str = list(sys.stdin.readline().strip())
#     oper = int(sys.stdin.readline())
#     cursor = len(first_str)

#     for _ in range(oper):
#         command = list(map(str, sys.stdin.readline().rstrip()))
#         if command[0] == 'L':
#             if cursor > 0:
#                 cursor -= 1
#         if command[0] == 'D':
#             if cursor < len(first_str):
#                 cursor += 1
#         if command[0] == 'B':
#             if cursor > 0:
#                 first_str.remove(first_str[cursor - 1])
#         if command[0] == 'P':
#             first_str.insert(cursor, command[-1])
#             cursor += 1

#     print(''.join(first_str))


# 위에거 시간초과나서 내가 다시 스택 2개로 풀었다.
# 왜 시간초과인지 살펴보니 remove delete insert 는 시간복잡도가 O(N)이지만 append나 pop은 O(1)이라 시간초과가 난 듯 하다.
import sys

if __name__ == "__main__":
    first_str = list(sys.stdin.readline().strip())                     # 커서 기준 왼쪽
    last_str = []                                                      # 커서 기준 오른쪽
    oper = int(sys.stdin.readline())                                   # 명령어 개수

    for _ in range(oper):
        command = list(map(str, sys.stdin.readline().rstrip()))        # 명령어
        if command[0] == 'L':                                          # 왼쪽으로 이동시 오른쪽 리스트의 마지막 원소를 왼쪽으로 이동
            if len(first_str) > 0:                                     
                last_str.append(first_str.pop())
        if command[0] == 'D':                                          # 오른쪽으로 이동시 왼쪽 리스트의 마지막 원소를 오른쪽으로 이동
            if len(last_str) > 0:
                first_str.append(last_str.pop())
        if command[0] == 'B':                                          # 커서 왼쪽의 문자를 지울 시 왼쪽 리스트의 마지막 원소 제거
            if len(first_str) > 0:
                first_str.pop()
        if command[0] == 'P':                                          # 커서 왼쪽의 문자 추가 시 왼쪽 리스트 마지막에 원소 추가
            first_str.append(command[-1])

    if len(last_str) > 0:
        for _ in range(len(last_str)):
            first_str.append(last_str.pop())
            
    print(''.join(first_str))