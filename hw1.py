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

        print '\n-------------------- Question 1 --------------------\n'

        # initialize variables 
        g1_diameter = 0.0; g2_diameter = 0.0; g3_diameter = 0.0; 
        g1_con = 0.0; g2_con = 0.0; g3_con = 0.0; 
        p_tot = 0.0

        num_iterations = 100

        for i in range(0,num_iterations):
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
        plt.figure()
        plt.hist(g1.degree(),bins = 30 )
        plt.title('Q1: Degree distribution for n = 1000, p=0.01')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')

        plt.figure()
        plt.hist(g2.degree(),bins = 30 )
        plt.title('Q1: Degree distribution for n = 1000, p=0.05')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')

        plt.figure()
        plt.hist(g3.degree(),bins = 30 )
        plt.title('Q1: Degree distribution for n = 1000, p=0.1')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')


        # Print diameters of each graph
        print "Average diameter for p = 0.01 over", num_iterations, "iterations is: ", g1_diameter/num_iterations
        print "Average diameter for p = 0.05 over", num_iterations, "iterations is: ", g2_diameter/num_iterations
        print "Average diameter for p = 0.1 over", num_iterations, "iterations is: ", g3_diameter/num_iterations

        # Print connected/disconnected percentages
        print "Probability for p = 0.01 being connected is: %", (g1_con/num_iterations)*100
        print "Probability for p = 0.05 being connected is: %", (g2_con/num_iterations)*100
        print "Probability for p = 0.1 being connected is: %", (g3_con/num_iterations)*100

        # Print p_c (part C)
        print "Threshold for p such that the network is connected is : ", p_tot/num_iterations

        plt.show()



def part2():

        print '\n-------------------- Question 2 --------------------\n'

        # initialze variables 
        g1_diameter = 0.0; num_connectivity = 0.0; 
        g1_modularity = 0.0; g2_modularity = 0.0; 
        com_size_list = []

        num_iterations = 100

        for i in range(0,num_iterations):
                g1 = Graph.Barabasi(n=1000)
                g2 = Graph.Barabasi(n=10000)

                # Calculate diameter
                g1_diameter = g1_diameter + g1.diameter()

                # Check connectivity
                if g1.is_connected():
                        num_connectivity = num_connectivity + 1; 

                # fast greedy
                community1 = g1.community_fastgreedy()  
                community2 = g2.community_fastgreedy()  

                # Giant connected component
                GCC1 = community1.as_clustering().giant()
                GCC1 = community2.as_clustering().giant()

                # Calculate modularity
                g1_modularity = g1_modularity + g1.modularity(community1.as_clustering())
                g2_modularity = g2_modularity + g2.modularity(community2.as_clustering())

                # calculate community structure
                community1_subgraphs = community1.as_clustering().subgraphs()
                com_size_list = com_size_list + [len(community1_subgraphs)]

        # Plot degree distribution 
        plt.figure()
        plt.hist(g1.degree(), bins =20) 
        plt.title('Q2: Fat-Tailed Degree distribution ')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')

        plt.figure()
        plt.hist(com_size_list,bins=20)
        plt.title('Q2: Fat-Tailed Community Structure')
        plt.xlabel('Community Size')
        plt.ylabel('Frequency')


        # Print variables 
        print 'Average diameter for network with 1,000 nodes over', num_iterations, 'iterations : ' , g1_diameter/num_iterations
        print 'Probability the fat-tailed network is connected over', num_iterations, 'iterations  : %', (num_connectivity/num_iterations) * 100
        print 'Modularity for network with 1,000 nodes over', num_iterations, 'iterations : ' , g1_modularity/num_iterations
        print 'Modularity for network with 10,000 nodes over', num_iterations, 'iterations : ' , g2_modularity/num_iterations

        plt.show()
        

        
def part3():
        print '\n-------------------- Question 3 --------------------\n'

        # initialize variables 
        tot_modularity = 0.0 ; com_size_list = []; 

        num_iterations = 100

        for i in range (0,num_iterations):
                
                g = Graph.Barabasi(n=1000)

                # calculate modularity
                community = g.community_fastgreedy()
                tot_modularity = tot_modularity + g.modularity(community.as_clustering())

                # calculate community structure
                community_subgraphs = community.as_clustering().subgraphs()
                com_size_list = com_size_list + [len(community_subgraphs)]

        # plot degree distribution and community structure for 1 instance
        plt.figure()
        plt.hist(g.degree(),bins = 30)
        plt.title('Q3: Degree Distribution')
        plt.xlabel('Degree')
        plt.ylabel('Frequency')

        plt.figure()
        plt.hist(com_size_list,bins=10)
        plt.title('Q3: Community Structure')
        plt.xlabel('Community Size')
        plt.ylabel('Frequency')


        # print variables
        print "Average Modularity over", num_iterations, "iterations : ", tot_modularity/num_iterations
        print "Average Community Size over", num_iterations, "iterations : " , mean(com_size_list)

        plt.show()


def part4():
        print '\n-------------------- Question 4 --------------------\n'

        # initialize variables 
        com_size_list = []; tot_modularity = 0.0; tot_diameter = 0.0;

        # What are the specs of this?
        nodes = 1000    
        bwfactor = .65

        num_iterations = 20

        for i in range (0,num_iterations):
                g1 = Graph.Forest_Fire(n=nodes, fw_prob=.5, bw_factor=bwfactor, directed = True)

                # get community structure / modularity
                g1_undirected = g1.as_undirected()
                community = g1_undirected.community_fastgreedy()
                tot_modularity = tot_modularity + g1_undirected.modularity(community.as_clustering())

                # get diameter
                tot_diameter = tot_diameter + g1.diameter()

                # get community structure 
                community_subgraphs = community.as_clustering().subgraphs()
                com_size_list = com_size_list + [len(community_subgraphs)]

        # Plotting degree distribution for 5 instances w/ different fwprob
        for i in range (1,6):

                fwprob = i*.12
                g2 = Graph.Forest_Fire(n=nodes, fw_prob=fwprob, bw_factor=bwfactor, directed = True)

                # In-Degree distribution 
                plt.hist(g2.indegree(), bins = 100)
                plt.title('In-Degree distribution for Forest Fire with fwprob = %s' %fwprob)
                plt.xlabel('Degree')
                plt.ylabel('Frequency')
                plt.show()

                # Out-Degree distribution
                plt.hist(g2.outdegree(), bins = 100)
                plt.title('Out-Degree distribution for Forest Fire with fwprob = %s' %fwprob)
                plt.xlabel('Degree')
                plt.ylabel('Frequency')
                plt.show()  


        plt.figure()
        plt.hist(com_size_list,bins=20)
        plt.title('Q4: Forest Fire Community Structure')
        plt.xlabel('Community Size')
        plt.ylabel('Frequency')



        # print variables
        print "Average diameter of the forest fire directed network over", num_iterations, "iterations : ", tot_diameter/num_iterations
        print "Average Modularity over", num_iterations,"iterations : ", tot_modularity/num_iterations
        print "Average Community Size over" , num_iterations, "iterations : " , mean(com_size_list)

        plt.show()

if __name__ == '__main__':
        main()
