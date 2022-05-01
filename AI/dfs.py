# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C','D'],
    'B' : ['E'],
    'C' : ['F','G'],
    'D' : ['H'],
    'E' : [],
    'F' : [],
    'G' : ['I'],
    'H' : ['J','K'],
    'I' : [],
    'J' : [],
    'K' : []
}

visited = [] # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')