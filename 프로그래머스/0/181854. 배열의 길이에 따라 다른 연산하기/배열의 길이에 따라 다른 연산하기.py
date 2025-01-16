def solution(arr, n):
    is_odd_length = len(arr) % 2 == 1
    
    for i in range(len(arr)):
        if (is_odd_length and i % 2 == 0) or (not is_odd_length and i % 2 == 1):
            arr[i] += n
    return arr
