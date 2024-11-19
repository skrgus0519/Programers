def solution(num_list):
    i,j = 0,0
    for num in num_list:
        if num % 2 == 0:
            i += 1
        else:
            j += 1
    return i,j