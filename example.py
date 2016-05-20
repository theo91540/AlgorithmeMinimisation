from CGS import *

cgs1 = CGS(3)

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")

edge1 = Edge(nodeA, nodeB, ["0","0","1"])
edge1 = Edge(nodeA, nodeB, ["0","0","0"])

edge2 = Edge(nodeC, nodeD, ["1","1","1"])
edge2 = Edge(nodeC, nodeD, ["0","0","1"])

cgs1.add_node(nodeA)
cgs1.add_node(nodeB)
cgs1.add_node(nodeC)
cgs1.add_node(nodeD)

cgs1.add_edge(edge1)
cgs1.add_edge(edge2)

partition = []
C1 = set()
C1.add(nodeA)
C1.add(nodeB)
C1.add(nodeC)
C1.add(nodeD)

partition.append(C1)

print("A")
print(nodeA)
print("B")
print(nodeB)
print("C")
print(nodeC)
print("D")
print(nodeD)

#print(equivalence(nodeA, nodeC, cgs1, partition))

print("Partition initiale: ")
print(partition)
print(len(partition))
pfinale = minimisation(cgs1, partition)
print("Partition finale : ")
print(pfinale)
print(len(pfinale))
