# https://www.acmicpc.net/submit/2231

# import sys

# if __name__ == "__main__":
#     n = int(sys.stdin.readline())
#     max_base = 9 * 3
#     print_list = []

#     if n == 1:
#         print(0)
#     else:
#         for i in range(3, max_base):
#             constructor = n - i
#             print("cons = ",constructor)
#             hap = 0
#             for j in str(constructor):
#                 print(j)
#                 hap += int(j)
#             if constructor + hap == n:
#                 print_list.append(constructor)
#         print(min(print_list))


# import sys

# if __name__ == "__main__":
#     n = int(sys.stdin.readline())
#     max_base = 9 * len(str(n))
#     print_list = []

#     if n == 1:
#         print(0)
#     else:
#         for i in range(3, max_base):
#             constructor = n - i
#             print("cons = ",constructor)
#             hap = 0
#             for j in str(constructor):
#                 print(j)
#                 hap += int(j)
#             if constructor + hap == n:
#                 print_list.append(constructor)
#         print(min(print_list))

# 30분 넘어서 답 봤다
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    result = 0
    hap = 0

    for i in range(1, n + 1):       # 1부터 n까지
        for j in str(i):            # 각 자리 수를 분해
            hap += int(j)           # 자리수 합 구하기
        if i + hap == n:            # 분해합이 n과 같다면
            result = i
            break
        
    print(result)