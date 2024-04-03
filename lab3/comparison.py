import time
import random
import matplotlib.pyplot as plt
from collections import defaultdict, deque

# Class to represent a graph using adjacency list
class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def add_edge(self, u, v):
        self.adjList[u].append(v)

    def dfs(self, start_node):
        visited = [False] * (max(self.adjList.keys()) + 1)
        stack = [start_node]

        while stack:
            current_node = stack.pop()
            if not visited[current_node]:
                visited[current_node] = True
                stack.extend(self.adjList[current_node])

    def bfs(self, start_node):
        queue = deque([start_node])
        visited = [False] * (max(self.adjList.keys()) + 1)
        visited[start_node] = True

        while queue:
            current_node = queue.popleft()
            for neighbor in self.adjList[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

# Generate dense graph with specified number of nodes
def generate_dense_graph(num_nodes):
    graph = Graph()
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            graph.add_edge(i, j)
            graph.add_edge(j, i)
    return graph

# Generate sparse graph with specified number of nodes
def generate_sparse_graph(num_nodes, edge_probability=0.01):
    graph = Graph()
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < edge_probability:
                graph.add_edge(i, j)
                graph.add_edge(j, i)
    return graph

# Measure DFS traversal time
def measure_dfs(graph):
    start_time = time.time()
    graph.dfs(random.randint(0, len(graph.adjList) - 1))
    return time.time() - start_time

# Measure BFS traversal time
def measure_bfs(graph):
    start_time = time.time()
    graph.bfs(random.randint(0, len(graph.adjList) - 1))
    return time.time() - start_time

# Analyze traversal times for different graph sizes
graph_sizes = [50, 150, 400, 900, 1500, 2500, 4000, 5500, 8000]
dfs_times_dense = []
bfs_times_dense = []
dfs_times_sparse = []
bfs_times_sparse = []

for size in graph_sizes:
    dense_graph = generate_dense_graph(size)
    sparse_graph = generate_sparse_graph(size)
    dfs_time_dense = measure_dfs(dense_graph)
    bfs_time_dense = measure_bfs(dense_graph)
    dfs_time_sparse = measure_dfs(sparse_graph)
    bfs_time_sparse = measure_bfs(sparse_graph)
    dfs_times_dense.append(dfs_time_dense)
    bfs_times_dense.append(bfs_time_dense)
    dfs_times_sparse.append(dfs_time_sparse)
    bfs_times_sparse.append(bfs_time_sparse)

# Plot results
plt.plot(graph_sizes, dfs_times_dense, label='DFS Dense Graph', color='red', linestyle='-')
plt.plot(graph_sizes, dfs_times_sparse, label='DFS Sparse Graph', color='pink', linestyle='-')
plt.plot(graph_sizes, bfs_times_dense, label='BFS Dense Graph', color='blue', linestyle='-')
plt.plot(graph_sizes, bfs_times_sparse, label='BFS Sparse Graph', color='purple', linestyle='-')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.title('DFS and BFS Traversal Time for Dense and Sparse Graphs')
plt.legend()
plt.savefig('graph_traversal_times.png')
plt.show()
