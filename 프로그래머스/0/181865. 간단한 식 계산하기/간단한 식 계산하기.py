def solution(binomial):
    a,b,c = map(str, binomial.split())
    if b == '+':
        return int(a) + int(c)
    elif b == '-':
        return int(a) - int(c)
    else:
        return int(a) * int(c)
    