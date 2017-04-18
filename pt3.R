
# clearing workspace
closeAllConnections()
rm(list=ls())

# importing library
library("igraph")

# initialize vars
nodesNum <-  1000

# generate network
g <-sample_pa_age(nodesNum, pa.exp=1, aging.exp=0, aging.bin=1000, directed = FALSE)

# find degree
deg_g <- degree(g)

# plot degree distribution
degree_dist <- hist(x = deg_g, breaks = seq(from = min(deg_g), to = max(deg_g), by=1), main = "Degree Distribution", xlab = "Degrees")

# generate community and modularity
comm_g <- fastgreedy.community(g)
mod_g <- modularity(comm_g)

#plot community distribution
cs <- hist( x= membership(comm_g), breaks = seq(from = min(deg_g), to = max(deg_g), by=1), main = "Community Distribution", xlab = "Community", ylab = "Community Size")

# plot the community and calculate the modularity
plot(comm_g, g, vertex.size=10, vertex.label.cex=0.1)
cat("Modularity: ", mod_g)

