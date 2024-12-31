def solution(polynomial):
    x_coeff = 0
    constant = 0

    terms = polynomial.split(" + ")

    for term in terms:
        if "x" in term:
            if term == "x":
                x_coeff += 1
            else:
                x_coeff += int(term[:-1]) 
        else:
            constant += int(term)

    result = []
    if x_coeff > 0:
        result.append(f"{x_coeff}x" if x_coeff > 1 else "x")
    if constant > 0:
        result.append(str(constant))
    
    return " + ".join(result)
