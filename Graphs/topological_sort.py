# The main goal of this function is to implment the topological sort
# The function takes arguments as graph and node

def topological_sort(graph,node):
    visited = set()
    stack = [node]
    new_lst = []
    while stack:
        s = stack.pop(0)
        if s not in visited:
            visited.add(s)
            new_lst.append(s)
            for neighbours in graph[s]:
                stack.append(neighbours)
    print(new_lst)
    return new_lst

#main
graph = {'1':['2','4'],
         '2':['4','3','5'],
         '3':['5'],
         '4':[],
         '5':[]}

topological_sort(graph,'1')