def solution(arr, delete_list):
    delete_set = set(delete_list)  
    result = [num for num in arr if num not in delete_set]
    return result
