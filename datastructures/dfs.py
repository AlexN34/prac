#/usr/bin/python3
#assume graph is adjacency matrix;
#graph[v][w] = edge from v- w
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, v):
    visited, stack = [], []
    stack.append(v)
    print("inside! {} {}".format(visited, stack))
    while len(stack) != 0:
        cur_vertex = stack.pop()
        # do stuff here
        print("just popped {}".format(cur_vertex))
        if cur_vertex not in visited:
            print("visiting {}".format(cur_vertex))
            visited.append(cur_vertex)
            print(visited)
            for edge in graph[cur_vertex]: # all adj edges
                stack.append(edge)
    return visited

if __name__ == "__main__":
    print(dfs(graph, 'D'))
