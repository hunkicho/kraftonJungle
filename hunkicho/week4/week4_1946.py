# https://www.acmicpc.net/problem/1946

# import sys

# test_case = int(sys.stdin.readline().strip())

# for _ in range(test_case):
#     case_group = []
#     a = 0
#     b = 0
#     c = 100001
#     apply = int(sys.stdin.readline().strip())
#     print_num = apply
#     for _ in range(apply):
#         case_group.append(list(map(int, sys.stdin.readline().split())))
#     case_group.sort(key=lambda x: x[0])
#     #case_group = sorted(case_group, key=lambda x: (x[0]))
#     for i in case_group:
#         for j in range(i[0]):
#             if i[1] > case_group[j][1]:
#                 print_num -= 1
#                 break
#     print(print_num)

# https://velog.io/@jaenny/%EB%B0%B1%EC%A4%80-1946-%EC%8B%A0%EC%9E%85%EC%82%AC%EC%9B%90

import sys

test_case = int(sys.stdin.readline().strip())

for _ in range(test_case):
    case_group = []

    apply = int(sys.stdin.readline().strip())
    
    for _ in range(apply):
        case_group.append(list(map(int, sys.stdin.readline().split())))
    case_group.sort(key=lambda x: x[0])

    print_num = 1
    minimum = case_group[0][1]

    for i in range(1, apply):
        if case_group[i][1] <= minimum:
            minimum = case_group[i][1]
            print_num += 1
        
    print(print_num)