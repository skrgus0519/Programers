def solution(n):
    result = []
    num = 1
    while len(result) < n:
        if num % 3 != 0 and "3" not in str(num):
            result.append(num)
        num += 1
    return result[-1]
