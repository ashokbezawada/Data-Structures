# The main goal of this function is to implement the depth first search in non recursive way
# The function takes arguments as stack,graph,visited,node

def depth_first_search_iterative(graph,visited,stack,node):
    stack.append(node)
    while len(stack) != 0:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
        for neighbour in graph[vertex]:
            stack.append(neighbour)

graph = {
    'A' : ['B'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()
depth_first_search_iterative(graph,visited,[],"A") 