import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define a simplified Twitter user dataset (user, follows) relationships
twitter_users = {
  'User1': ['User2', 'User3', 'User4', 'User5', 'User6', 'User7'],
    'User2': ['User1', 'User3', 'User5', 'User6'],
    'User3': ['User1', 'User2', 'User4', 'User5', 'User7'],
    'User4': ['User1', 'User3', 'User5', 'User6', 'User7'],
    'User5': ['User2', 'User3', 'User4', 'User6', 'User7'],
    'User6': ['User4', 'User5', 'User7'],
    'User7': ['User1', 'User3', 'User4', 'User5', 'User6']
}

# Add nodes (Twitter users)
for user in twitter_users.keys():
    G.add_node(user)

# Add edges (follow relationships)
for user, follows in twitter_users.items():
    for follow in follows:
        G.add_edge(user, follow)

# Compute degree centrality
degree_centrality = nx.degree_centrality(G)

# Compute betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Compute closeness centrality
closeness_centrality = nx.closeness_centrality(G)

# Compute eigenvector centrality
eigenvector_centrality = nx.eigenvector_centrality(G)

# Compute diameter
try:
    diameter = nx.diameter(G)
except nx.NetworkXError:
    diameter = "Not connected"

# Print results
print("Degree Centrality:")
for node, centrality in degree_centrality.items():
    print(f"Node {node}: {centrality}")

print("\nBetweenness Centrality:")
for node, centrality in betweenness_centrality.items():
    print(f"Node {node}: {centrality}")

print("\nCloseness Centrality:")
for node, centrality in closeness_centrality.items():
    print(f"Node {node}: {centrality}")

print("\nEigenvector Centrality:")
for node, centrality in eigenvector_centrality.items():
    print(f"Node {node}: {centrality}")

print("\nDiameter:", diameter)
# Draw the graph
pos = nx.spring_layout(G)  # Layout for the graph
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, arrowsize=10)
plt.title("Cricket Social Network")
plt.show()
