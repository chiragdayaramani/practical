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

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  
  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')