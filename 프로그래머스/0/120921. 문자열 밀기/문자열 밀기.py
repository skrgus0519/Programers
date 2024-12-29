def solution(A, B):
    if A == B:
        return 0

    length = len(A)
    for i in range(1, length + 1):
        rotated = A[-i:] + A[:-i]
        if rotated == B:
            return i

    return -1  
