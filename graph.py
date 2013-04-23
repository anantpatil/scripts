#!/usr/bin/env python2.7
"""
    A module for Graph implementations.
    DG = Directed Graph.
    UG = Undirected Graph.
    SG = Symbol Graph.
    
    Undirected Graph
    ----
    Path, reachability: Is a vertex reachable from a given vertex.
    Shortest Path: Single source shortest path. What's the shortest path
    from v to w. Shortest path from multiple sources.
    Cycle: Is there a cycle in Grpah? Print all the cycles.
    Connectivity, connected components: How many connected components?
    Are v and w in same CC.
    Bipartite (2 colorability): Is the Graph two colorable?
    
    Directed Graph
    ----
    Path, reachability
    Shortest Path: Single source and multiple sources
    Cycle: Detect and print all cycles.
    Ordered Traversal
    Euler Path
    Hamilton Path
    Topological sort
    Strong connectivity
    Transitive closure for connectivity 

    Directed Graph: DFS, BFS, Ordered Traversal, Strong Connectivity,
    Euler Path, Hamilton Path, Topology Sorting, Transitive Closure

"""

#-----------------------------------------------------------------------
import unittest
#-----------------------------------------------------------------------

#=======================================================================
#	Undirected Graph
#=======================================================================
class UG:
    """
	An implementation of un-directed graph.
    """
    def __init__(self, v):
	"""
	    Init a un-directed graph with vertices numbered from 0..v.
	"""
	self.__V = v
	self.__E = 0
	self.__adj = []
	# Initialize a 2-D adjacency list with number of rows = v.
	for i in range(v):
	    self.__adj.append([])

    def V(self):
	"""
	    Return number of vertices.
	"""
	return self.__V

    def E(self):
	"""
	    Return number of edges.
	"""
	return self.__E
    
    def adj(self, v):
	"""
	    Returns all the vertices adjacent to v.
	"""
	return self.__adj[v]
    
    def addEdge(self, v, w):
	self.__adj[v].append(w)
	self.__adj[w].append(v)
	self.__E += 1

    def prettyPrint(self):
	for v in range(self.V()):
	    for w in self.adj(v):
		print str(v) + " - " + str(w)

#=======================================================================
#	Directed Graph
#=======================================================================
class DG:
    """
	An implementation of directed graph.
    """
    def __init__(self, v):
	"""
	    Init a dirercted graph with vertices numbered from 0..v.
	"""
	self.__V = v
	self.__E = 0
	self.__adj = []
	# Initialize a 2-D adjacency list with number of rows = v.
	for i in range(v):
	    self.__adj.append([])

    def V(self):
	"""
	    Return number of vertices.
	"""
	return self.__V

    def E(self):
	"""
	    Return number of edges.
	"""
	return self.__E
    
    def adj(self, v):
	"""
	    Returns all the vertices adjacent to v.
	"""
	return self.__adj[v]
    
    def addEdge(self, v, w):
	self.__adj[v].append(w)
	self.__E += 1

    def reverse(self):
	"""
	    Return a reverse of this Graph i.e. all edges are reversed
	    while the vertices remain same.
	"""
	R = DG(self.V())
	for v in xrange(self.V()):
	    for w in self.adj(v):
		R.addEdge(w, v)
	return R

    def prettyPrint(self):
	for v in range(self.V()):
	    for w in self.adj(v):
		print str(v) + " -> " + str(w)

#=======================================================================
#	Symbol Directed Graph
#=======================================================================
class SDG:
    """
	A symbol graph for refering to module names and graph vertex
	index.
    """
    def __init__(self):
	self.nameToIdxMap = dict()
	self.idxToNameMap = dict()
	self.count = 0 # keep track of next vertex number in graph

    def add_name(self, name):
	if name not in self.nameToIdxMap:
	    self.nameToIdxMap[name] = self.count
	    self.idxToNameMap[self.count] = name
	    self.count += 1

    def size(self):
	return self.count;

    def names(self):
	return self.nameToIdxMap.keys()

    def get_name(self, idx):
	return self.idxToNameMap[idx];

    def get_idx(self, name):
	return self.nameToIdxMap[name] 

class SDGBuilder:
    """
	A class to build SDG.
    """
    def __init__(self):
	g = SDG()

    def addSymbol(self, symbol):
	g.addName(symbol)
    
    def addAllSymbols(self, symbols):
	for sym in symbols:
	    g.addName(sym)

    def addEdge(self, src, dest):
	g.addEdge(src, dest)
    
#=======================================================================
#	Unit tets
#=======================================================================
class DGTestCase(unittest.TestCase):
    def test_init(self):
	g = DG(3)
	self.assertEquals(3, g.V())
	self.assertEquals(0, g.E())	

    def test_addEdge(self):
	g = DG(3)
	g.addEdge(0,1)
	g.addEdge(1,2)
	g.addEdge(2,0)
	g.addEdge(0,2)
	self.assertEquals(4, g.E())	

    def test_reverse(self):
	g = DG(3)
	g.addEdge(0,1)
	g.addEdge(1,2)
	g.addEdge(2,0)
	g.addEdge(0,2)
	r = g.reverse();
	adjToVer2 = [0, 1] # After reverse, 0, 1 are ajacent to 2
	self.assertEquals(adjToVer2, r.adj(2))

class DSGTestCase(unittest.TestCase):
    def test_add_name(self):
	symGraph = SDG()
	self.assertEquals(0, symGraph.size())
        symGraph.add_name("module-1");
	self.assertTrue("module-1" in symGraph.names())
	self.assertEquals(1, symGraph.size())
	self.assertEquals(0, symGraph.get_idx("module-1"))

#=======================================================================
#	Run Tests
#=======================================================================
if __name__ == '__main__':
    unittest.main()
