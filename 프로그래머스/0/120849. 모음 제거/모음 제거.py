def solution(my_string):
    list = ['a','e','i','o','u']
    for i in list:
        my_string = my_string.replace(i, '')
    return my_string