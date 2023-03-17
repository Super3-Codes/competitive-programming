def superDigit(n, k):
    s = str(sum([int(i) for i in n]))
    if len(n) == 1:
        if k == 1:
            return n
        else:
            return superDigit(n * k, 1)
    else:
        return superDigit(s, k)
