# https://www.acmicpc.net/problem/1655

# 가운데를 말해요
# 우선순위 큐 이용
# 중간값보다 작은값들은 left에, 큰 값은 right에 저장
# left를 최대힙, right를 최소힙으로 하면 left에 가운데 수가 저장됨
# left와 right에 번갈아 넣어주는데 right에 넣을 때 left보다 작은 값 넣으면 left와 right의 루트값을 바꾼다.

import sys
import heapq

count = int(sys.stdin.readline().strip())

left = []
right = []
answer = []

for _ in range(count):
    number = int(sys.stdin.readline().strip())

    if len(left) == len(right):
        heapq.heappush(left, -number)
    else:
        heapq.heappush(right, number)

    if right and -left[0] > right[0]:
        left_val = heapq.heappop(left)
        rigth_val = heapq.heappop(right)

        heapq.heappush(left, -rigth_val)
        heapq.heappush(right, -left_val)

    print(-left[0])