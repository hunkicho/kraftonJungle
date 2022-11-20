# https://www.acmicpc.net/problem/9251

# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence#%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4longest-common-subsequence-%EA%B8%B8%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0
# https://ddongwon.tistory.com/106

# import sys

# str1 = list(sys.stdin.readline().strip())
# str2 = list(sys.stdin.readline().strip())

# lcs = [[0 for _ in range(len(str1) )] for _ in range(len(str2) )]


# for i in range(len(str1)):
#     for j in range(len(str2)):
#         if str1[i] == str2[j]:
#             lcs[i][j] = lcs[i - 1][j - 1] + 1
#         elif lcs[i - 1][j] >= lcs[i][j - 1]:
#             lcs[i][j] = lcs[i - 1][j]
#         else:
#             lcs[i][j] = lcs[i][j - 1]

# print(lcs)


# https://ddongwon.tistory.com/106

import sys

sys.setrecursionlimit(10 ** 6)

str1 = list(sys.stdin.readline().strip())
str2 = list(sys.stdin.readline().strip())

def lcs(arr1, arr2, len1, len2):
    if len1 == 0 or len2 == 0:
        return 0
    elif arr1[len1 - 1] == arr2[len2 - 1]:
        return 1 + lcs(arr1, arr2, len1 - 1, len2 - 1)
    else:
        return max(lcs(arr1, arr2, len1 - 1, len2), lcs(arr1, arr2, len1, len2 - 1))

print(lcs(str1, str2, len(str1), len(str2)))