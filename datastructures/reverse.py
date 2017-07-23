def reverse(list):
    if list == []:
        return []
    else:
        return reverse(list[1:]) + list[:1]
    
def reversenew(list):
    if not list:
        return list
    else:
        return reverse(list[1:]) + list[:1]
    
def ireverse(list):
    res = []
    for x in list:
        res = [x] + res
    return res

def ireversenew(list):
    res = list[:0]
    for i in range(len(list)):
        res = list[i:i+1] + res
    return res

