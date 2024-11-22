def solution(emergency):
    return [sum(1 for x in emergency if x > value) + 1 for value in emergency]
