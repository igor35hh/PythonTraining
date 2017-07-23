def sort(list, field):
    res = []
    for x in list:
        i = 0
        for y in res:
            if x[field] <= y[field]:
                break
            i += 1
        res[i:i] = [x]
    return res

def sortnew(seq, func=(lambda x,y: x <= y)):
    res = seq[:0]
    for j in range(len(seq)):
        i = 0
        for y in res:
            if func(seq[j], y):
                break
            i += 1
        res = res[:i] + seq[j:j+1] + res[i:]
    return res


if __name__ == '__main__':
    table = [{'name':'john', 'age':25}, {'name':'doe', 'age':32}]
    print(sort(table, 'name'))
    print(sort(table, 'age'))
    table = [{'name':'john', 'age':25}, {'name':'doe', 'age':32}]
    print(sortnew(list(table), (lambda x, y: x['name'] <= y['name'])))
    print(sortnew(tuple(table), (lambda x, y: x['age'] <= y['age'])))
    