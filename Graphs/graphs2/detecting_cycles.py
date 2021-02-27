# The main goal of this function is to find whether the graph has cycle or not
# The function takes argument as graph and node


def find_cycles(graph,node):
    unvisited = [u for u in graph]
    stack = [node]
    visited = set()
    while unvisited:
        s = stack.pop()
        if s not in visited:
            visited.add(s)
            unvisited.remove(s)
        for neighbours in graph[s]:
            stack.append(neighbours)
        x = [i for i in stack]
        return_st = find_cycles_helper(x,graph,s)
        #print(stack)
        if s in return_st:
            #print("cycle exists")
            return True

def find_cycles_helper(rec_stack,graph,n):
    r_lst = []
    while rec_stack:
        rs = rec_stack.pop()
        if rs not in r_lst:
            r_lst.append(rs)
            for neighbours in graph[rs]:
                rec_stack.append(neighbours)
    return r_lst
        

graph_example_1 = { 0 : [1],
                    1 : [2],
                    2 : [3],
                    3 : [4],
                    4 : [1] }
                    
graph_example_2 = { 0 : [1, 2],
                    1 : [2],
                    2 : [] }

graph1 = { 0 : [1, 2],
           1 : [],
           2 : [3],
           3 : [4],
           4 : [2] }

graph2 = { 0 : [],
           1 : [2],
           2 : [],  
           3 : [4],
           4 : [5],
           5 : [3] }

print(find_cycles(graph_example_1,0))