# The main goal of this function is to find the target node using depth first search
# the function takes arguments as graph and visited set to mark visisted vertices and target and start node

def dfs_find_target(graph,visited,node,target):
    if node == target:
        return True
    if node not in visited:
        visited.add(node)
    found = False    
    for neighbour in graph[node]:
        if neighbour == target:
            print("node is found ")
            return True
        found = dfs_find_target(graph,visited,neighbour,target)
    return found

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()
print(dfs_find_target(graph,visited,"A","K"))
