def solution(lines):
    grid = [0] * 201

    for start, end in lines:
        for i in range(start + 100, end + 100):
            grid[i] += 1

    over_length = sum(1 for x in grid if x >= 2)

    return over_length
