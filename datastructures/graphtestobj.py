from datastructures.graph import Graph

S = Graph('s')
P = Graph('p')
A = Graph('a')
M = Graph('m')

S.arcs = [P, M]
P.arcs = [S, M, A]
A.arcs = [M]

print(S.search(M))

#for name in "ABCDEFG":
    #exec("%s = Graph('%s')" % (name, name))
    
A = Graph('A')
B = Graph('B')
C = Graph('C')
D = Graph('D')
E = Graph('E')
F = Graph('F')
G = Graph('G')
    
A.arcs = [B, E, G]
B.arcs = [C]
C.arcs = [D, E]
D.arcs = [F]
E.arcs = [C, F, G]
G.arcs = [A]

A.search(G)
for (start, stop) in [(E, D), (A, G), (G, F), (B, A), (D, A)]:
    print(start.search(stop))
    