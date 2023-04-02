def solution(N):
    binary_number = str(bin(N))[2:]
    stack = []
    is_start = 0
    count = 0

    for i in binary_number:
        if i == "1":
            if is_start == 0:
                is_start = 1

        if is_start == 1:
            if i == "0":
                stack.append(i)
            else:
                count = len(stack) if len(stack) > count else count
                stack = []
    return count

print(solution(1041))