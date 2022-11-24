# https://www.acmicpc.net/problem/1541

# https://pacific-ocean.tistory.com/228

import sys

input = sys.stdin.readline().strip().split('-')

result = []

for i in input:
    if i.count('+') > 0:
        calc = i.split('+')
        num = 0
        for j in calc:
            num += int(j)
        result.append(num)
    else:
        result.append(i)

final_num = int(result[0])

for k in range(1,len(result)):
    final_num -= int(result[k])

print(final_num)