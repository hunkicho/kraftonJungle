# https://www.acmicpc.net/problem/1904

# https://blog.naver.com/occidere/220787441430

import sys

count = int(sys.stdin.readline().strip())

dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3, count + 1):
    dp[i] = (dp[i-2] + dp[i - 1]) % 15746

print(dp[count] )