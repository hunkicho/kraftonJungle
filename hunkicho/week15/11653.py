# https://www.acmicpc.net/problem/11653

# 소인수 분해가 뭔지 몰라서 1차 구글 검색
# 어떻게 구현해야 할지 몰라서 2차 구글 검색

import sys

if __name__ == "__main__":
    number = int(sys.stdin.readline())
    check = 0

    for i in range(2, number + 1):      # 2부터 반복문으로 0으로 나누어 떨어지지 않을 때 까지 나눈다.
        while number % i ==0:
            print(i)
            number //= i