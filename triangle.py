def DetectTriangle(g):
    nodes = len(g)
    flag_triangle = 0

    # Consider every possible
    # triplet of edges in graph
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):

                # check the triplet
                # if it satisfies the condition
                if (i != j and i != k
                        and j != k and
                        g[i][j] and g[j][k]
                        and g[k][i]):
                 flag_triangle = "True"
    return flag_triangle



# Create adjacency matrix of an undirected graph
graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]
dict_graph = {
    1: [2,3,4],
    2:  [1,4],
    3:  [1,4],
    4:  [1,2,3]
}

graph_list = []

hubs = dict_graph.items()    # list of nodes and outgoing vertices
size = max(map(lambda hub: max(hub[0], max(hub[1])), hubs))+1   # matrix dimension is highest known node index + 1
matrix = [[None]*size for row in range(size)]      # set up a matrix of the appropriate size
#print (matrix)
for node, vertices in hubs: # loop through every node in dictionary
    for vertice in vertices: # loop through vertices
       if  vertice >0:
        matrix[vertice][node] = 1
       else:
           matrix[vertice][node] = 0
print (matrix)

print("Triangle(s) in undirected graph : %s" % DetectTriangle(graph))
print("Triangle(s) in undirected graph : %s" % DetectTriangle(matrix))


