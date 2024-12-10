def solution(my_string):
    m = 0
    n = ''
    for i in my_string :

        if i in n :
            continue 
        else :
            n += i

    answer = n
    return answer