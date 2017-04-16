from igraph import *
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np

def main():
	# part1()
	# part2()
	# part3()
	part4()

def part1():

	print '/n-------------------- Question 1 --------------------/n'

	# initialize variables 
	g1_diameter = 0.0; g2_diameter = 0.0; g3_diameter = 0.0; 
	g1_con = 0.0; g2_con = 0.0; g3_con = 0.0; 
	p_tot = 0.0

	for i in range(0,100):
		p_temp = 0.0

		# Generating random networks
		g1 = Graph.Erdos_Renyi(n=1000,p=0.01)
		g2 = Graph.Erdos_Renyi(n=1000,p=0.05)
		g3 = Graph.Erdos_Renyi(n=1000,p=0.1)

		# Checking connectivity 
		if g1.is_connected() == 1:
			g1_con = g1_con + 1

		if g2.is_connected() == 1:
			g2_con = g2_con + 1

		if g3.is_connected() == 1:
			g3_con = g3_con + 1		

		# Calculate diameters 
		g1_diameter = g1_diameter + g1.diameter()
		g2_diameter = g2_diameter + g2.diameter()
		g3_diameter = g3_diameter + g3.diameter()	

		# Calculate threshold for p such that newtork is connected (part C)
		g_test = Graph.Erdos_Renyi(n=1000,p=p_temp)
		while g_test.is_connected() == 0 :
			p_temp = p_temp + .001
			g_test = Graph.Erdos_Renyi(n=1000,p=p_temp)

		p_tot = p_tot + p_temp

	# Plotting degree distributions 
	plt.hist(g1.degree(),bins = 30 )
	plt.title('Degree distribution for n = 1000, p=0.01')
	plt.xlabel('Degree')
	plt.ylabel('Frequency')
	plt.show()

	plt.hist(g2.degree(),bins = 30 )
	plt.title('Degree distribution for n = 1000, p=0.05')
	plt.xlabel('Degree')
	plt.ylabel('Frequency')
	plt.show()

	plt.hist(g3.degree(),bins = 30 )
	plt.title('Degree distribution for n = 1000, p=0.1')
	plt.xlabel('Degree')
	plt.ylabel('Frequency')
	plt.show()

	# Print diameters of each graph
	print "The average diameter for p = 0.01 over 100 trials is: ", g1_diameter/100
	print "The average diameter for p = 0.05 over 100 trials is: ", g2_diameter/100
	print "The average diameter for p = 0.1 over 100 trials is: ", g3_diameter/100

	# Print connected/disconnected percentages
	print "The probability for p = 0.01 being connected is: %", g1_con
	print "The probability for p = 0.05 being connected is: %", g2_con
	print "The probability for p = 0.1 being connected is: %", g3_con

	# Print p_c (part C)
	print "The threshold for p such that the network is connected is : ", p_tot/100





def part2():

	print '\n-------------------- Question 2 --------------------\n'

	# initialze variables 
	g1_diameter = 0.0; num_connectivity = 0.0

	for i in range(0,100):
		g1 = Graph.Barabasi(n=1000)

		# Calculate diameter
		g1_diameter = g1_diameter + g1.diameter()

		# Check connectivity
		if g1.is_connected():
			num_connectivity = num_connectivity + 1; 


	g2 = Graph.Barabasi(n=10000)

	# Plot degree distribution 
	plt.figure(2)
	plt.hist(g1.degree(), bins =20) 
	plt.title('Fat-Tailed Degree distribution ')
	plt.xlabel('Degree')
	plt.ylabel('Frequency')
	plt.show()

	# Giant connected component
	GCC1 = g1.clusters().giant()
	GCC1 = g2.clusters().giant()

	# fast greedy
	community1 = g1.community_fastgreedy()	
	community2 = g2.community_fastgreedy()	

	# Calculate modularity
	m1 = g1.modularity(community1.as_clustering())
	m2 = g2.modularity(community2.as_clustering())
	

	# Print variables 
	print 'Average diameter for network with 1,000 nodes is' , g1_diameter/100

	print 'Probability the fat-tailed network is connected is : %', num_connectivity

	print 'Modularity for network with 1,000 nodes is' , m1
	print 'Modularity for network with 10,000 nodes is' , m2


	

	
def part3():
	print '/n-------------------- Question 3 --------------------/n'

	g1 = Graph.Erdos_Renyi(n=1000,p=0.01)
	g2 = Graph.Erdos_Renyi(n=1000,p=0.05)
	g3 = Graph.Erdos_Renyi(n=1000,p=0.1)


	g1.as_undirected()
	g2.as_undirected()
	g3.as_undirected()

def part4():
	print '\n-------------------- Question 4 --------------------\n'
	# initialize variables 
	com_size_list = []; tot_modularity = 0.0; tot_diameter = 0.0;

	# What are the specs of this?
	nodes = 1000
	fwprob = 0.32	
	bwfactor = 0.32/0.37

	for i in range (0,100):
		g1 = Graph.Forest_Fire(n=nodes, fw_prob=fwprob, bw_factor=bwfactor, directed = True)

		# get community structure / modularity
		g1_undirected = g1.as_undirected()
		community = g1_undirected.community_fastgreedy()
		tot_modularity = tot_modularity + g1_undirected.modularity(community.as_clustering())

		# get diameter
		tot_diameter = tot_diameter + g1.diameter()

		# get community structure 
		community_subgraphs = community.as_clustering().subgraphs()
		com_size_list = com_size_list + [len(community_subgraphs)]

	# Plotting degree distribution / community structure
	plt.hist(g1.indegree(),bins=30)
	plt.title('In-Degree distribution for Forest Fire')
	plt.xlabel('Degree')
	plt.ylabel('Frequency')
	
	plt.figure()
	plt.hist(g1.outdegree(),bins=30)
	plt.title('Out-Degree distribution for Forest Fire')
	plt.xlabel('Degree')
	plt.ylabel('Frequency')

	plt.figure()
	plt.hist(com_size_list,bins=20)
	plt.title('Community Structure')
	plt.show()
	plt.xlabel('Community Size')
	plt.ylabel('Frequency')

	# print variables
	print "Average diameter of the forest fire directed network over 100 iterations is: ", tot_diameter/100
	print "Average Modularity over 100 iterations: ", tot_modularity/100

if __name__ == '__main__':
	main()
