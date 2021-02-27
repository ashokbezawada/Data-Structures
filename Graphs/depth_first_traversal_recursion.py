# the main goal of this function is to traverse the graph using the depth first traversal
# The function takes arguments as graph and a list to mark visited vertices and starting node

def depth_first_search_graph(graph,visited,node):
    if node not in visited:
        visited.append(node)
        print(node)
    for neighbour in graph[node]:
        depth_first_search_graph(graph,visited,neighbour)

#main
graph = {
    'A' : ['B'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

graph_1 = {'1':['2','4'],
         '2':['4','3','5'],
         '3':['5'],
         '4':[],
         '5':[]}

depth_first_search_graph(graph_1,[],'1')