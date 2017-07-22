def search(start, goal, graph):
    solns = []
    generate([start], goal, solns, graph)
    solns.sort(key=lambda x: len(x))
    return solns

def searchnew(start, goal, graph):
    solns = generatenew(([start], []), goal, graph)
    solns.sort(key=lambda x: len(x))
    return solns

def generate(path, goal, solns, graph):
    state = path[-1]
    if state == goal:
        solns.append(path)
    else:
        for arc in graph[state]:
            if arc not in path:
                generate(path + [arc], goal, solns, graph)
                
def generatenew(paths, goal, graph):
    solns = []
    while paths:
        front, paths = paths
        state = front[-1]
        if state == goal:
            solns.append(front)
        else:
            for arc in graph[state]:
                if arc not in front:
                    paths = (front + [arc]), paths
    return solns
                
if __name__ == '__main__':
    import datastructures.graphtestfunc as graphtestfunc
    graphtestfunc.tests(search)
    print()
    graphtestfunc.tests(searchnew)