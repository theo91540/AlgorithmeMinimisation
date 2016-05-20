#!/usr/bin/python3.5
#-*- coding: utf-8 -*-

class Node:

	def __init__(self, name):

		self.name = name

class Edge:

	def __init__(self, node1, node2, action):

		self.node1 = node1
		self.node2 = node2
		self.action = action

class CGS:

	def __init__(self, joueurs):

		self.list_nodes = set()
		self.list_edges = set()
		self.joueurs = joueurs


	def add_node(self, node):

		self.list_nodes.add(node)

	def add_edge(self, edge):

		self.list_edges.add(edge)

	def to_string(self):

		s = ""
		for n in self.list_nodes:
			s += n.name + "\n"
		return s


def nouvelle_coalition(C):

	pos = len(C) - 1
	while C[pos] == 1:
		pos -= 1

	C[pos] = 1
	while pos + 1 < len(C):
		C[pos+1] = 0
		pos += 1

	return C



def equivalence(s, t, cgs, partition):

	equivalence = True
	i = 1
	C = [0]*cgs.joueurs

	while i < pow(2,cgs.joueurs): 
	
		C = nouvelle_coalition(C)
		
		list_act = []

		for n in cgs.list_nodes:
			for e in cgs.list_edges:
				if e.node1 == n:
					a = []
					for m,c in enumerate(C):
						if c == 1:
							a.append(e.action[m])
					list_act.append(a)

		
		for act in list_act:

			SCluster = []
			TCluster = []

			for e in cgs.list_edges:
				
				if e.node1 == s:
					is_act = True
					z = 0
					for j,a in enumerate(e.action):
						if C[j] == 1:
							if a != act[z]:
								is_act = False
							z += 1

					if is_act:
						for cluster in partition:
							if e.node2 in cluster:
									SCluster.append(cluster)

			
				if e.node1 == t:
					is_act = True
					z = 0
					for j,a in enumerate(e.action):
						if C[j] == 1:
							if a != act[z]:
								is_act = False
							z += 1

					if is_act:
						for cluster in partition:
							if e.node2 in cluster:
									TCluster.append(cluster)


			testT = False
			testS = False
			for act in list_act:

				clusters_atteignablesT = []
				clusters_atteignablesS = []
				for e in cgs.list_edges:
					
					if e.node1 == t:
						is_act = True
						z = 0
						for j,a in enumerate(e.action):
							if C[j] == 1:
								if a != act[z]:
									is_act = False
								z += 1

						if is_act:
							for cluster in partition:
								if e.node2 in cluster:
										clusters_atteignablesT.append(cluster)

					if e.node1 == s:
						is_act = True
						z = 0
						for j,a in enumerate(e.action):
							if C[j] == 1:
								if a != act[z]:
									is_act = False
								z += 1

						if is_act:
							for cluster in partition:
								if e.node2 in cluster:
										clusters_atteignablesS.append(cluster)

				if clusters_atteignablesT == (SCluster):
					testT = True

				if clusters_atteignablesS == (TCluster):
					testS = True

			if not testS or not testT:
				equivalence = False

		i += 1	

	return equivalence


def minimisation(cgs, partition):
	pi = partition.copy()
	change = True
	
	while change:

		change = False
		
		for cluster in pi :
			
			B = split(cgs, cluster, pi)
			if B != cluster:
				
				pi.remove(cluster)
				pi.append(B[0])
				pi.append(B[1])
				change = True

	return pi

def split(cgs, cluster, pi):

	s = cluster.copy().pop()

	b1 = set()
	b2 = set()

	for t in cluster:
		setT = set()
		setT.add(t)
		if(equivalence(s, t, cgs, pi)):
			b1 = b1.union(setT)
		else:
			b2 = b2.union(setT)

	if len(b2) == 0:
		return b1
	else:

		return [b1, b2]