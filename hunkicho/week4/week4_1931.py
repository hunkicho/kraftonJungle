# https://www.acmicpc.net/problem/1931

# https://somjang.tistory.com/entry/BaekJoon-1931%EB%B2%88-%ED%9A%8C%EC%9D%98%EC%8B%A4-%EB%B0%B0%EC%A0%95-Python

import sys

count = int(sys.stdin.readline().strip())

meeting = []

for _ in range(count):
    meeting.append(list(map(int, sys.stdin.readline().split())))

# 빠르게 끝나는 회의 일수록 더 많은 회의가 진행될 수 있다 따라서 우선 끝나는 시간이 빠른 순서대로 정렬.
# 시작시간이 끝나는 시간과 최대한 가까이 있어야 회의 사이 시간을 최소화 하여 많은 회의가 진행되기 때문에 두번째로 시작하는 시간이 빠른 순서대로 정렬

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))  # 끝나는 시간으로 먼저 정렬, 이후 시작시간으로 정렬

cnt = 0
end = 0  # 끝나는 시간

for time in meeting:
    if time[0] >= end:  # 시작시간이 종료시간 이상이면 그 회의 가능
        cnt += 1
        end = time[1]

print(cnt)