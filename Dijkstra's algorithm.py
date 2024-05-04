import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(range(1, 101))

# Add edges with weights
for i in range(1, 100):
    G.add_edge(i, i+1, weight=i)
# Visualize the graph
nx.draw(G, with_labels=True)
plt.show()

# Dijkstra's algorithm
shortest_paths = nx.single_source_dijkstra_path(G, 1)
print("Shortest Paths from node 1:")
for node, path in shortest_paths.items():
    print(f"To node {node}: {path}, with length {nx.shortest_path_length(G, 1, node)}")

# Closeness Centrality
closeness_centrality = nx.closeness_centrality(G)
print("\nCloseness Centrality:")
for node, cc in closeness_centrality.items():
    print(f"Node {node}: {cc}")

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)
print("\nBetweenness Centrality:")
for node, bc in betweenness_centrality.items():
    print(f"Node {node}: {bc}")

# Degree Centrality
degree_centrality = nx.degree_centrality(G)
print("\nDegree Centrality:")
for node, dc in degree_centrality.items():
    print(f"Node {node}: {dc}")

# Diameter
diameter = nx.diameter(G)
print("\nDiameter:", diameter)

# Density
density = nx.density(G)
print("\nDensity:", density)

# Eigenvector Centrality
eigenvector_centrality = nx.eigenvector_centrality(G)
print("\nEigenvector Centrality:")
for node, ec in eigenvector_centrality.items():
    print(f"Node {node}: {ec}")

# Authority and Hub Scores
authority_scores, hub_scores = nx.hits(G)
print("\nAuthority Scores:")
print(authority_scores)
print("\nHub Scores:")
print(hub_scores)

# PageRank
pagerank = nx.pagerank(G)
print("\nPageRank:")
for node, pr in pagerank.items():
    print(f"Node {node}: {pr}")

# Significant Nodes
significant_nodes = nx.significant_nodes(G)
print("\nSignificant Nodes:")
print(significant_nodes)

# K-core Decomposition
k_core = nx.k_core(G)
print("\nK-Core Decomposition:")
print(k_core.nodes())

# Modularity Maximization
modularity_maximization = nx.community.modularity_maximization.greedy_modularity_communities(G)
print("\nModularity Maximization:")
for i, community in enumerate(modularity_maximization):
    print(f"Community {i+1}: {community}")

# Majors
majors = nx.majors(G)
print("\nMajors:")
print(majors)
