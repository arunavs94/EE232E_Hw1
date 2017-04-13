from igraph import *
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np

def main():
	# part1()
	# part3()
	part4()

def part1():

	# Generating random networks
	g1 = Graph.Erdos_Renyi(n=1000,p=0.01)
	g2 = Graph.Erdos_Renyi(n=1000,p=0.05)
	g3 = Graph.Erdos_Renyi(n=1000,p=0.1)

	# Plotting degree distributions
	plt.hist(g1.degree())
	plt.title('Degree distribution for n = 1000, p=0.01')
	plt.show()

	plt.hist(g2.degree())
	plt.title('Degree distribution for n = 1000, p=0.05')
	plt.show()

	plt.hist(g3.degree())
	plt.title('Degree distribution for n = 1000, p=0.1')
	plt.show()

	# Diameters of each graph
	print "The diameter of g1 is: ", g1.diameter(directed = False)
	print "The diameter of g2 is: ", g2.diameter(directed = False)
	print "The diameter of g3 is: ", g3.diameter(directed = False)

	# Checking connectivity (Sometimes hangs)
	if g1.is_connected() == 1:
		print "Graph g1 is connected."
	else:
		print "Graph g1 is disconnected."

	if g2.is_connected() == 1:
		print "Graph g2 is connected."
	else:
		print "Graph g2 is disconnected."

	if g3.is_connected() == 1:
		print "Graph g3 is connected."
	else:
		print "Graph g3 is disconnected."

	# # Sweeping across p-value, found threshold p to be 0.006-0.007
	pvals = np.linspace(0,0.05,51)

	for p_test in pvals:
		g_test = Graph.Erdos_Renyi(n=1000,p=p_test)

		if g_test.is_connected() == 1:
			print "Graph g_test is connected, with p = ", p_test
		else:
			print "Graph g_test is disconnected, with p = ", p_test

	

	
def part3():

	g1 = Graph.Erdos_Renyi(n=1000,p=0.01)
	g2 = Graph.Erdos_Renyi(n=1000,p=0.05)
	g3 = Graph.Erdos_Renyi(n=1000,p=0.1)

	g1.as_undirected()
	g2.as_undirected()
	g3.as_undirected()

def part4():

	# What are the specs of this?
	nodes = 1000
	fwprob = 0.37
	bwfactor = 0.32/0.37

	g1 = Graph.Forest_Fire(nodes, fwprob, bwfactor, directed = False)

	# # If direction degree dists are needed
	# dd_in = Graph.degree_distribution(g1,mode="in")
	# dd_out = Graph.degree_distribution(g1,mode="out")

	# Plotting degree distribution
	plt.hist(g1.degree())
	plt.title('Degree distribution for Forest Fire')
	plt.show()


if __name__ == '__main__':
	main()