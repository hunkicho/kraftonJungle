import sys

import math
from collections import deque

def bfs():
    q = deque()
    q.append([start, 0])

    # 방문여부
    visited = [0 for i in range(10000)]
    visited[start] = 1

    while q:
        now, cnt = q.popleft()
        # now를 숫자에서 문자로 변환
        strNow = str(now)

        # 빼낸 값이 end면 cnt 리턴 
        if now == end:
            return cnt

        for i in range(4):
            # 각 자리에 0 ~ 9를 넣어가며 소수인지 확인
            for j in range(10):
                #print(strNow[:i],"-",str(j), strNow[i+1:])
                temp = int(strNow[:i] + str(j) + strNow[i+1:])

                # 방문 X, 소수 O, 1000이상인 숫자
                if visited[temp] == 0 and array[temp] and temp >= 1000:
                    visited[temp] = 1
                    q.append([temp, cnt + 1])


###############################################
print(str(bin(1041))[2:])
n = 9999 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘 
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    start, end = map(int, sys.stdin.readline().split())

    result = bfs()
    print(result if result != None else "Impossible" )
