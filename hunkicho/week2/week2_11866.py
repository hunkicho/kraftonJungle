# https://www.acmicpc.net/problem/11866

# import sys

# n,k = list(map(int,sys.stdin.readline().split()))
# no = n
# front = k
# back = k
# print_list = "<"

# circle = [None] * n

# for i in range(n):
#     circle[i] = i + 1

# while no > 0:
#     if front >= n:
#         front = 0 + (front - n)
#     print_list += str(circle[front - 1]) + ", "
#     no -= 1
#     front += k

# print(print_list[:-2] + ">")


# https://my-coding-notes.tistory.com/84


n,k = map(int,input().split())
q = [i for i in range(1,n+1)]
r = []

while(q):
    for i in range(k-1):
        q.append(q.pop(0))
    r.append(str(q.pop(0)))
print("<", ", ".join(r), ">", sep="")