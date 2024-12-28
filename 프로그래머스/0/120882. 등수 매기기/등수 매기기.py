def solution(score):
    averages = [(sum(s) / 2, idx) for idx, s in enumerate(score)]
    
    sorted_averages = sorted(averages, key=lambda x: -x[0])
    
    ranks = [0] * len(score)
    
    rank = 1
    for i, (_, idx) in enumerate(sorted_averages):
        if i > 0 and sorted_averages[i][0] != sorted_averages[i - 1][0]:
            rank = i + 1
        ranks[idx] = rank
    
    return ranks
