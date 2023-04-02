# https://www.acmicpc.net/problem/2343

# import sys

# if __name__ == "__main__":
#     lec_count, blue = map(int, sys.stdin.readline().split())
#     lec_list = list(map(int, sys.stdin.readline().split()))

#     pl = 0
#     pr = lec_count - 1

#     while True:
#         pc = (pl + pr) // 2 # 중앙 원소 인덱스
        


# def add_lesson():
#     cnt = 0  # 레코드 갯수 세기
#     sum_lesson = 0  # 한 레코드에 들어갈 레슨들의 합
#     for i in range(N):
#         if sum_lesson + lesson_list[i] > mid:
#             cnt += 1
#             sum_lesson = 0

#         sum_lesson += lesson_list[i]
#     else:
#         if sum_lesson:
#             cnt += 1
#     return cnt


# if __name__ == "__main__":
#     N, M = map(int, input().split())  # N: 레슨 수, M: 블루레이 수
#     lesson_list = list(map(int, input().split()))  # 레슨들

#     right = sum(lesson_list)   # 레슨을 하나의 레코드에 다 담을 수 있을 때 레코드의 크기는 레슨의 합이다
#     left = max(lesson_list)  # 레코드가 가질 수 있는 가장 작은 크기
#     while left <= right:
#         # 레코드 크기 중간값 구하기
#         mid = (left + right) // 2
#         cnt = add_lesson()
#         if cnt <= M:  # 레코드 숫자가 모자라면 레코드 크기(mid)를 줄인다.
#             right = mid - 1
#         elif cnt > M:  # 레코드 숫자가 더 많아지면 레코드 크기(mid)를 늘린다
#             left = mid + 1

#     # 답은 left 에 있다. (최소 크기)
#     print(left)



import sys

def count_blue():
    cnt = 0
    time = 0
    for i in range(n):
        if time + lecture[i] > mid:
            cnt += 1
            time = 0
        time += lecture[i]
    if time:
        cnt += 1
    return cnt


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lecture = list(map(int, sys.stdin.readline().split()))

    left = max(lecture)
    right = sum(lecture)

    while True:
        mid = (left + right) // 2
        cnt = count_blue()
        if left > right:
            break

        if cnt > m:
            left = mid + 1
        else:
            right = mid - 1
        
    print(left)































