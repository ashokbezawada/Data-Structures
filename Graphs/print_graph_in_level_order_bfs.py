# The main goal of this function is to print the graph in level order 
# The function takes arguments as graph and start vertex

def print_graph_in_levelorder(graph,node):
    visited = set()
    queue = [node]
    visited.add(node)
    next_level = []
    while len(queue) != 0:
        vertex = queue.pop(0)
        print(vertex)
        for neighbours in graph[vertex]:
            if neighbours not in visited:
                visited.add(neighbours)
                next_level.append(neighbours)
        
        if len(queue) == 0:
            queue = next_level
            next_level = [] 
        #print(queue)

graph = {'A': ['B','C'],
         'B': ['D','E'],
         'C': ['F','G'],
         'D': ['A'],
         'E': ['B'],
         'F': ['A'],
         'G': ['B']}
print_graph_in_levelorder(graph,'A')