# The main goal of this function is to travel in a tree using breadth first search
# The function takes arguments as graph and node from where the search has to be started 
def breadth_first_search(graph,node):
    visited = set()
    queue = [node]
    while len(queue) != 0:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            for neighbours in graph[vertex]:
                queue.append(neighbours)
    return visited

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

print(breadth_first_search(graph,'A'))