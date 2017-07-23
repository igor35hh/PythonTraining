def permute(list):
    if not list:
        return [list]
    else:
        res = []
        for i in range(len(list)):
            rest = list[:i] + list[i+1:]
            #print(n, i, rest)
            for x in permute(rest):
                res.append(list[i:i+1] + x)
                #print(n, res, list[i:i+1], x)
        return res
    
def subset(list, size):
    if size == 0 or not list:
        return [list[:0]]
    else:
        result = []
        for i in range(len(list)):
            pick = list[i:i+1]
            rest = list[:i] + list[i+1:]
            for x in subset(rest, size-1):
                result.append(pick + x)
        return result
    
def combo(list, size):
    if size == 0 or not list:
        return [list[:0]]
    else:
        result = []
        for i in range(0, (len(list) - size) + 1):
            pick = list[i:i+1]
            rest = list[i+1:]
            for x in combo(rest, size - 1):
                result.append(pick + x)
        return result
    
if __name__ == '__main__':
    num = [1,2,3]
    str = 'abs'

    b = permute(num)
    print(b)
    s = permute(str)
    print(s)
    
    b = combo(num, 2)
    print(b)
    s = combo(str, 2)
    print(s)
    
    b = subset(num, 2)
    print(b)
    s = subset(str, 2)
    print(s)
    