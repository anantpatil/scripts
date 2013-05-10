#!/usr/bin/env python2.7

""" 
A script to build a maven module along with its dependencies. A
dependency graph is created and precedence is computed and build is
fired in the prcedence order.

    Usage:
    $ build.py module-1 // build module-1 along with dependencies
    $ build.py module-2 module-1 // build both along with dependencies
    $ build.py // build current module (project)

Algorithm:
1. Read the main pom file and build the universal set of modules for the
   project. Build a DG.
2. Make sure the DG is DAG. Print cycles found, if any. 
3. Read the pom file of module and get the dependent modules. Using the
   list from (1)  build the dependency graph. Find any cycles etc.
3. Fire the build in post-order DFS traversal.

Data structures:
A Symbol table for storing module vs vertex number.
Adjacency list for Directed graph.

Style:
Comletely test-driven.

TODO:
Add ability to fire parallel build. Take number of threads to be used as
an argument to program.

    $ build.py module-1 --parallel --thread-count 4

"""


#-----------------------------------------------------------------------
import os 
import unittest
#-----------------------------------------------------------------------

all_modules = [] # all the modules in project
build_modules = [] # modules to be built

def build():
    """
	Check ags.
	Read the module name(s): build_modules.
	Read the main POM file and get all the modules in project:
	all_modules
	Add all the modules in SDGBuilder.
	q.enque(build_modules)
	while(!isEmpty(q)):
	    m = q.delete()
	    for d in dep(m):
		SDGBuilder.addEdge(m, d)
		q.enque(d)
    """
    pass

def determine_build_order():
    """
	Determine the build order.
    """
    pass

def fire_build(module):
    """
	Fire Maven build for the module.
    """
    pass



def build_dep_graph():
    """
	Build the DG using SDG.
    """
    pass

def dep(stream, module):
    """
	Return list of dependencies for given module.
	Read POM file of m and get the dependencies.
	All modules matching names from the all_modules.
    """
    pass

def read_all_modules(stream):
    """
	Read all the modules from POM file. The given POM file should be
	MAIN POM file of project.
    """
    pass

#=======================================================================
#	Entry Point
#=======================================================================
def test_read_all_modules():
    # Create a MAIN POM file and see if modules are read.
    pass

def test_dep():
    # create a fake POM XML and make sure dependencies are listed.
    pass

def test_build_dep_graph():
    # Test the dependency graph.
    pass

def test_build_order():
    # Check the order of build determined by the alogrithm
    pass


if __name__ == '__main__':
    unittest.main()
