#Lab Exercise - Implement Breadth First, Depth First and A* Search Algorithms
#Part 1 – Implement Breadth First Search Algorithm using a Queueimport numpy as np
from queue import Queue
graph={0:[1,3],1:[0,2,3],2:[1,4,5],3:[0,1,4],4:[2,3,5],5:[2,4],6:[]}
print("The adjacency List representing the graph is:")
print(graph)

def bfs(graph,source):
    Q=Queue()
    visited_vertices=set()
    Q.put(source)
    visited_vertices.update({0})
    while not Q.empty():
        vertex=Q.get()
        print(vertx,end="-->")
        for u in graph[vertex]:
            if u not in visited_vertices:
                Q.put(u)
                visited_vertices.update({u})
print("BFS traversal of graph with source 0 is:")