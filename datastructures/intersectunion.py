def intersectold(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other:
                break
        else:
            res.append(x)
    return res

def unionold(seq1, seq2):
    res = list(seq1)
    for x in seq2:
        if not x in res:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

