# The main goal of this function is to find target in the graph using breadth first search 
# The function takes arguments as graph, starting vertex and target

def find_target_using_dfs(graph,node,target):
    visited = set()
    queue = [node]
    while len(queue) != 0:
        vertex = queue.pop(0)
        if vertex == target:
            return True
        for neighbours in graph[vertex]:
            if neighbours not in visited:
                visited.add(neighbours)
                queue.append(neighbours)
    return False

graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

print(find_target_using_dfs(graph,'A','K'))

