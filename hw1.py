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

        g1_diameter = 0.0; g2_diameter = 0.0; g3_diameter = 0.0; 
        g1_con = 0.0; g2_con = 0.0; g3_con = 0.0; 
        p_tot = 0.0

        for i in range(0,100):
                p_temp = 0.0

                # Generating random networks
                g1 = Graph.Erdos_Renyi(n=1000,p=0.01)
                g2 = Graph.Erdos_Renyi(n=1000,p=0.05)
                g3 = Graph.Erdos_Renyi(n=1000,p=0.1)

                # Plotting degree distributions (how do we average histogram plots?)
                # plt.hist(g1.degree(),bins = 20 )
                # plt.title('Degree distribution for n = 1000, p=0.01')
                # plt.xlabel('Degree')
                # plt.ylabel('Density')
                # plt.show()

                # plt.hist(g2.degree(),bins = 25 )
                # plt.title('Degree distribution for n = 1000, p=0.05')
                # plt.xlabel('Degree')
                # plt.ylabel('Density')
                # plt.show()

                # plt.hist(g3.degree(),bins = 30 )
                # plt.title('Degree distribution for n = 1000, p=0.1')
                # plt.xlabel('Degree')
                # plt.ylabel('Density')
                # plt.show()

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

        print '\n Question 2 \n'

        g1_diameter = 0
        g1_degree = []

        for i in range(0,100): #100 instances
                # Generate network for n = 1,000 & 10,000 
                g1 = Graph.Barabasi(n=1000)
                g2 = Graph.Barabasi(n=10000)

                # Diameter of graph for n = 1,000
                g1_diameter = g1_diameter + g1.diameter()

                # concatenate each instance for histogram
                g1_degree = g1_degree + g1.degree()


        # Plot degree distribution 
        plt.figure(2)
        plt.hist(g1_degree, bins =20) 
        plt.title('Degree distribution for n = 1000 & degree distribution proportional to $x^{-3}$')
        plt.xlabel('Degree')
        plt.ylabel('Density')
        plt.show()

        print "The diameter of the graph with 1,000 nodes is: %", g1_diameter/100

        
        # #Check connectivity
        # if g1.is_connected():
        #       print "Graph with 1,000 nodes is connected."
        # else:
        #       print "Graph with 1,000 nodes is disconnected."

        # # Giant connected component
        # cluster1 = g1.clusters()
        # cluster2 = g2.clusters()

        # GCC1 = cluster1.giant()
        # GCC2 = cluster2.giant()

        # GCC1_community = GCC1.community_fastgreedy()  
        # GCC2_community = GCC2.community_fastgreedy()  

        # # Calculate modularity
        # m1 = Graph.modularity(GCC1_community,weights=None)
        # m2 = Graph.modularity(GCC2_community,weights=None)

        # print 'Modularity for network with 1,000 nodes is' , m1
        # print 'Modularity for network with 10,000 nodes is' , m2
        

        
def part3():

        g1 = Graph.Barabasi(n=1000, start_from=None)
        
        plt.hist(g1.degree(),bins = 100)
        plt.title('Degree distribution for Preferential Attachment')
        plt.show()

        comm = g1.community_fastgreedy()
        print "The modularity of the community structure is:", g1.modularity(comm.as_clustering())
        



def part4():

        print "Question 4---------------------------------------------------------"

        nodes = 1000
        fwprob = 0.50
        bwfactor = 0.65

        g1 = Graph.Forest_Fire(nodes, fwprob, bwfactor, directed = True)

        # In-Degree distribution 
        plt.hist(g1.indegree(), bins = 100)
        plt.title('In-Degree distribution for Forest Fire')
        plt.show()

        # Out-Degree distribution
        plt.hist(g1.outdegree(), bins = 100)
        plt.title('Out-Degree distribution for Forest Fire')
        plt.show()      


        #Find an average diameter for Forest Fire graphs
        diameter = 0.0
        for i in range(0,20):
                g2 = Graph.Forest_Fire(nodes, fwprob, bwfactor, directed = True)
                diameter += g2.diameter()
                
        print "The average diameter of the 1000 Node Forest Fire graph is:" , diameter/20

        #Measure the community structure
        print communities(g1)
        print "The modularity of the community structure is:", g1.modularity(comm.as_clustering())

if __name__ == '__main__':
        main()
