#!/usr/bin/env python2.7
"""
    A module for Graph implementations.
    DG = Directed Graph.
    UG = Un-directed Graph.
    SUG = Symbolic Un-directed Graph.
    SDG = Symbolic Directed Graph.
    
"""

#-----------------------------------------------------------------------
import unittest
#-----------------------------------------------------------------------

#=======================================================================
#	Undirected Graph
#=======================================================================

"""
    Following problems are solved for un-directed graphs:
    ----
    a. Path & Reachability: Is a vertex reachable from a given vertex.

    b. Shortest Path: Single source shortest path. What's the shortest path
       from v to w. Shortest path from multiple sources.

    c. Cycle: Is there a cycle in Graph? Print all the cycles.

    d. Connectivity, connected components: How many connected components?
       Are v and w in same CC.

    e. Bipartite (2 colorability): Is the Graph two colorable?
"""
    
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


class UGConnectedComponents:
    """
	Gives connected components of UG.
    """
    pass

#=======================================================================
#	Directed Graph
#=======================================================================

"""
    Following problems are solved for Directed Graph
    ----
    a. Path, reachability
    b. Shortest Path: Single source and multiple sources
    c. Cycle: Detect and print all cycles.
    d. Ordered Traversal
    e. Euler Path
    f. Hamilton Path
    g. Topological sort
    h. Strong connectivity
    i. Transitive closure for connectivity 
"""

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


class DGRechability:
    """
	Determines if a vertex is reachable from a given vertex.
	If reachable, then gives the path, not necessarily shortest
	path.
    """
    pass


class DGShortestPath:
    """
	Gives shotest path from single source or multiple source.
	Uses BFS.
    """
    pass


class DGOrderedTraversal:
    """
	Provides APIs for ordered traversal.
	Post-order.
	Pre-order.
	Reverse Post-order.
    """
    pass


class DGHamiltonianPath:
    """
	Gives Hamiltonian path for the graph.
    """
    pass


class DGCycles:
    """
	Detects if the DG has cycles.
	Gives list of all the cycles in the graph.
    """
    pass


class DGBipartite:
    """
	Detects if the graph is bipartite.
    """
    pass


class DGEulerPath:
    """
	Gives Euler path.
    """
    pass


class DGStrongConnectivity:
    """
	Gives all the strongly connected components in DG.
	Determines if two vertices are strongly connected.
	Uses Kosraju algorithm.
    """
    pass


class DGTransitiveClosure:
    """
	Transitive closure of DG.
	Used to determine is a pair of vertices are connected (not
	strongly though. Maintains a VxV matrix of boolean values to
	support O(1) query for whether two vertices are connected. 
    """
    pass
#=======================================================================
#	Symbol Directed Graph
#=======================================================================
class SDG:
    """
	A symbol graph for refering to module names and graph vertex
	index.
    """
    def __init__(self, nameToIdxMap, idxToNameMap, dg):
	self.__name_vs_idx = nameToIdxMap
	self.__idx_vs_name = idxToNameMap
	self.__dg = dg

    def size(self):
	return len(self.__name_vs_idx)

    def all_names(self):
	return self.__name_vs_idx.keys()

    def get_name(self, idx):
	return self.__idx_vs_name[idx];

    def get_idx(self, name):
	return self.__name_vs_idx[name] 

    def get_dg(self):
	return self.__dg

class SDGBuilder:
    """
	A class to build SDG.
	Keep a adjacency list and add symbol names and edges to it.
	When "build" is called, just initiate a SDG with all the data
	you have.
    """
    def __init__(self):
	self.__sym = []
	self.__adj = dict()

    def addSymbol(self, symbol):
	self.__sym.append(symbol)
    
    def addAllSymbols(self, symbols):
	for sym in symbols:
	    if symbol not in self.__sym:
		self.__sym.add(symbol)

    def addEdge(self, src, dest):
	self.__adj[src].append(dest) 

    def build(self):
	sg = SDG()
	for sym in self.__sym:
	    sg.add_name(sym) 

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
	idx_vs_name = {0:"one", 1:"two", 2:"three"}
	name_vs_idx = {"one":0, "two":1, "three":2}
	g = DG(3)
	g.addEdge(0,1)
	g.addEdge(1,2)
	g.addEdge(2,0)
	symGraph = SDG(idx_vs_name, name_vs_idx, g)
	self.assertEquals(3, symGraph.size())
        symGraph.add_name("module-1");
	self.assertTrue("module-1" in symGraph.names())
	self.assertEquals(4, symGraph.size())

#=======================================================================
#	Run Tests
#=======================================================================
if __name__ == '__main__':
    unittest.main()
