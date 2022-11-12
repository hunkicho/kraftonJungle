# https://www.acmicpc.net/problem/5639

# https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-5639%EB%B2%88-%EC%9D%B4%EC%A7%84-%EA%B2%80%EC%83%89-%ED%8A%B8%EB%A6%AC
# 가장 앞에 있는 root 노드로 비교해서 left, right를 구분한 뒤, left,right에 대해 재귀함수를 호출하여 left+right+root 순으로 반환
# 입력의 길이가 정해져있지 않기 때문에 EOF가 입력되면 에러가 나는 것을 이용해 try-except를 통해 입력받는다는 점이 중요

# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline


# def getPostorder(nums):
#     length = len(nums)

#     if length <= 1:
#         return nums

#     for i in range(1, length):
#         if nums[i] > nums[0]:
#             return getPostorder(nums[1:i]) + getPostorder(nums[i:]) + [nums[0]]

#     return getPostorder(nums[1:]) + [nums[0]]

# if __name__ == '__main__':
#     nums = []
#     while True:
#         try:
#             nums.append(int(input()))
#         except:
#             break

#     nums = getPostorder(nums)
#     for n in nums:
#         print(n)


# https://backtony.github.io/algorithm/2021-02-18-algorithm-boj-class4-20/

import sys

# default 값이 1000이다
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def post_order(start, end):
    # 역전시 리턴
    if start > end:
        return

    # 루트 노드
    root = pre_order[start]
    idx = start + 1

    # root보다 커지는 지점을 찾는 과정
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리
    post_order(start + 1, idx - 1)

    # 오른쪽 서브트리
    post_order(idx, end)

    # 후위순회이므로 제일 마지막에 찍으면 된다
    print(root)


pre_order = []
while 1:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행
    except:
        break

post_order(0, len(pre_order) - 1)