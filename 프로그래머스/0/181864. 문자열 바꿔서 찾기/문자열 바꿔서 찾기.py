def solution(myString, pat):
    swapped = ''.join('B' if char == 'A' else 'A' for char in myString)
    
    return 1 if pat in swapped else 0
