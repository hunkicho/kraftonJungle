# https://www.acmicpc.net/problem/11053

# import sys

# def check_len(a: list) -> None:
#     a.sort()
#     cnt = 2
#     cur_num = a[0]
#     diff = a[1] - cur_num
#     cur_num = a[1]

#     for i in a[2:]:
#         if cur_num < i and (i - cur_num) == diff:
#             cnt += 1
#             cur_num = i
#     print(cnt)

# if __name__ == "__main__":
#     n = int(sys.stdin.readline())
#     a = list(map(int, sys.stdin.readline().split()))
    
#     check_len(a)


import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    dp = [0 for i in range(n)]

    for i in range(n):
        for j in range(i):
            print(i,j)
            if a[i] > a[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1
    print(max(dp))