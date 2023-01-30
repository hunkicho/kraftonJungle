# https://www.acmicpc.net/problem/1269


# 시간초과
# import sys

# if __name__ == "__main__":
#     a_count, b_count = map(int, sys.stdin.readline().split())
#     a = list(map(int, sys.stdin.readline().split()))
#     b = list(map(int, sys.stdin.readline().split()))
    
#     a.sort()
#     b.sort()

#     base_list = a if len(a) < len(b) else b
#     comp_list = a if len(a) > len(b) else b

#     base_count = 0
#     comp_count = len(comp_list)

#     for i in base_list:
#         for j in comp_list:
#             if i == j:
#                 comp_count -= 1
#                 break
#             if i < j:
#                 base_count += 1
#                 break
#     #print("base = ",base_count)
#     #print("comp = ",comp_count)

#     print(base_count + comp_count)


# 이것도 시간초과
# import sys
# import copy

# if __name__ == "__main__":
#     a_count, b_count = map(int, sys.stdin.readline().split())
    
#     a = list(map(int, sys.stdin.readline().split()))
#     b = list(map(int, sys.stdin.readline().split()))

#     a_copy = copy.deepcopy(a)
#     b_copy = copy.deepcopy(b)

    
#     a.sort()
#     b.sort()

#     base_list = a if len(a) < len(b) else b
#     comp_list = a if len(a) > len(b) else b

#     base_count = 0
#     comp_count = len(comp_list)

#     for i in a[:]:
#         if b_copy.count(i) > 0:
#             a.remove(i)

#     for i in b[:]:
#         if a_copy.count(i) > 0:
#             b.remove(i)        
        
#     print(len(a) + len(b))


# 파이썬 set -> 집합에 관련한 것을 처리하기 위해 만들어진 자료형
# set은 순서가 없고 값들의 중복이 불가능하다.
# 또한 mutable(값이 변하는) 객체이다.
# 순서가 없기 때문에 리스트나 튜플에서 사용하는 인덱싱이 불가능

import sys

if __name__ == "__main__":
    a_count, b_count = map(int, sys.stdin.readline().split())
    
    a = set(map(int, sys.stdin.readline().split()))
    b = set(map(int, sys.stdin.readline().split()))

    print(len(a ^ b))