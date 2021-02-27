# The main goal of this function is to clone a graph
# the function takes arguments as graph, new_graph, stack and visited

def clone_a_graph_dfs(graph,new_graph,stack,visited,node):
    if node not in stack:
        stack.append(node)
    while(len(stack) != 0):
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(node)
            new_graph[vertex] = list()
            for neighbour in graph[vertex]:
                stack.append(neighbour)
                new_graph[vertex].append(neighbour)
    return new_graph




# main
graph = {
    'A' : ['B'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set()
new_graph = {}
clone_a_graph_dfs(graph,new_graph,[],visited,'A')