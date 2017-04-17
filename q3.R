library ("igraph")

nodesNum = 1000
g = sample_pa_age(nodesNum, pa.exp=1, aging.exp=0, 
                  aging.bin=1000, directed = FALSE)
plot(g, vertex.size=8, vertex.label.cex=0.7)

fg = fastgreedy.community(g)
cmsize = sizes(fg)
